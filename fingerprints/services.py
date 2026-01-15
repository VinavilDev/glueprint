SERVICES = {
    # Fonts
    "Google Fonts": {
        "body": [r"fonts\.googleapis\.com", r"fonts\.gstatic\.com"],
        "confidence": 95,
        "requires": 1,
    },
    "Adobe Fonts": {
        "body": [r"use\.typekit\.net", r"typekit\.com"],
        "confidence": 95,
        "requires": 1,
    },
    "Bunny Fonts": {
        "body": [r"fonts\.bunny\.net"],
        "confidence": 90,
        "requires": 1,
    },
    "Fontshare": {
        "body": [r"api\.fontshare\.com"],
        "confidence": 88,
        "requires": 1,
    },

    # CAPTCHA
    "reCAPTCHA": {
        "body": [r"google\.com/recaptcha", r"grecaptcha", r"g-recaptcha"],
        "confidence": 95,
        "requires": 1,
    },
    "hCaptcha": {
        "body": [r"hcaptcha\.com", r"h-captcha"],
        "confidence": 95,
        "requires": 1,
    },
    "Cloudflare Turnstile": {
        "body": [r"challenges\.cloudflare\.com/turnstile", r"cf-turnstile"],
        "confidence": 95,
        "requires": 1,
    },

    # Auth
    "Auth0": {
        "body": [r"auth0\.com"],
        "confidence": 92,
        "requires": 1,
    },
    "Firebase": {
        "body": [r"firebase\.google\.com", r"firebase\.js", r"firebaseapp\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "Okta": {
        "body": [r"okta\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "Clerk": {
        "body": [r"clerk\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Supabase": {
        "body": [r"supabase\.co"],
        "confidence": 88,
        "requires": 1,
    },

    # Payment
    "Stripe": {
        "body": [r"js\.stripe\.com", r"Stripe\s*\("],
        "confidence": 95,
        "requires": 1,
    },
    "PayPal": {
        "body": [r"paypal\.com/sdk", r"paypalobjects\.com"],
        "confidence": 95,
        "requires": 1,
    },
    "Braintree": {
        "body": [r"js\.braintreegateway\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "Square": {
        "body": [r"squareup\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Paddle": {
        "body": [r"cdn\.paddle\.com"],
        "confidence": 90,
        "requires": 1,
    },

    # Search
    "Algolia": {
        "body": [r"algoliasearch", r"algolia\.com", r"algolia\.net"],
        "confidence": 92,
        "requires": 1,
    },
    "Meilisearch": {
        "body": [r"meilisearch"],
        "confidence": 85,
        "requires": 1,
    },
    "DocSearch": {
        "body": [r"docsearch\.algolia\.com"],
        "confidence": 88,
        "requires": 1,
    },

    # Storage/CDN
    "AWS S3": {
        "body": [r"s3\.amazonaws\.com", r"\.s3\."],
        "confidence": 90,
        "requires": 1,
    },
    "Cloudinary": {
        "body": [r"res\.cloudinary\.com"],
        "confidence": 92,
        "requires": 1,
    },
    "Imgix": {
        "body": [r"\.imgix\.net"],
        "confidence": 90,
        "requires": 1,
    },
    "Uploadcare": {
        "body": [r"ucarecdn\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Bunny CDN": {
        "body": [r"b-cdn\.net"],
        "confidence": 90,
        "requires": 1,
    },

    # Error Tracking
    "Sentry": {
        "body": [r"browser\.sentry-cdn\.com", r"sentry\.io", r"Sentry\.init"],
        "confidence": 92,
        "requires": 1,
    },
    "Bugsnag": {
        "body": [r"bugsnag\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Rollbar": {
        "body": [r"rollbar\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Datadog RUM": {
        "body": [r"datadoghq\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "New Relic": {
        "body": [r"newrelic\.com", r"js-agent\.newrelic\.com"],
        "confidence": 90,
        "requires": 1,
    },

    # Push Notifications
    "OneSignal": {
        "body": [r"onesignal\.com"],
        "confidence": 92,
        "requires": 1,
    },
    "Pusher": {
        "body": [r"pusher\.com", r"js\.pusher\.com"],
        "confidence": 88,
        "requires": 1,
    },

    # Social Login
    "Google Sign-In": {
        "body": [r"accounts\.google\.com/gsi"],
        "confidence": 92,
        "requires": 1,
    },
    "Facebook Login": {
        "body": [r"connect\.facebook\.net.*sdk\.js", r"FB\.login"],
        "confidence": 90,
        "requires": 1,
    },
    "Apple Sign-In": {
        "body": [r"appleid\.cdn-apple\.com"],
        "confidence": 90,
        "requires": 1,
    },

    # CDN
    "jsDelivr": {
        "body": [r"cdn\.jsdelivr\.net"],
        "confidence": 90,
        "requires": 1,
    },
    "unpkg": {
        "body": [r"unpkg\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "cdnjs": {
        "body": [r"cdnjs\.cloudflare\.com"],
        "confidence": 90,
        "requires": 1,
    },

    # Misc
    "Gravatar": {
        "body": [r"gravatar\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Akismet": {
        "body": [r"akismet\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Cookie Consent (Osano)": {
        "body": [r"osano\.com", r"cookieconsent"],
        "confidence": 85,
        "requires": 1,
    },
    "Cookiebot": {
        "body": [r"cookiebot\.com", r"Cookiebot"],
        "confidence": 90,
        "requires": 1,
    },
    "OneTrust": {
        "body": [r"onetrust\.com", r"optanon"],
        "confidence": 90,
        "requires": 1,
    },
}

HOSTING = {
    "Aruba.it": {
        "headers": {"Server": r"Aruba"},
        "body": [r"aruba\.it", r"arubacloud"],
        "confidence": 85,
        "requires": 1,
    },
    "OVH": {
        "headers": {"Server": r"OVH"},
        "body": [r"ovh\.com", r"ovhcloud"],
        "confidence": 85,
        "requires": 1,
    },
    "Hetzner": {
        "body": [r"hetzner\.com", r"hetzner\.cloud"],
        "confidence": 85,
        "requires": 1,
    },
    "DigitalOcean": {
        "body": [r"digitalocean\.com", r"digitaloceanspaces"],
        "confidence": 85,
        "requires": 1,
    },
    "Linode": {
        "body": [r"linode\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Vultr": {
        "body": [r"vultr\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "GoDaddy": {
        "body": [r"godaddy\.com", r"secureserver\.net"],
        "confidence": 85,
        "requires": 1,
    },
    "Bluehost": {
        "body": [r"bluehost\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "SiteGround": {
        "body": [r"siteground\.com", r"sgvps\.net"],
        "confidence": 85,
        "requires": 1,
    },
    "WP Engine": {
        "headers": {"X-Powered-By": r"WP Engine"},
        "body": [r"wpengine\.com", r"wpe-"],
        "confidence": 92,
        "requires": 1,
    },
    "Kinsta": {
        "headers": {"X-Kinsta-Cache": r".+"},
        "body": [r"kinsta\.com", r"kinsta\.cloud"],
        "confidence": 92,
        "requires": 1,
    },
    "Pantheon": {
        "headers": {"X-Pantheon-Styx-Hostname": r".+"},
        "confidence": 95,
        "requires": 1,
    },
}
