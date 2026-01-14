CDN = {
    "Cloudflare": {
        "headers": {"CF-RAY": r".+", "CF-Cache-Status": r".+"},
        "cookies": [r"^__cf"],
        "confidence": 98,
        "requires": 1,
    },
    "AWS CloudFront": {
        "headers": {"X-Amz-Cf-Id": r".+", "X-Amz-Cf-Pop": r"[A-Z]{3}\d+"},
        "confidence": 95,
        "requires": 1,
    },
    "Fastly": {
        "headers": {"X-Served-By": r"cache-", "Fastly-Debug-Digest": r".+"},
        "confidence": 92,
        "requires": 1,
    },
    "Akamai": {
        "headers": {"X-Akamai-Transformed": r".+", "Server": r"AkamaiGHost"},
        "confidence": 95,
        "requires": 1,
    },
    "Vercel": {
        "headers": {"X-Vercel-Id": r".+", "X-Vercel-Cache": r".+"},
        "confidence": 95,
        "requires": 1,
    },
    "Netlify": {
        "headers": {"X-NF-Request-ID": r".+"},
        "confidence": 95,
        "requires": 1,
    },
    "Azure CDN": {
        "headers": {"X-MSEdge-Ref": r".+", "X-Azure-Ref": r".+"},
        "confidence": 92,
        "requires": 1,
    },
    "Google Cloud CDN": {
        "headers": {"Via": r"google"},
        "confidence": 78,
        "requires": 1,
    },
    "KeyCDN": {
        "headers": {"Server": r"^keycdn-engine$"},
        "confidence": 95,
        "requires": 1,
    },
    "StackPath": {
        "headers": {"X-HW": r".+"},
        "confidence": 88,
        "requires": 1,
    },
    "Sucuri": {
        "headers": {"X-Sucuri-ID": r".+"},
        "confidence": 95,
        "requires": 1,
    },
    "Incapsula": {
        "headers": {"X-CDN": r"^Incapsula$"},
        "cookies": [r"^incap_ses_", r"^visid_incap_"],
        "confidence": 95,
        "requires": 1,
    },
    "Varnish": {
        "headers": {"Via": r"varnish", "X-Varnish": r"\d+"},
        "confidence": 90,
        "requires": 1,
    },
    "Fly.io": {
        "headers": {"Fly-Request-Id": r".+"},
        "confidence": 92,
        "requires": 1,
    },
    "Render": {
        "headers": {"X-Render-Origin-Server": r".+"},
        "confidence": 90,
        "requires": 1,
    },
    "Railway": {
        "headers": {"Server": r"railway"},
        "confidence": 85,
        "requires": 1,
    },
    "Heroku": {
        "headers": {"Via": r"heroku"},
        "confidence": 85,
        "requires": 1,
    },
}
