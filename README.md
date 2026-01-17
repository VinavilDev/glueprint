<h1 align="center">GluePrint - Web Technology Fingerprinting</h1>

<p align="center">
  <img src="https://img.shields.io/badge/technologies-600+-blue" alt="technologies" />
  <img src="https://img.shields.io/badge/python-3.8+-green" alt="python" />
  <img src="https://img.shields.io/badge/license-MIT-orange" alt="license" />
  <br>
  <em>GluePrint is a web technology fingerprinting tool for security researchers
    <br> and penetration testers. Detect 600+ technologies from a single scan.</em>
  <br>
</p>

<p align="center">
  <a href="#installation"><strong>Installation</strong></a>
  ·
  <a href="#usage"><strong>Usage</strong></a>
  ·
  <a href="#detection-categories"><strong>Categories</strong></a>
  ·
  <a href="#contributing"><strong>Contributing</strong></a>
</p>

<hr>

## Documentation

- [Installation](#installation)
- [CLI Usage](#cli)
- [Library Usage](#library)
- [Detection Categories](#detection-categories)
- [Adding Fingerprints](#adding-fingerprints)

### Advanced

- [Deep Scan Mode](#deep-scan)
- [Custom Headers](#custom-headers)
- [JSON Export](#json-export)

## Installation

### Prerequisites

- Python 3.8+
- pip

### Setup

```bash
git clone https://github.com/VinavilDev/glueprint.git
cd glueprint
pip install -r requirements.txt
```

## Usage

### CLI

```bash
# Basic scan
python __main__.py -u https://example.com

# Deep scan with evidence
python __main__.py -u https://example.com --deep --verbose

# JSON output
python __main__.py -u https://example.com --json -o report.json

# Custom headers
python __main__.py -u https://example.com -H "Authorization: Bearer token"
```

### Library

```python
from core import GluePrint

scanner = GluePrint("https://example.com")
result = scanner.scan(deep=True)

for tech in result.detections:
    print(f"{tech.name}: {tech.confidence}%")

# Check specific technology
if result.has("WordPress"):
    print("WordPress detected")

# Filter by category
wafs = result.by_category("waf")

# Export to JSON
data = scanner.to_json()
```

## Detection Categories

| Category | Technologies | Examples |
|----------|-------------|----------|
| **Web Servers** | 20+ | Apache, nginx, IIS, LiteSpeed, Caddy |
| **Languages** | 10+ | PHP, Python, Ruby, Node.js, ASP.NET |
| **Databases** | 5+ | MySQL, PostgreSQL, MongoDB, Redis |
| **Frameworks** | 60+ | Laravel, Django, Rails, Next.js, WordPress |
| **Frontend** | 20+ | React, Vue, Angular, Svelte, HTMX |
| **JavaScript** | 200+ | jQuery, GSAP, Chart.js, Three.js, Socket.io |
| **CSS/Icons** | 50+ | Tailwind, Bootstrap, Font Awesome |
| **Analytics** | 60+ | Google Analytics, Matomo, Hotjar, Mixpanel |
| **E-commerce** | 110+ | Shopify, WooCommerce, Stripe, PayPal, Klarna |
| **Security** | 70+ | reCAPTCHA, Auth0, Sentry, Cloudflare Turnstile |
| **Widgets** | 40+ | YouTube, SoundCloud, Disqus, Twitter |
| **Services** | 60+ | Google Fonts, Algolia, Firebase, Twilio |
| **Hosting** | 15+ | Aruba, OVH, WP Engine, Vercel, Netlify |
| **CDN** | 17+ | Cloudflare, AWS CloudFront, Fastly, Akamai |
| **WAF** | 12+ | Cloudflare WAF, AWS WAF, ModSecurity |

## Features

- **Header Analysis** - Server, X-Powered-By, cookies
- **Body Pattern Matching** - Scripts, styles, meta tags
- **Version Extraction** - Automatic version detection
- **Confidence Scoring** - Evidence-based scoring system
- **Security Audit** - HSTS, CSP, X-Frame-Options
- **Deep Scan** - WAF triggering, path probing
- **JSON Export** - Automation-friendly output

## Adding Fingerprints

Add patterns to the appropriate file in `fingerprints/`:

```python
"Technology Name": {
    "headers": {"Header-Name": r"pattern"},
    "cookies": [r"cookie_pattern"],
    "body": [r"body_pattern_1", r"body_pattern_2"],
    "confidence": 90,
    "requires": 1,
},
```

## CLI Options

| Flag | Description |
|------|-------------|
| `-u, --url` | Target URL |
| `-d, --deep` | Deep scan mode |
| `-v, --verbose` | Show evidence |
| `-j, --json` | JSON output |
| `-o, --output` | Save to file |
| `-t, --timeout` | Request timeout |
| `--no-verify` | Skip SSL verification |
| `-H, --header` | Custom header |
| `-c, --cookie` | Custom cookie |

## Contributing

### Want to Help?

Read through our contributing guidelines and then check out issues labeled as <kbd>help wanted</kbd> or <kbd>good first issue</kbd>.

### Adding Technologies

1. Fork the repository
2. Add fingerprint patterns to the appropriate category file in `fingerprints/`
3. Test detection accuracy
4. Submit a pull request

## Community

- [Submit an Issue](https://github.com/VinavilDev/glueprint/issues)
- [Discussions](https://github.com/VinavilDev/glueprint/discussions)

**Find GluePrint useful? Give the repo a star ⭐**