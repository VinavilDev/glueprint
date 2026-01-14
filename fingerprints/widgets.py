WIDGETS = {
    # Accessibility
    "ReadSpeaker": {
        "body": [
            r"readspeaker\.com",
            r"ReadSpeaker",
            r"rspkr\.",
            r"rscdn\.com",
            r"ReadSpeaker\.init",
        ],
        "confidence": 95,
        "requires": 1,
    },
    "UserWay": {
        "body": [r"userway\.org", r"UserWay"],
        "confidence": 90,
        "requires": 1,
    },
    "accessiBe": {
        "body": [r"accessibe\.com", r"acsbapp\.com"],
        "confidence": 90,
        "requires": 1,
    },

    # Music
    "Spotify Embed": {
        "body": [r"open\.spotify\.com/embed", r"spotify:(?:track|album|playlist):"],
        "confidence": 95,
        "requires": 1,
    },
    "SoundCloud Embed": {
        "body": [r"w\.soundcloud\.com/player", r"api\.soundcloud\.com"],
        "confidence": 95,
        "requires": 1,
    },
    "Apple Music Embed": {
        "body": [r"embed\.music\.apple\.com"],
        "confidence": 95,
        "requires": 1,
    },
    "Tidal Embed": {
        "body": [r"embed\.tidal\.com"],
        "confidence": 95,
        "requires": 1,
    },
    "Deezer Embed": {
        "body": [r"widget\.deezer\.com"],
        "confidence": 95,
        "requires": 1,
    },
    "Bandcamp Embed": {
        "body": [r"bandcamp\.com/EmbeddedPlayer"],
        "confidence": 95,
        "requires": 1,
    },
    "Mixcloud Embed": {
        "body": [r"mixcloud\.com/widget"],
        "confidence": 92,
        "requires": 1,
    },

    # Video
    "YouTube Embed": {
        "body": [r"youtube\.com/embed", r"youtube-nocookie\.com/embed"],
        "confidence": 95,
        "requires": 1,
    },
    "Vimeo Embed": {
        "body": [r"player\.vimeo\.com"],
        "confidence": 95,
        "requires": 1,
    },
    "Dailymotion Embed": {
        "body": [r"dailymotion\.com/embed"],
        "confidence": 92,
        "requires": 1,
    },
    "Twitch Embed": {
        "body": [r"player\.twitch\.tv"],
        "confidence": 95,
        "requires": 1,
    },
    "Wistia": {
        "body": [r"fast\.wistia\.com"],
        "confidence": 92,
        "requires": 1,
    },
    "TikTok Embed": {
        "body": [r"tiktok\.com/embed"],
        "confidence": 95,
        "requires": 1,
    },
    "Instagram Embed": {
        "body": [r"instagram\.com/embed"],
        "confidence": 95,
        "requires": 1,
    },
    "Twitter/X Embed": {
        "body": [r"platform\.twitter\.com/widgets", r"twitter-tweet"],
        "confidence": 95,
        "requires": 1,
    },

    # Maps
    "Google Maps Embed": {
        "body": [r"google\.com/maps/embed"],
        "confidence": 95,
        "requires": 1,
    },
    "OpenStreetMap Embed": {
        "body": [r"openstreetmap\.org/export/embed"],
        "confidence": 90,
        "requires": 1,
    },

    # Social
    "Facebook Like": {
        "body": [r"facebook\.com/plugins/like"],
        "confidence": 92,
        "requires": 1,
    },
    "Disqus": {
        "body": [r"disqus\.com/embed", r"disqus_thread"],
        "confidence": 95,
        "requires": 1,
    },

    # Scheduling
    "Calendly": {
        "body": [r"calendly\.com/"],
        "confidence": 92,
        "requires": 1,
    },
    "Typeform": {
        "body": [r"typeform\.com"],
        "confidence": 92,
        "requires": 1,
    },
    "Google Forms": {
        "body": [r"docs\.google\.com/forms/"],
        "confidence": 95,
        "requires": 1,
    },

    # Code
    "CodePen Embed": {
        "body": [r"codepen\.io/"],
        "confidence": 92,
        "requires": 1,
    },
    "GitHub Gist": {
        "body": [r"gist\.github\.com"],
        "confidence": 92,
        "requires": 1,
    },

    # Design
    "Figma Embed": {
        "body": [r"figma\.com/embed"],
        "confidence": 92,
        "requires": 1,
    },
    "Canva Embed": {
        "body": [r"canva\.com/design"],
        "confidence": 88,
        "requires": 1,
    },
}
