WAF = {
    "Cloudflare WAF": {
        "headers": {"CF-RAY": r".+"},
        "body": [r"Attention Required! \| Cloudflare", r"cf-error-details"],
        "confidence": 95,
        "requires": 1,
    },
    "AWS WAF": {
        "body": [r"Request blocked", r"AWS WAF"],
        "confidence": 80,
        "requires": 1,
    },
    "ModSecurity": {
        "headers": {"Server": r"mod_security|ModSecurity"},
        "body": [r"ModSecurity"],
        "confidence": 88,
        "requires": 1,
    },
    "Imperva/Incapsula": {
        "headers": {"X-CDN": r"^Incapsula$"},
        "cookies": [r"^incap_ses_", r"^visid_incap_"],
        "body": [r"Request unsuccessful\. Incapsula"],
        "confidence": 95,
        "requires": 1,
    },
    "F5 BIG-IP ASM": {
        "headers": {"Server": r"^BigIP$"},
        "cookies": [r"^BIGipServer"],
        "confidence": 88,
        "requires": 1,
    },
    "Barracuda": {
        "headers": {"Server": r"^Barracuda"},
        "confidence": 90,
        "requires": 1,
    },
    "Fortinet FortiWeb": {
        "headers": {"Server": r"FortiWeb"},
        "cookies": [r"^FORTIWAFSID$"],
        "confidence": 92,
        "requires": 1,
    },
    "Citrix NetScaler": {
        "headers": {"Via": r"NS-CACHE"},
        "confidence": 88,
        "requires": 1,
    },
    "PerimeterX": {
        "cookies": [r"^_px"],
        "body": [r"blocked by PerimeterX"],
        "confidence": 90,
        "requires": 1,
    },
    "DataDome": {
        "headers": {"X-DataDome": r".+"},
        "cookies": [r"^datadome$"],
        "confidence": 95,
        "requires": 1,
    },
    "Wordfence": {
        "body": [r"wordfence", r"wfwaf-authcookie"],
        "confidence": 88,
        "requires": 1,
    },
    "Sucuri WAF": {
        "headers": {"X-Sucuri-ID": r".+"},
        "body": [r"Sucuri Website Firewall"],
        "confidence": 95,
        "requires": 1,
    },
}
