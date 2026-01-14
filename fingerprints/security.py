SECURITY_HEADERS = {
    "HSTS": "Strict-Transport-Security",
    "CSP": "Content-Security-Policy",
    "X-Frame-Options": "X-Frame-Options",
    "X-Content-Type-Options": "X-Content-Type-Options",
    "X-XSS-Protection": "X-XSS-Protection",
    "Referrer-Policy": "Referrer-Policy",
    "Permissions-Policy": "Permissions-Policy",
}


def check_security(headers: dict) -> dict:
    return {name: header in headers for name, header in SECURITY_HEADERS.items()}
