import requests
from requests.exceptions import RequestException, Timeout
from typing import Optional, Dict
from urllib.parse import urlparse


DEFAULT_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)


class HttpClient:
    def __init__(
        self,
        timeout: int = 10,
        verify_ssl: bool = True,
        user_agent: str = None,
        headers: Dict[str, str] = None,
        cookies: Dict[str, str] = None
    ):
        self.timeout = timeout
        self.verify_ssl = verify_ssl
        
        self.headers = {
            "User-Agent": user_agent or DEFAULT_UA,
            "Accept": "text/html,application/xhtml+xml,*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate",
        }
        if headers:
            self.headers.update(headers)
            
        self.cookies = cookies or {}
        self._session = requests.Session()

    def get(self, url: str, **kwargs) -> Optional[requests.Response]:
        try:
            return self._session.get(
                url,
                headers=self.headers,
                cookies=self.cookies,
                timeout=self.timeout,
                verify=self.verify_ssl,
                allow_redirects=True,
                **kwargs
            )
        except (Timeout, RequestException):
            return None

    def close(self):
        self._session.close()


def normalize_url(url: str) -> str:
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    return url


def get_base_url(url: str) -> str:
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}"
