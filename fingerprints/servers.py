SERVERS = {
    "Apache HTTP Server": {
        "headers": {"Server": r"^Apache"},
        "confidence": 95,
    },
    "nginx": {
        "headers": {"Server": r"^nginx"},
        "confidence": 95,
    },
    "IIS": {
        "headers": {"Server": r"^Microsoft-IIS"},
        "confidence": 95,
    },
    "LiteSpeed": {
        "headers": {"Server": r"^LiteSpeed"},
        "confidence": 95,
    },
    "Caddy": {
        "headers": {"Server": r"^Caddy"},
        "confidence": 92,
    },
    "OpenResty": {
        "headers": {"Server": r"^openresty"},
        "confidence": 95,
    },
    "Tengine": {
        "headers": {"Server": r"^Tengine"},
        "confidence": 95,
    },
    "Cherokee": {
        "headers": {"Server": r"^Cherokee"},
        "confidence": 92,
    },
    "Gunicorn": {
        "headers": {"Server": r"^gunicorn"},
        "confidence": 92,
    },
    "Uvicorn": {
        "headers": {"Server": r"^uvicorn"},
        "confidence": 92,
    },
    "Daphne": {
        "headers": {"Server": r"^daphne"},
        "confidence": 90,
    },
    "Tomcat": {
        "headers": {"Server": r"Tomcat|Apache-Coyote"},
        "confidence": 90,
    },
    "Jetty": {
        "headers": {"Server": r"Jetty"},
        "confidence": 90,
    },
    "Kestrel": {
        "headers": {"Server": r"^Kestrel"},
        "confidence": 92,
    },
    "Werkzeug": {
        "headers": {"Server": r"^Werkzeug"},
        "confidence": 90,
    },
    "Cowboy": {
        "headers": {"Server": r"^Cowboy"},
        "confidence": 90,
    },
    "Phusion Passenger": {
        "headers": {"Server": r"Phusion Passenger"},
        "confidence": 92,
    },
    "Cloudflare": {
        "headers": {"Server": r"^cloudflare$"},
        "confidence": 95,
    },
    "Vercel": {
        "headers": {"Server": r"^Vercel$"},
        "confidence": 95,
    },
    "Netlify": {
        "headers": {"Server": r"^Netlify$"},
        "confidence": 95,
    },
}
