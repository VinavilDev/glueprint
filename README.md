# GluePrint

A fast, accurate web technology fingerprinting tool built for security professionals.

Identifies servers, frameworks, JavaScript libraries, analytics, widgets, and more by analyzing HTTP responses and page content.

## Quick Start

```bash
git clone https://github.com/yourusername/glueprint.git
cd glueprint
pip install -r requirements.txt

python -m glueprint -u https://example.com
python -m glueprint -u https://example.com --deep --verbose
```

## What It Detects

| Category | Examples |
|----------|----------|
| Servers | Apache, nginx, IIS, LiteSpeed, Caddy |
| Languages | PHP, Python, Ruby, Node.js |
| Frameworks | Laravel, Django, Rails, Express, Next.js |
| Frontend | React, Vue, Angular, Svelte, Preact |
| JS Libraries | jQuery, GSAP, Anime.js, Swiper, Three.js |
| CSS | Bootstrap, Tailwind, Bulma, Font Awesome |
| Widgets | Spotify, SoundCloud, YouTube, Tidal, ReadSpeaker |
| Analytics | GA4, Matomo, Hotjar, Siteimprove, Plausible |
| CDN/WAF | Cloudflare, Fastly, Akamai, AWS |
| SEO | Open Graph, Twitter Cards, Schema.org, RSS |

## Usage

```bash
# Basic scan
python -m glueprint -u https://target.com

# Deep scan with WAF probing
python -m glueprint -u https://target.com --deep

# Verbose output showing evidence
python -m glueprint -u https://target.com -v

# JSON output
python -m glueprint -u https://target.com --json

# Save results
python -m glueprint -u https://target.com -o results.json

# Custom headers
python -m glueprint -u https://target.com -H "Authorization: Bearer token"
```

## As a Library

```python
from glueprint import GluePrint

scanner = GluePrint("https://target.com")
result = scanner.scan(deep=True)

for tech in result.detections:
    print(f"{tech.name}: {tech.confidence}%")

# Export
data = scanner.to_dict()
json_str = scanner.to_json()
```

## Adding Fingerprints

Each fingerprint supports:

- `headers` - HTTP header patterns
- `cookies` - Cookie name patterns  
- `body` - HTML/JS content patterns
- `confidence` - Base confidence score (0-100)
- `requires` - Minimum matches needed

Example:

```python
"MyFramework": {
    "headers": {"X-Powered-By": r"^MyFramework"},
    "cookies": [r"^myfw_session$"],
    "body": [r"myframework\.js", r"MyFramework\.init"],
    "confidence": 85,
    "requires": 1
}
```

## Project Structure

```
glueprint/
├── glueprint/
│   ├── core.py           # Scanner engine
│   ├── models.py         # Data structures
│   ├── fingerprints/
│   │   ├── servers.py    # Web servers
│   │   ├── frameworks.py # Backend frameworks
│   │   ├── frontend.py   # Frontend frameworks
│   │   ├── javascript.py # JS libraries
│   │   ├── css.py        # CSS frameworks & icons
│   │   ├── widgets.py    # Embeds & widgets
│   │   ├── analytics.py  # Analytics & tracking
│   │   ├── services.py   # APIs & services
│   │   ├── meta.py       # SEO & meta tags
│   │   ├── cdn.py        # CDN providers
│   │   └── waf.py        # Web firewalls
│   └── utils/
│       ├── http.py       # HTTP client
│       ├── matching.py   # Pattern matching
│       └── output.py     # CLI formatting
└── tests/
```

## Requirements

- Python 3.8+
- requests
- pyfiglet

## License

MIT
