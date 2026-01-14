import json
from typing import Dict, Set

from .models import Detection, ScanResult
from .fingerprints import load_all, check_security
from .utils.http import HttpClient, normalize_url, get_base_url
from .utils.matching import match_header, match_cookies, match_body, extract_version, is_generic


class GluePrint:
    def __init__(
        self,
        url: str,
        timeout: int = 10,
        verify_ssl: bool = True,
        user_agent: str = None,
        headers: Dict[str, str] = None,
        cookies: Dict[str, str] = None
    ):
        self.url = normalize_url(url)
        self.base_url = get_base_url(self.url)
        
        self.client = HttpClient(
            timeout=timeout,
            verify_ssl=verify_ssl,
            user_agent=user_agent,
            headers=headers,
            cookies=cookies
        )
        
        self.fingerprints = load_all()
        self.result = ScanResult(url=self.url)
        self._found: Set[str] = set()

    def scan(self, deep: bool = False) -> ScanResult:
        response = self.client.get(self.url)
        
        if not response:
            return self.result

        self.result.status_code = response.status_code
        self.result.headers = dict(response.headers)
        self.result.cookies = [c.name for c in response.cookies]

        body = response.text[:600000]

        # Check all fingerprint categories
        for category, fps in self.fingerprints.items():
            self._check_category(category, fps, response.headers, response.cookies, body)

        # Check security headers
        self.result.security_headers = check_security(response.headers)
        self._add_security_detections(response.headers)

        # Deep scan if requested
        if deep:
            self._deep_scan()

        # Sort by confidence
        self.result.detections.sort(key=lambda x: -x.confidence)
        
        return self.result

    def _check_category(self, category: str, fingerprints: dict, headers, cookies, body: str):
        for name, fp in fingerprints.items():
            if name in self._found:
                continue

            evidence = []
            specific_matches = 0
            version = None

            # Check headers
            if "headers" in fp:
                for header_name, pattern in fp["headers"].items():
                    matched, value = match_header(dict(headers), header_name, pattern)
                    
                    if matched:
                        evidence.append(f"Header: {header_name}")
                        
                        if not is_generic(header_name):
                            specific_matches += 1
                        
                        if not version and value:
                            version = extract_version(value)

            # Check cookies
            if "cookies" in fp:
                cookie_names = [c.name for c in cookies]
                cookie_string = "; ".join([f"{c.name}={c.value}" for c in cookies])
                
                matched, ev = match_cookies(cookie_names, cookie_string, fp["cookies"])
                
                if matched:
                    evidence.append(f"Cookie: {ev}")
                    specific_matches += 1

            # Check body
            if "body" in fp:
                matches = match_body(body, fp["body"])
                
                for m in matches:
                    evidence.append(f"Body: {m[:50]}")
                    specific_matches += 1
                    
                    if not version:
                        version = extract_version(m)

            # Decide if we should report this detection
            required = fp.get("requires", 1)
            
            if specific_matches >= required:
                confidence = min(fp.get("confidence", 70) + (specific_matches - 1) * 5, 98)
                self._add_detection(name, category, confidence, version, evidence)

    def _add_detection(self, name: str, category: str, confidence: int, version=None, evidence=None):
        if name in self._found:
            # Update existing detection if higher confidence
            for det in self.result.detections:
                if det.name == name and confidence > det.confidence:
                    det.confidence = confidence
            return
        
        self._found.add(name)
        
        detection = Detection(
            name=name,
            category=category,
            confidence=confidence,
            version=version,
            evidence=evidence or []
        )
        
        self.result.detections.append(detection)
        self.result.technologies.setdefault(category, []).append(name)

    def _add_security_detections(self, headers):
        for name, present in self.result.security_headers.items():
            if present:
                self._add_detection(name, "security", 100, None, ["Header present"])

    def _deep_scan(self):
        payloads = ["?id=1'", "?id=<script>"]
        
        for payload in payloads:
            response = self.client.get(self.url.rstrip('/') + payload)
            
            if response and response.status_code in [403, 406, 429, 503]:
                for name, fp in self.fingerprints.get("waf", {}).items():
                    if name in self._found:
                        continue
                    
                    if "body" in fp:
                        matches = match_body(response.text, fp["body"])
                        if matches:
                            self._add_detection(name, "waf", fp.get("confidence", 85), None, ["WAF triggered"])

        # Check common paths
        paths = ["/robots.txt", "/wp-json/", "/api/", "/feed/"]
        
        for path in paths:
            response = self.client.get(self.base_url + path)
            
            if response and response.status_code == 200:
                for cat in ["frameworks", "services", "meta"]:
                    if cat in self.fingerprints:
                        self._check_category(cat, self.fingerprints[cat], response.headers, response.cookies, response.text)

    def to_dict(self) -> dict:
        return {
            "url": self.result.url,
            "status_code": self.result.status_code,
            "technologies": self.result.technologies,
            "detections": [
                {
                    "name": d.name,
                    "category": d.category,
                    "confidence": d.confidence,
                    "version": d.version,
                    "evidence": d.evidence
                }
                for d in self.result.detections
            ],
            "security_headers": self.result.security_headers,
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent)
