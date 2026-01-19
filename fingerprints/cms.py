CMS = {
    # Blogging
    "Ghost": {
        "body": [r"ghost\.org", r"ghost-admin", r"content/themes"],
        "headers": {"X-Ghost-Cache-Status": r".+"},
        "confidence": 90,
        "requires": 1,
    },
    "Medium": {
        "body": [r"medium\.com", r"medium-com"],
        "confidence": 85,
        "requires": 1,
    },
    "Substack": {
        "body": [r"substack\.com", r"substackcdn\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "Blogger": {
        "body": [r"blogger\.com", r"blogspot\.com", r"blogger\.googleusercontent"],
        "confidence": 92,
        "requires": 1,
    },
    "Tumblr": {
        "body": [r"tumblr\.com", r"tumblr-feed"],
        "confidence": 90,
        "requires": 1,
    },
    "Hashnode": {
        "body": [r"hashnode\.com", r"hashnode\.dev"],
        "confidence": 85,
        "requires": 1,
    },
    "Dev.to": {
        "body": [r"dev\.to"],
        "confidence": 82,
        "requires": 1,
    },

    # Enterprise CMS
    "Contentful": {
        "body": [r"contentful\.com", r"ctfassets\.net", r"contentful"],
        "confidence": 88,
        "requires": 1,
    },
    "Sanity": {
        "body": [r"sanity\.io", r"sanitycdn\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Strapi": {
        "body": [r"strapi\.io", r"/api/strapi"],
        "confidence": 82,
        "requires": 1,
    },
    "Prismic": {
        "body": [r"prismic\.io", r"prismic-dom"],
        "confidence": 85,
        "requires": 1,
    },
    "Storyblok": {
        "body": [r"storyblok\.com", r"a\.storyblok\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "DatoCMS": {
        "body": [r"datocms\.com", r"datocms-assets"],
        "confidence": 82,
        "requires": 1,
    },
    "Directus": {
        "body": [r"directus\.io", r"/admin/directus"],
        "confidence": 80,
        "requires": 1,
    },
    "Payload CMS": {
        "body": [r"payloadcms\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "KeystoneJS": {
        "body": [r"keystonejs\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Craft CMS": {
        "body": [r"craftcms\.com", r"/cpresources/"],
        "cookies": [r"^CraftSessionId$"],
        "confidence": 88,
        "requires": 1,
    },
    "Statamic": {
        "body": [r"statamic\.com", r"statamic"],
        "confidence": 82,
        "requires": 1,
    },
    "Kirby": {
        "body": [r"getkirby\.com", r"kirby"],
        "confidence": 78,
        "requires": 1,
    },
    "ProcessWire": {
        "body": [r"processwire\.com"],
        "confidence": 75,
        "requires": 1,
    },
    "Grav": {
        "body": [r"getgrav\.org", r"grav-admin"],
        "confidence": 78,
        "requires": 1,
    },
    "October CMS": {
        "body": [r"octobercms\.com", r"october"],
        "confidence": 78,
        "requires": 1,
    },
    "Concrete5": {
        "body": [r"concrete5\.org", r"concrete/js"],
        "confidence": 80,
        "requires": 1,
    },
    "TYPO3": {
        "body": [r"typo3", r"TYPO3"],
        "headers": {"X-TYPO3-Parsetime": r".+"},
        "confidence": 88,
        "requires": 1,
    },
    "Joomla": {
        "body": [r"/media/jui/", r"Joomla!", r"/templates/", r"com_content"],
        "headers": {"X-Content-Encoded-By": r"Joomla"},
        "confidence": 88,
        "requires": 1,
    },
    "Drupal": {
        "body": [r"Drupal", r"/sites/default/files", r"drupal\.org"],
        "headers": {"X-Drupal-Cache": r".+", "X-Generator": r"Drupal"},
        "confidence": 90,
        "requires": 1,
    },
    "SilverStripe": {
        "body": [r"silverstripe", r"SilverStripe"],
        "headers": {"X-SilverStripe-Cache": r".+"},
        "confidence": 85,
        "requires": 1,
    },
    "Umbraco": {
        "body": [r"umbraco", r"Umbraco"],
        "confidence": 85,
        "requires": 1,
    },
    "Sitecore": {
        "body": [r"sitecore", r"Sitecore"],
        "cookies": [r"^SC_ANALYTICS"],
        "confidence": 88,
        "requires": 1,
    },
    "Kentico": {
        "body": [r"kentico", r"Kentico"],
        "confidence": 82,
        "requires": 1,
    },
    "Episerver": {
        "body": [r"episerver", r"EPiServer"],
        "confidence": 82,
        "requires": 1,
    },
    "Adobe Experience Manager": {
        "body": [r"/content/dam/", r"cq\.wcm", r"/etc/clientlibs"],
        "confidence": 88,
        "requires": 1,
    },
    "Sitefinity": {
        "body": [r"sitefinity", r"Telerik\.Sitefinity"],
        "confidence": 82,
        "requires": 1,
    },
    "DNN": {
        "body": [r"DotNetNuke", r"/Portals/", r"dnn\."],
        "confidence": 85,
        "requires": 1,
    },
    "Orchard": {
        "body": [r"orchardcore", r"orchardproject"],
        "confidence": 78,
        "requires": 1,
    },
    "Piranha CMS": {
        "body": [r"piranhacms"],
        "confidence": 75,
        "requires": 1,
    },
    "Agility CMS": {
        "body": [r"agilitycms\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "ButterCMS": {
        "body": [r"buttercms\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Cosmic": {
        "body": [r"cosmicjs\.com"],
        "confidence": 75,
        "requires": 1,
    },
    "GraphCMS": {
        "body": [r"graphcms\.com", r"hygraph\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "Kontent.ai": {
        "body": [r"kontent\.ai", r"kenticocloud"],
        "confidence": 80,
        "requires": 1,
    },
    "Netlify CMS": {
        "body": [r"netlify-cms", r"netlify-identity"],
        "confidence": 82,
        "requires": 1,
    },
    "Forestry": {
        "body": [r"forestry\.io"],
        "confidence": 75,
        "requires": 1,
    },
    "TinaCMS": {
        "body": [r"tina\.io", r"tinacms"],
        "confidence": 75,
        "requires": 1,
    },
    "Decap CMS": {
        "body": [r"decapcms\.org"],
        "confidence": 72,
        "requires": 1,
    },

    # Wiki
    "MediaWiki": {
        "body": [r"mediawiki", r"MediaWiki", r"/wiki/"],
        "headers": {"X-Powered-By": r"MediaWiki"},
        "confidence": 92,
        "requires": 1,
    },
    "Confluence": {
        "body": [r"confluence", r"Atlassian Confluence"],
        "confidence": 88,
        "requires": 1,
    },
    "DokuWiki": {
        "body": [r"dokuwiki", r"DokuWiki"],
        "confidence": 85,
        "requires": 1,
    },
    "TiddlyWiki": {
        "body": [r"tiddlywiki", r"TiddlyWiki"],
        "confidence": 82,
        "requires": 1,
    },
    "BookStack": {
        "body": [r"bookstack"],
        "confidence": 78,
        "requires": 1,
    },
    "Wiki.js": {
        "body": [r"wiki\.js", r"wikijs"],
        "confidence": 80,
        "requires": 1,
    },
    "Notion": {
        "body": [r"notion\.so", r"notion-static"],
        "confidence": 88,
        "requires": 1,
    },
    "Gitbook": {
        "body": [r"gitbook\.com", r"gitbook\.io"],
        "confidence": 85,
        "requires": 1,
    },
    "ReadTheDocs": {
        "body": [r"readthedocs\.org", r"readthedocs\.io"],
        "confidence": 88,
        "requires": 1,
    },
    "Docusaurus": {
        "body": [r"docusaurus", r"Docusaurus"],
        "confidence": 85,
        "requires": 1,
    },
    "MkDocs": {
        "body": [r"mkdocs", r"MkDocs"],
        "confidence": 82,
        "requires": 1,
    },
    "Sphinx": {
        "body": [r"sphinx-doc", r"sphinxdoc"],
        "confidence": 80,
        "requires": 1,
    },
    "VuePress": {
        "body": [r"vuepress", r"VuePress"],
        "confidence": 82,
        "requires": 1,
    },
    "Docsify": {
        "body": [r"docsify", r"docsify\.js"],
        "confidence": 80,
        "requires": 1,
    },
    "Nextra": {
        "body": [r"nextra", r"nextra-theme"],
        "confidence": 78,
        "requires": 1,
    },
    "Mintlify": {
        "body": [r"mintlify\.com"],
        "confidence": 78,
        "requires": 1,
    },

    # Site Builders
    "Wix": {
        "body": [r"wix\.com", r"wixstatic\.com", r"_wix"],
        "confidence": 95,
        "requires": 1,
    },
    "Squarespace": {
        "body": [r"squarespace\.com", r"squarespace-cdn", r"sqsp"],
        "confidence": 95,
        "requires": 1,
    },
    "Webflow": {
        "body": [r"webflow\.com", r"webflow\.io", r"wf-"],
        "confidence": 95,
        "requires": 1,
    },
    "Weebly": {
        "body": [r"weebly\.com", r"weeblycloud"],
        "confidence": 90,
        "requires": 1,
    },
    "Jimdo": {
        "body": [r"jimdo\.com", r"jimstatic\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Duda": {
        "body": [r"duda\.co", r"dudaone\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "GoDaddy Website Builder": {
        "body": [r"godaddy\.com", r"godaddy-"],
        "confidence": 82,
        "requires": 1,
    },
    "Strikingly": {
        "body": [r"strikingly\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Carrd": {
        "body": [r"carrd\.co"],
        "confidence": 85,
        "requires": 1,
    },
    "Leadpages": {
        "body": [r"leadpages\.net", r"leadpages\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Unbounce": {
        "body": [r"unbounce\.com", r"ubembed\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Instapage": {
        "body": [r"instapage\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "ClickFunnels": {
        "body": [r"clickfunnels\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Kajabi": {
        "body": [r"kajabi\.com", r"kajabi-"],
        "confidence": 85,
        "requires": 1,
    },
    "Teachable": {
        "body": [r"teachable\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Thinkific": {
        "body": [r"thinkific\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Podia": {
        "body": [r"podia\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Mighty Networks": {
        "body": [r"mightynetworks\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "Circle.so": {
        "body": [r"circle\.so"],
        "confidence": 80,
        "requires": 1,
    },
    "Memberful": {
        "body": [r"memberful\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Patreon": {
        "body": [r"patreon\.com", r"patreonusercontent"],
        "confidence": 90,
        "requires": 1,
    },
    "Ko-fi": {
        "body": [r"ko-fi\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Buy Me a Coffee": {
        "body": [r"buymeacoffee\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Linktree": {
        "body": [r"linktr\.ee"],
        "confidence": 90,
        "requires": 1,
    },
    "Beacons": {
        "body": [r"beacons\.ai"],
        "confidence": 82,
        "requires": 1,
    },
    "Stan Store": {
        "body": [r"stan\.store"],
        "confidence": 80,
        "requires": 1,
    },
    "Gumroad": {
        "body": [r"gumroad\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Lemon Squeezy": {
        "body": [r"lemonsqueezy\.com"],
        "confidence": 82,
        "requires": 1,
    },
}
