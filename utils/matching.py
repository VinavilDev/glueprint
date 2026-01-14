import re
from typing import Optional, List, Tuple, Dict


GENERIC_HEADERS = frozenset({
    "X-Frame-Options",
    "X-Content-Type-Options",
    "X-XSS-Protection",
    "Cache-Control",
    "Pragma",
    "Content-Type",
    "Content-Length",
    "Date",
})


def match_header(headers: Dict[str, str], name: str, pattern: str) -> Tuple[bool, Optional[str]]:
    value = headers.get(name, "")
    if not value:
        return False, None
    try:
        if re.search(pattern, value, re.IGNORECASE):
            return True, value
    except re.error:
        pass
    return False, None


def match_cookies(names: List[str], full_string: str, patterns: List[str]) -> Tuple[bool, Optional[str]]:
    for pattern in patterns:
        try:
            for name in names:
                if re.search(pattern, name, re.IGNORECASE):
                    return True, name
            if re.search(pattern, full_string, re.IGNORECASE):
                return True, pattern
        except re.error:
            continue
    return False, None


def match_body(body: str, patterns: List[str]) -> List[str]:
    matches = []
    for pattern in patterns:
        try:
            match = re.search(pattern, body, re.IGNORECASE)
            if match:
                text = match.group()
                if len(text) > 80:
                    text = text[:80] + "..."
                matches.append(text)
        except re.error:
            continue
    return matches


def extract_version(text: str) -> Optional[str]:
    for p in [r"(\d+\.\d+\.\d+)", r"v(\d+\.\d+)", r"(\d+\.\d+)"]:
        m = re.search(p, text)
        if m:
            return m.group(1)
    return None


def is_generic(header_name: str) -> bool:
    return header_name in GENERIC_HEADERS
