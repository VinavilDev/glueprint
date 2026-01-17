LANGUAGES = {
    "PHP": {
        "headers": {"X-Powered-By": r"^PHP/?[\d.]*"},
        "cookies": [r"^PHPSESSID$"],
        "confidence": 95,
        "requires": 1,
    },
    "Python": {
        "headers": {"Server": r"Python|Werkzeug|gunicorn|uvicorn|daphne"},
        "confidence": 78,
        "requires": 1,
    },
    "Ruby": {
        "headers": {"Server": r"Phusion Passenger|WEBrick|Puma"},
        "cookies": [r"_session$"],
        "confidence": 75,
        "requires": 1,
    },
    "Java": {
        "headers": {"Server": r"Tomcat|Jetty|GlassFish"},
        "cookies": [r"^JSESSIONID$"],
        "confidence": 80,
        "requires": 1,
    },
    "ASP.NET": {
        "headers": {"X-Powered-By": r"ASP\.NET", "X-AspNet-Version": r"[\d.]+"},
        "cookies": [r"^ASP\.NET_SessionId$", r"^\.ASPXAUTH$"],
        "confidence": 95,
        "requires": 1,
    },
    "Node.js": {
        "headers": {"X-Powered-By": r"^Express$"},
        "body": [r"node_modules", r"nodejs\.org"],
        "confidence": 85,
        "requires": 1,
    },
    "Go": {
        "headers": {"Server": r"^Go-http"},
        "confidence": 85,
        "requires": 1,
    },
    "Rust": {
        "headers": {"Server": r"^Actix|^Rocket|^Warp"},
        "confidence": 82,
        "requires": 1,
    },
    "Perl": {
        "headers": {"Server": r"^Perl|mod_perl"},
        "confidence": 82,
        "requires": 1,
    },
    "ColdFusion": {
        "headers": {"Server": r"ColdFusion"},
        "cookies": [r"^CFID$", r"^CFTOKEN$"],
        "confidence": 90,
        "requires": 1,
    },
}

DATABASES = {
    "MySQL": {
        "body": [r"mysql", r"mysqli", r"MySQL server", r"SQL syntax.*MySQL"],
        "headers": {"X-Powered-By": r"MySQL"},
        "confidence": 75,
        "requires": 1,
    },
    "PostgreSQL": {
        "body": [r"PostgreSQL", r"pg_", r"psycopg"],
        "confidence": 75,
        "requires": 1,
    },
    "MongoDB": {
        "body": [r"mongodb", r"mongoose"],
        "confidence": 75,
        "requires": 1,
    },
    "Redis": {
        "body": [r"redis"],
        "confidence": 70,
        "requires": 1,
    },
    "SQLite": {
        "body": [r"sqlite", r"SQLite3"],
        "confidence": 70,
        "requires": 1,
    },
}
