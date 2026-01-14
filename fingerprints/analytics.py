ANALYTICS = {
    # Google
    "Google Analytics 4": {
        "body": [r"gtag\s*\(\s*['\"]config['\"]", r"G-[A-Z0-9]{10,}", r"googletagmanager\.com/gtag"],
        "confidence": 95,
        "requires": 1,
    },
    "Google Tag Manager": {
        "body": [r"googletagmanager\.com/gtm\.js", r"GTM-[A-Z0-9]+"],
        "confidence": 95,
        "requires": 1,
    },
    "Google Analytics (Universal)": {
        "body": [r"google-analytics\.com/analytics\.js", r"UA-\d+-\d+"],
        "confidence": 92,
        "requires": 1,
    },

    # Privacy-focused
    "Matomo Analytics": {
        "body": [
            r"matomo\.js",
            r"matomo\.php",
            r"piwik\.js",
            r"piwik\.php",
            r"_paq\.push",
            r"matomo\.",
            r"cdn\.matomo\.cloud",
        ],
        "confidence": 95,
        "requires": 1,
    },
    "Plausible": {
        "body": [r"plausible\.io/js"],
        "confidence": 95,
        "requires": 1,
    },
    "Fathom": {
        "body": [r"cdn\.usefathom\.com"],
        "confidence": 92,
        "requires": 1,
    },
    "Simple Analytics": {
        "body": [r"simpleanalytics\.com"],
        "confidence": 92,
        "requires": 1,
    },
    "Umami": {
        "body": [r"umami\.is/script"],
        "confidence": 90,
        "requires": 1,
    },
    "GoatCounter": {
        "body": [r"goatcounter\.com/count", r"gc\.zgo\.at"],
        "confidence": 88,
        "requires": 1,
    },

    # Enterprise
    "Siteimprove": {
        "body": [
            r"siteimprove\.com",
            r"siteimproveanalytics\.com",
            r"siteimprove\.js",
            r"si\.js",
            r"dc\.siteimprove\.com",
        ],
        "confidence": 95,
        "requires": 1,
    },
    "Adobe Analytics": {
        "body": [r"omniture\.com", r"sc\.omtrdc\.net", r"s_code\.js", r"AppMeasurement\.js"],
        "confidence": 92,
        "requires": 1,
    },

    # Meta/Facebook
    "Facebook Pixel": {
        "body": [r"connect\.facebook\.net/.*fbevents\.js", r"fbq\s*\(\s*['\"]init['\"]"],
        "confidence": 95,
        "requires": 1,
    },

    # Session Recording
    "Hotjar": {
        "body": [r"static\.hotjar\.com", r"_hjSettings"],
        "confidence": 95,
        "requires": 1,
    },
    "FullStory": {
        "body": [r"fullstory\.com/s/fs\.js"],
        "confidence": 92,
        "requires": 1,
    },
    "Clarity": {
        "body": [r"clarity\.ms/tag"],
        "confidence": 92,
        "requires": 1,
    },
    "Lucky Orange": {
        "body": [r"luckyorange\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "Smartlook": {
        "body": [r"rec\.smartlook\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "LogRocket": {
        "body": [r"cdn\.logrocket\.io"],
        "confidence": 88,
        "requires": 1,
    },
    "Mouseflow": {
        "body": [r"mouseflow\.com"],
        "confidence": 88,
        "requires": 1,
    },

    # Product Analytics
    "Mixpanel": {
        "body": [r"cdn\.mxpnl\.com", r"mixpanel\.init"],
        "confidence": 95,
        "requires": 1,
    },
    "Amplitude": {
        "body": [r"cdn\.amplitude\.com"],
        "confidence": 92,
        "requires": 1,
    },
    "Segment": {
        "body": [r"cdn\.segment\.com"],
        "confidence": 92,
        "requires": 1,
    },
    "Heap": {
        "body": [r"heapanalytics\.com"],
        "confidence": 92,
        "requires": 1,
    },
    "PostHog": {
        "body": [r"posthog\.com", r"posthog\.init"],
        "confidence": 90,
        "requires": 1,
    },
    "Pendo": {
        "body": [r"pendo\.io", r"cdn\.pendo\.io"],
        "confidence": 90,
        "requires": 1,
    },

    # Chat & Support
    "Intercom": {
        "body": [r"widget\.intercom\.io"],
        "confidence": 92,
        "requires": 1,
    },
    "Drift": {
        "body": [r"js\.driftt\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "Crisp": {
        "body": [r"client\.crisp\.chat"],
        "confidence": 90,
        "requires": 1,
    },
    "Zendesk": {
        "body": [r"zdassets\.com"],
        "confidence": 92,
        "requires": 1,
    },
    "Tawk.to": {
        "body": [r"embed\.tawk\.to"],
        "confidence": 92,
        "requires": 1,
    },
    "HubSpot": {
        "body": [r"js\.hs-scripts\.com"],
        "confidence": 92,
        "requires": 1,
    },
    "Tidio": {
        "body": [r"code\.tidio\.co"],
        "confidence": 90,
        "requires": 1,
    },
    "LiveChat": {
        "body": [r"livechatinc\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "Freshdesk": {
        "body": [r"freshdesk\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Help Scout": {
        "body": [r"beacon-v2\.helpscout\.net"],
        "confidence": 88,
        "requires": 1,
    },
    "Olark": {
        "body": [r"static\.olark\.com"],
        "confidence": 88,
        "requires": 1,
    },

    # Marketing
    "Klaviyo": {
        "body": [r"static\.klaviyo\.com"],
        "confidence": 92,
        "requires": 1,
    },
    "Mailchimp": {
        "body": [r"chimpstatic\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "ConvertKit": {
        "body": [r"convertkit\.com"],
        "confidence": 88,
        "requires": 1,
    },

    # A/B Testing
    "Optimizely": {
        "body": [r"cdn\.optimizely\.com"],
        "confidence": 92,
        "requires": 1,
    },
    "VWO": {
        "body": [r"dev\.visualwebsiteoptimizer\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "Google Optimize": {
        "body": [r"googleoptimize\.com"],
        "confidence": 90,
        "requires": 1,
    },

    # Ads
    "Google Ads": {
        "body": [r"googleads\.g\.doubleclick\.net", r"AW-\d+"],
        "confidence": 92,
        "requires": 1,
    },
    "Google AdSense": {
        "body": [r"pagead2\.googlesyndication\.com/pagead/js/adsbygoogle"],
        "confidence": 92,
        "requires": 1,
    },
    "LinkedIn Insight": {
        "body": [r"snap\.licdn\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "TikTok Pixel": {
        "body": [r"analytics\.tiktok\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "Pinterest Tag": {
        "body": [r"s\.pinimg\.com/ct/core\.js"],
        "confidence": 88,
        "requires": 1,
    },
    "Twitter Ads": {
        "body": [r"static\.ads-twitter\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Bing Ads": {
        "body": [r"bat\.bing\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Criteo": {
        "body": [r"static\.criteo\.net"],
        "confidence": 88,
        "requires": 1,
    },
}
