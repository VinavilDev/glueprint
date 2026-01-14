META = {
    "Open Graph": {
        "body": [r'property="og:', r'<meta[^>]+og:title', r'<meta[^>]+og:image', r'og:description'],
        "confidence": 95,
        "requires": 1,
    },
    "Twitter Cards": {
        "body": [r'name="twitter:', r'<meta[^>]+twitter:card'],
        "confidence": 95,
        "requires": 1,
    },
    "Schema.org JSON-LD": {
        "body": [r'type="application/ld\+json"', r'"@context":\s*"https?://schema\.org"'],
        "confidence": 95,
        "requires": 1,
    },
    "Schema.org Microdata": {
        "body": [r'itemscope', r'itemtype="https?://schema\.org'],
        "confidence": 90,
        "requires": 1,
    },
    "Dublin Core": {
        "body": [r'name="DC\.', r'name="dc\.'],
        "confidence": 88,
        "requires": 1,
    },
    "RSS": {
        "body": [
            r'type="application/rss\+xml"',
            r'rel="alternate"[^>]+type="application/rss',
            r'/feed/?["\']',
            r'/rss/?["\']',
            r'\.rss["\']',
        ],
        "confidence": 92,
        "requires": 1,
    },
    "Atom Feed": {
        "body": [r'type="application/atom\+xml"'],
        "confidence": 88,
        "requires": 1,
    },
    "Canonical URL": {
        "body": [r'rel="canonical"'],
        "confidence": 92,
        "requires": 1,
    },
    "Hreflang": {
        "body": [r'hreflang="[a-z]{2}'],
        "confidence": 85,
        "requires": 1,
    },
    "AMP": {
        "body": [r'rel="amphtml"', r"cdn\.ampproject\.org", r"<html[^>]+amp"],
        "confidence": 95,
        "requires": 1,
    },
    "Manifest (PWA)": {
        "body": [r'rel="manifest"', r'manifest\.json'],
        "confidence": 90,
        "requires": 1,
    },
    "Service Worker": {
        "body": [r"serviceWorker\.register", r"navigator\.serviceWorker"],
        "confidence": 88,
        "requires": 1,
    },
    "Google Site Verification": {
        "body": [r'name="google-site-verification"'],
        "confidence": 92,
        "requires": 1,
    },
    "Bing Site Verification": {
        "body": [r'name="msvalidate\.01"'],
        "confidence": 90,
        "requires": 1,
    },
    "Facebook Domain Verification": {
        "body": [r'name="facebook-domain-verification"'],
        "confidence": 92,
        "requires": 1,
    },
    "Pinterest Site Verification": {
        "body": [r'name="p:domain_verify"'],
        "confidence": 88,
        "requires": 1,
    },
    "Apple Touch Icon": {
        "body": [r'rel="apple-touch-icon"'],
        "confidence": 85,
        "requires": 1,
    },
    "Viewport": {
        "body": [r'name="viewport"'],
        "confidence": 90,
        "requires": 1,
    },
    "Theme Color": {
        "body": [r'name="theme-color"'],
        "confidence": 85,
        "requires": 1,
    },
    "Preconnect": {
        "body": [r'rel="preconnect"'],
        "confidence": 82,
        "requires": 1,
    },
    "Preload": {
        "body": [r'rel="preload"'],
        "confidence": 82,
        "requires": 1,
    },
    "DNS Prefetch": {
        "body": [r'rel="dns-prefetch"'],
        "confidence": 82,
        "requires": 1,
    },
}
