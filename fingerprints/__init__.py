from .servers import SERVERS
from .languages import LANGUAGES, DATABASES
from .frameworks import FRAMEWORKS
from .frontend import FRONTEND
from .javascript import JAVASCRIPT
from .css import CSS
from .widgets import WIDGETS
from .analytics import ANALYTICS
from .services import SERVICES, HOSTING, COMMUNICATION
from .meta import META, PROTOCOLS
from .cdn import CDN
from .waf import WAF
from .ecommerce import ECOMMERCE
from .security_tools import SECURITY_TOOLS
from .cms import CMS
from .chat_support import CHAT_SUPPORT
from .dev_tools import DEV_TOOLS
from .social_media import SOCIAL_MEDIA
from .advertising import ADVERTISING, TAG_MANAGERS
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
        "communication": COMMUNICATION,
        "ecommerce": ECOMMERCE,
        "security_tools": SECURITY_TOOLS,
        "cms": CMS,
        "chat_support": CHAT_SUPPORT,
        "dev_tools": DEV_TOOLS,
        "social_media": SOCIAL_MEDIA,
        "advertising": ADVERTISING,
        "tag_managers": TAG_MANAGERS,
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
