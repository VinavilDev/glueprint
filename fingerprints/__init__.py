from .servers import SERVERS
from .languages import LANGUAGES, DATABASES
from .frameworks import FRAMEWORKS
from .frontend import FRONTEND
from .javascript import JAVASCRIPT
from .css import CSS
from .widgets import WIDGETS
from .analytics import ANALYTICS
from .services import SERVICES, HOSTING
from .meta import META, PROTOCOLS
from .cdn import CDN
from .waf import WAF
from .security import SECURITY_HEADERS, check_security


def load_all() -> dict:
    return {
        "servers": SERVERS,
        "languages": LANGUAGES,
        "databases": DATABASES,
        "frameworks": FRAMEWORKS,
        "frontend": FRONTEND,
        "javascript": JAVASCRIPT,
        "css": CSS,
        "widgets": WIDGETS,
        "analytics": ANALYTICS,
        "services": SERVICES,
        "hosting": HOSTING,
        "meta": META,
        "protocols": PROTOCOLS,
        "cdn": CDN,
        "waf": WAF,
    }


def get_all_names() -> list:
    fps = load_all()
    names = []
    for cat in fps.values():
        names.extend(cat.keys())
    return sorted(set(names))
