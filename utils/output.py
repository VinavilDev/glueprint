import sys

try:
    import pyfiglet
    HAS_PYFIGLET = True
except ImportError:
    HAS_PYFIGLET = False

from ..models import ScanResult


class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"


if not sys.stdout.isatty():
    for attr in ["RED", "GREEN", "YELLOW", "BLUE", "PURPLE", "CYAN", "WHITE", "BOLD", "DIM", "RESET"]:
        setattr(Colors, attr, "")

C = Colors

CATEGORIES = {
    "servers": ("🖥️ ", "Web Server", C.BLUE),
    "languages": ("💻", "Language", C.PURPLE),
    "databases": ("🗄️ ", "Database", C.YELLOW),
    "frameworks": ("⚙️ ", "Framework", C.PURPLE),
    "frontend": ("🎨", "Frontend", C.CYAN),
    "javascript": ("📦", "JavaScript", C.YELLOW),
    "css": ("🎭", "CSS/Icons", C.PURPLE),
    "widgets": ("🎵", "Widgets", C.GREEN),
    "analytics": ("📊", "Analytics", C.WHITE),
    "services": ("🔌", "Services", C.BLUE),
    "hosting": ("☁️ ", "Hosting", C.CYAN),
    "ecommerce": ("🛒", "E-commerce", C.GREEN),
    "security_tools": ("🔐", "Security Tools", C.RED),
    "cms": ("📝", "CMS", C.PURPLE),
    "chat_support": ("💬", "Chat/Support", C.CYAN),
    "dev_tools": ("🛠️ ", "Dev Tools", C.YELLOW),
    "social_media": ("📱", "Social/Media", C.BLUE),
    "advertising": ("📺", "Advertising", C.YELLOW),
    "tag_managers": ("🏷️ ", "Tag Managers", C.WHITE),
    "meta": ("🔍", "SEO/Meta", C.DIM),
    "protocols": ("🔗", "Protocols", C.GREEN),
    "cdn": ("🌐", "CDN", C.CYAN),
    "waf": ("🛡️ ", "WAF", C.RED),
    "security": ("🔒", "Headers", C.GREEN),
}


def print_banner():
    if HAS_PYFIGLET:
        fig = pyfiglet.Figlet(font="slant")
        print(f"{C.CYAN}{fig.renderText('GluePrint')}{C.RESET}")
    else:
        print(f"\n{C.CYAN}{C.BOLD}  GluePrint{C.RESET}\n")
    print(f"{C.DIM}  Web Technology Fingerprinter{C.RESET}")
    print(f"{C.DIM}  {'─' * 40}{C.RESET}\n")


def print_results(result: ScanResult, verbose: bool = False):
    status_color = C.GREEN if 200 <= result.status_code < 400 else C.YELLOW
    print(f"  {C.WHITE}Target:{C.RESET} {result.url}")
    print(f"  {C.WHITE}Status:{C.RESET} {status_color}{result.status_code}{C.RESET}")
    print(f"  {C.DIM}{'─' * 50}{C.RESET}\n")

    by_category = {}
    for det in result.detections:
        by_category.setdefault(det.category, []).append(det)

    for cat_key, (icon, cat_name, color) in CATEGORIES.items():
        if cat_key not in by_category:
            continue
        
        detections = by_category[cat_key]
        print(f"  {C.BOLD}{icon} {cat_name}{C.RESET}")
        print(f"  {'─' * 40}")
        
        for det in sorted(detections, key=lambda x: -x.confidence):
            if det.confidence >= 85:
                conf_color = C.GREEN
            elif det.confidence >= 70:
                conf_color = C.YELLOW
            else:
                conf_color = C.RED
            
            version = f" v{det.version}" if det.version else ""
            print(f"    {color}●{C.RESET} {det.name}{version} {C.DIM}({conf_color}{det.confidence}%{C.RESET}{C.DIM}){C.RESET}")
            
            if verbose and det.evidence:
                for ev in det.evidence[:2]:
                    print(f"      {C.DIM}└─ {ev[:70]}{C.RESET}")
        print()

    missing = [h for h, v in result.security_headers.items() if not v and h in ("HSTS", "CSP")]
    if missing:
        print(f"  {C.YELLOW}⚠️  Missing:{C.RESET} {', '.join(missing)}\n")

    print(f"  {C.DIM}{'─' * 50}{C.RESET}")
    print(f"  {C.BOLD}Detected: {result.count} technologies{C.RESET}\n")


def print_error(msg: str):
    print(f"  {C.RED}✗{C.RESET} {msg}")


def print_success(msg: str):
    print(f"  {C.GREEN}✓{C.RESET} {msg}")
