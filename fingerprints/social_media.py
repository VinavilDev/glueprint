SOCIAL_MEDIA = {
    # Social Networks
    "Facebook SDK": {
        "body": [r"connect\.facebook\.net", r"facebook-jssdk", r"fb-root"],
        "confidence": 95,
        "requires": 1,
    },
    "Facebook Pixel": {
        "body": [r"facebook\.com/tr", r"fbevents\.js", r"fbq\s*\("],
        "confidence": 95,
        "requires": 1,
    },
    "Instagram Embed": {
        "body": [r"instagram\.com/embed", r"instgrm\.Embeds"],
        "confidence": 90,
        "requires": 1,
    },
    "Twitter SDK": {
        "body": [r"platform\.twitter\.com", r"twitter-wjs"],
        "confidence": 92,
        "requires": 1,
    },
    "Twitter Pixel": {
        "body": [r"static\.ads-twitter\.com", r"twq\s*\("],
        "confidence": 90,
        "requires": 1,
    },
    "LinkedIn Insight": {
        "body": [r"snap\.licdn\.com", r"linkedin\.com/px"],
        "confidence": 90,
        "requires": 1,
    },
    "LinkedIn Share": {
        "body": [r"platform\.linkedin\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Pinterest Tag": {
        "body": [r"pintrk\s*\(", r"s\.pinimg\.com/ct/core"],
        "confidence": 88,
        "requires": 1,
    },
    "Pinterest Widget": {
        "body": [r"assets\.pinterest\.com", r"pinit\.js"],
        "confidence": 88,
        "requires": 1,
    },
    "TikTok Pixel": {
        "body": [r"analytics\.tiktok\.com", r"ttq\s*\("],
        "confidence": 90,
        "requires": 1,
    },
    "TikTok Embed": {
        "body": [r"tiktok\.com/embed"],
        "confidence": 90,
        "requires": 1,
    },
    "Snapchat Pixel": {
        "body": [r"sc-static\.net/scevent\.min\.js", r"snaptr\s*\("],
        "confidence": 88,
        "requires": 1,
    },
    "Reddit Pixel": {
        "body": [r"rdt\s*\(", r"reddit\.com/static/ads"],
        "confidence": 85,
        "requires": 1,
    },
    "Reddit Embed": {
        "body": [r"embed\.redditmedia\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "WhatsApp Chat": {
        "body": [r"wa\.me", r"api\.whatsapp\.com", r"whatsapp-widget"],
        "confidence": 88,
        "requires": 1,
    },
    "Telegram Widget": {
        "body": [r"telegram\.org/js/telegram-widget", r"t\.me"],
        "confidence": 85,
        "requires": 1,
    },
    "Discord Widget": {
        "body": [r"discord\.com/widget", r"discordapp\.com/widget"],
        "confidence": 85,
        "requires": 1,
    },
    "Slack Share": {
        "body": [r"slack\.com/share"],
        "confidence": 78,
        "requires": 1,
    },
    "Mastodon": {
        "body": [r"mastodon", r"joinmastodon\.org"],
        "confidence": 78,
        "requires": 1,
    },
    "Bluesky": {
        "body": [r"bsky\.app", r"bluesky"],
        "confidence": 78,
        "requires": 1,
    },
    "Threads": {
        "body": [r"threads\.net"],
        "confidence": 80,
        "requires": 1,
    },

    # Share Buttons
    "AddThis": {
        "body": [r"addthis\.com", r"addthis_widget"],
        "confidence": 90,
        "requires": 1,
    },
    "AddToAny": {
        "body": [r"addtoany\.com", r"a2a_config"],
        "confidence": 88,
        "requires": 1,
    },
    "ShareThis": {
        "body": [r"sharethis\.com", r"st_insights_js"],
        "confidence": 88,
        "requires": 1,
    },
    "Shareaholic": {
        "body": [r"shareaholic\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "SumoMe Share": {
        "body": [r"sumo\.com.*share"],
        "confidence": 82,
        "requires": 1,
    },
    "Social Warfare": {
        "body": [r"socialwarfare"],
        "confidence": 78,
        "requires": 1,
    },

    # Video Platforms
    "YouTube API": {
        "body": [r"www\.youtube\.com/iframe_api", r"YT\.Player"],
        "confidence": 92,
        "requires": 1,
    },
    "Vimeo Player": {
        "body": [r"player\.vimeo\.com", r"vimeo\.com/api"],
        "confidence": 92,
        "requires": 1,
    },
    "Dailymotion": {
        "body": [r"dailymotion\.com", r"dmcdn\.net"],
        "confidence": 88,
        "requires": 1,
    },
    "Twitch": {
        "body": [r"player\.twitch\.tv", r"embed\.twitch\.tv"],
        "confidence": 90,
        "requires": 1,
    },
    "Wistia": {
        "body": [r"wistia\.com", r"fast\.wistia\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "Vidyard": {
        "body": [r"vidyard\.com", r"play\.vidyard\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Brightcove": {
        "body": [r"brightcove\.com", r"players\.brightcove\.net"],
        "confidence": 88,
        "requires": 1,
    },
    "JW Player": {
        "body": [r"jwplayer\.com", r"cdn\.jwplayer\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "Kaltura": {
        "body": [r"kaltura\.com", r"cdnapi\.kaltura\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Panopto": {
        "body": [r"panopto\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "SproutVideo": {
        "body": [r"sproutvideo\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Loom": {
        "body": [r"loom\.com", r"cdn\.loom\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Cloudflare Stream": {
        "body": [r"stream\.cloudflarestream\.com", r"videodelivery\.net"],
        "confidence": 85,
        "requires": 1,
    },
    "Bunny Stream": {
        "body": [r"iframe\.mediadelivery\.net"],
        "confidence": 82,
        "requires": 1,
    },

    # Audio/Podcast
    "Spotify Embed": {
        "body": [r"open\.spotify\.com/embed"],
        "confidence": 92,
        "requires": 1,
    },
    "Apple Podcasts": {
        "body": [r"embed\.podcasts\.apple\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "SoundCloud": {
        "body": [r"soundcloud\.com", r"w\.soundcloud\.com"],
        "confidence": 92,
        "requires": 1,
    },
    "Audiomack": {
        "body": [r"audiomack\.com/embed"],
        "confidence": 82,
        "requires": 1,
    },
    "Mixcloud": {
        "body": [r"mixcloud\.com/widget"],
        "confidence": 85,
        "requires": 1,
    },
    "Podbean": {
        "body": [r"podbean\.com/player"],
        "confidence": 82,
        "requires": 1,
    },
    "Buzzsprout": {
        "body": [r"buzzsprout\.com/player"],
        "confidence": 82,
        "requires": 1,
    },
    "Transistor": {
        "body": [r"transistor\.fm/embed"],
        "confidence": 80,
        "requires": 1,
    },
    "Anchor": {
        "body": [r"anchor\.fm/.*embed"],
        "confidence": 85,
        "requires": 1,
    },
    "Simplecast": {
        "body": [r"player\.simplecast\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Captivate": {
        "body": [r"player\.captivate\.fm"],
        "confidence": 78,
        "requires": 1,
    },
    "Megaphone": {
        "body": [r"megaphone\.fm/embed"],
        "confidence": 78,
        "requires": 1,
    },
    "Spreaker": {
        "body": [r"widget\.spreaker\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "Libsyn": {
        "body": [r"play\.libsyn\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "Stitcher": {
        "body": [r"stitcher\.com/embed"],
        "confidence": 78,
        "requires": 1,
    },

    # News & Content
    "Medium Embed": {
        "body": [r"medium\.com/media"],
        "confidence": 82,
        "requires": 1,
    },
    "Substack Embed": {
        "body": [r"substackcdn\.com/embed"],
        "confidence": 82,
        "requires": 1,
    },
    "Issuu": {
        "body": [r"issuu\.com/embed", r"e\.issuu\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Scribd": {
        "body": [r"scribd\.com/embeds"],
        "confidence": 82,
        "requires": 1,
    },
    "SlideShare": {
        "body": [r"slideshare\.net/slideshow/embed"],
        "confidence": 85,
        "requires": 1,
    },
    "Prezi": {
        "body": [r"prezi\.com/embed"],
        "confidence": 82,
        "requires": 1,
    },
    "Canva Embed": {
        "body": [r"canva\.com/design.*embed"],
        "confidence": 82,
        "requires": 1,
    },
    "Ceros": {
        "body": [r"view\.ceros\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Flourish": {
        "body": [r"flourish\.studio/embed"],
        "confidence": 80,
        "requires": 1,
    },
    "Datawrapper": {
        "body": [r"datawrapper\.dwcdn\.net"],
        "confidence": 82,
        "requires": 1,
    },
    "Infogram": {
        "body": [r"infogram\.com/js/embed", r"e\.infogram\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Tableau Public": {
        "body": [r"public\.tableau\.com/views"],
        "confidence": 85,
        "requires": 1,
    },
    "Power BI": {
        "body": [r"app\.powerbi\.com/view"],
        "confidence": 85,
        "requires": 1,
    },

    # Maps
    "Google Maps": {
        "body": [r"maps\.googleapis\.com", r"google\.com/maps"],
        "confidence": 95,
        "requires": 1,
    },
    "Mapbox": {
        "body": [r"api\.mapbox\.com", r"mapbox\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "OpenStreetMap": {
        "body": [r"openstreetmap\.org", r"tile\.openstreetmap"],
        "confidence": 88,
        "requires": 1,
    },
    "Leaflet": {
        "body": [r"leafletjs\.com", r"leaflet\.js"],
        "confidence": 88,
        "requires": 1,
    },
    "HERE Maps": {
        "body": [r"js\.api\.here\.com", r"here\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Bing Maps": {
        "body": [r"bing\.com/api/maps", r"virtualearth\.net"],
        "confidence": 85,
        "requires": 1,
    },
    "TomTom": {
        "body": [r"api\.tomtom\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Apple Maps": {
        "body": [r"cdn\.apple-mapkit\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Carto": {
        "body": [r"carto\.com", r"cartodb\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "ArcGIS": {
        "body": [r"arcgis\.com", r"js\.arcgis\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "MapTiler": {
        "body": [r"maptiler\.com", r"api\.maptiler\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "Snazzy Maps": {
        "body": [r"snazzymaps\.com"],
        "confidence": 72,
        "requires": 1,
    },
    "What3words": {
        "body": [r"what3words\.com", r"w3w\.co"],
        "confidence": 78,
        "requires": 1,
    },
}
