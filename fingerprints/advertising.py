ADVERTISING = {
    # Ad Networks
    "Google Ads": {
        "body": [r"googleads\.g\.doubleclick\.net", r"pagead2\.googlesyndication\.com", r"adservice\.google"],
        "confidence": 95,
        "requires": 1,
    },
    "Google AdSense": {
        "body": [r"googlesyndication\.com", r"adsbygoogle"],
        "confidence": 95,
        "requires": 1,
    },
    "Google Ad Manager": {
        "body": [r"securepubads\.g\.doubleclick\.net", r"googletag\.cmd"],
        "confidence": 92,
        "requires": 1,
    },
    "Facebook Ads": {
        "body": [r"facebook\.com/tr", r"fbevents\.js"],
        "confidence": 92,
        "requires": 1,
    },
    "Microsoft Advertising": {
        "body": [r"bat\.bing\.com", r"clarity\.ms"],
        "confidence": 88,
        "requires": 1,
    },
    "Amazon Ads": {
        "body": [r"amazon-adsystem\.com", r"assoc-amazon\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Yahoo Ads": {
        "body": [r"ads\.yahoo\.com", r"gemini\.yahoo\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Taboola": {
        "body": [r"taboola\.com", r"cdn\.taboola\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "Outbrain": {
        "body": [r"outbrain\.com", r"widgets\.outbrain\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "RevContent": {
        "body": [r"revcontent\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "MGID": {
        "body": [r"mgid\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Content.ad": {
        "body": [r"content\.ad"],
        "confidence": 82,
        "requires": 1,
    },
    "Criteo": {
        "body": [r"criteo\.com", r"static\.criteo\.net"],
        "confidence": 90,
        "requires": 1,
    },
    "AdRoll": {
        "body": [r"adroll\.com", r"d\.adroll\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "MediaMath": {
        "body": [r"mediamath\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "The Trade Desk": {
        "body": [r"thetradedesk\.com", r"adsrvr\.org"],
        "confidence": 85,
        "requires": 1,
    },
    "AppNexus": {
        "body": [r"appnexus\.com", r"adnxs\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "PubMatic": {
        "body": [r"pubmatic\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Rubicon Project": {
        "body": [r"rubiconproject\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "OpenX": {
        "body": [r"openx\.net"],
        "confidence": 82,
        "requires": 1,
    },
    "Index Exchange": {
        "body": [r"indexexchange\.com", r"casalemedia\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "Sovrn": {
        "body": [r"sovrn\.com", r"lijit\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "GumGum": {
        "body": [r"gumgum\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Media.net": {
        "body": [r"media\.net", r"contextual\.media\.net"],
        "confidence": 85,
        "requires": 1,
    },
    "Infolinks": {
        "body": [r"infolinks\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "PropellerAds": {
        "body": [r"propellerads\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "Adsterra": {
        "body": [r"adsterra\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "PopAds": {
        "body": [r"popads\.net"],
        "confidence": 75,
        "requires": 1,
    },
    "Ezoic": {
        "body": [r"ezoic\.net", r"ezojs\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Mediavine": {
        "body": [r"mediavine\.com", r"scripts\.mediavine\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "AdThrive": {
        "body": [r"adthrive\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Monumetric": {
        "body": [r"monumetric\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "SHE Media": {
        "body": [r"blogherads\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Carbon Ads": {
        "body": [r"carbonads\.com", r"srv\.carbonads\.net"],
        "confidence": 85,
        "requires": 1,
    },
    "BuySellAds": {
        "body": [r"buysellads\.com", r"cdn\.buysellads\.net"],
        "confidence": 82,
        "requires": 1,
    },
    "EthicalAds": {
        "body": [r"ethicalads\.io"],
        "confidence": 78,
        "requires": 1,
    },
    "Codefund": {
        "body": [r"codefund\.io"],
        "confidence": 72,
        "requires": 1,
    },

    # Affiliate Networks
    "Amazon Associates": {
        "body": [r"amazon\.com/.*tag=", r"amzn\.to", r"amazon-adsystem"],
        "confidence": 88,
        "requires": 1,
    },
    "ShareASale": {
        "body": [r"shareasale\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "CJ Affiliate": {
        "body": [r"cj\.com", r"commission-junction"],
        "confidence": 82,
        "requires": 1,
    },
    "Rakuten Advertising": {
        "body": [r"rakuten.*advertising", r"linksynergy\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "Impact": {
        "body": [r"impact\.com", r"impactradius\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Partnerize": {
        "body": [r"partnerize\.com", r"prf\.hn"],
        "confidence": 78,
        "requires": 1,
    },
    "Awin": {
        "body": [r"awin\.com", r"awin1\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "FlexOffers": {
        "body": [r"flexoffers\.com"],
        "confidence": 75,
        "requires": 1,
    },
    "Skimlinks": {
        "body": [r"skimlinks\.com", r"skimresources\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "VigLink": {
        "body": [r"viglink\.com", r"sovrn\.com/viglink"],
        "confidence": 82,
        "requires": 1,
    },
    "Refersion": {
        "body": [r"refersion\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Post Affiliate Pro": {
        "body": [r"postaffiliatepro\.com"],
        "confidence": 75,
        "requires": 1,
    },
    "Tapfiliate": {
        "body": [r"tapfiliate\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "FirstPromoter": {
        "body": [r"firstpromoter\.com"],
        "confidence": 75,
        "requires": 1,
    },
    "Rewardful": {
        "body": [r"rewardful\.com"],
        "confidence": 75,
        "requires": 1,
    },
    "PartnerStack": {
        "body": [r"partnerstack\.com"],
        "confidence": 78,
        "requires": 1,
    },

    # Retargeting
    "AdRoll Retargeting": {
        "body": [r"adroll\.com/pixel"],
        "confidence": 85,
        "requires": 1,
    },
    "Perfect Audience": {
        "body": [r"perfectaudience\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "ReTargeter": {
        "body": [r"retargeter\.com"],
        "confidence": 75,
        "requires": 1,
    },
    "SiteScout": {
        "body": [r"sitescout\.com"],
        "confidence": 72,
        "requires": 1,
    },
}

TAG_MANAGERS = {
    "Google Tag Manager": {
        "body": [r"googletagmanager\.com/gtm\.js", r"GTM-[A-Z0-9]+"],
        "confidence": 95,
        "requires": 1,
    },
    "Google Analytics 4": {
        "body": [r"gtag/js\?id=G-", r"G-[A-Z0-9]+"],
        "confidence": 95,
        "requires": 1,
    },
    "Universal Analytics": {
        "body": [r"google-analytics\.com/analytics\.js", r"UA-\d+-\d+"],
        "confidence": 95,
        "requires": 1,
    },
    "Adobe Launch": {
        "body": [r"assets\.adobedtm\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Adobe Analytics": {
        "body": [r"omniture\.com", r"2o7\.net", r"sc\.omtrdc\.net"],
        "confidence": 88,
        "requires": 1,
    },
    "Tealium": {
        "body": [r"tealium\.com", r"tags\.tiqcdn\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Segment": {
        "body": [r"segment\.com", r"cdn\.segment\.com", r"analytics\.js"],
        "confidence": 90,
        "requires": 1,
    },
    "mParticle": {
        "body": [r"mparticle\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Ensighten": {
        "body": [r"ensighten\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Signal": {
        "body": [r"signal\.co", r"thebrighttag\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Commanders Act": {
        "body": [r"commandersact\.com", r"tagcommander\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "Piwik PRO Tag Manager": {
        "body": [r"piwik\.pro.*tag"],
        "confidence": 78,
        "requires": 1,
    },
    "Matomo Tag Manager": {
        "body": [r"matomo\..*tag"],
        "confidence": 78,
        "requires": 1,
    },

    # Consent Management
    "CookieBot": {
        "body": [r"cookiebot\.com", r"Cookiebot"],
        "confidence": 92,
        "requires": 1,
    },
    "OneTrust": {
        "body": [r"onetrust\.com", r"optanon", r"cookiepro\.com"],
        "confidence": 92,
        "requires": 1,
    },
    "TrustArc": {
        "body": [r"trustarc\.com", r"consent\.trustarc\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Quantcast Choice": {
        "body": [r"quantcast\.com.*choice"],
        "confidence": 85,
        "requires": 1,
    },
    "Didomi": {
        "body": [r"didomi\.io", r"sdk\.privacy-center\.org"],
        "confidence": 88,
        "requires": 1,
    },
    "Usercentrics": {
        "body": [r"usercentrics\.eu", r"usercentrics\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Osano": {
        "body": [r"osano\.com", r"cmp\.osano\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Sourcepoint": {
        "body": [r"sourcepoint\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "CookieYes": {
        "body": [r"cookieyes\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Cookie Script": {
        "body": [r"cookie-script\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "GDPR Cookie Consent": {
        "body": [r"gdpr-cookie-consent"],
        "confidence": 78,
        "requires": 1,
    },
    "Cookie Notice": {
        "body": [r"cookie-notice"],
        "confidence": 75,
        "requires": 1,
    },
    "Termly": {
        "body": [r"termly\.io", r"app\.termly\.io"],
        "confidence": 82,
        "requires": 1,
    },
    "iubenda": {
        "body": [r"iubenda\.com", r"cdn\.iubenda\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Civic Cookie Control": {
        "body": [r"civicuk\.com.*cookie"],
        "confidence": 78,
        "requires": 1,
    },
    "Cookie Information": {
        "body": [r"cookieinformation\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Consent Manager": {
        "body": [r"consentmanager\.net"],
        "confidence": 80,
        "requires": 1,
    },
    "LiveRamp": {
        "body": [r"liveramp\.com", r"rlcdn\.com"],
        "confidence": 82,
        "requires": 1,
    },
}
