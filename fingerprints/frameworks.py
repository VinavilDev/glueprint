FRAMEWORKS = {
    # PHP Frameworks
    "Laravel": {
        "cookies": [r"^laravel_session$", r"^XSRF-TOKEN$"],
        "body": [r"laravel\.com/docs"],
        "confidence": 92,
        "requires": 1,
    },
    "Symfony": {
        "cookies": [r"^sf_redirect$"],
        "body": [r"symfony\.com", r"_sf_toolbar"],
        "confidence": 88,
        "requires": 1,
    },
    "CodeIgniter": {
        "cookies": [r"^ci_session$", r"^ci_csrf_token$"],
        "confidence": 88,
        "requires": 1,
    },
    "CakePHP": {
        "cookies": [r"^CAKEPHP$"],
        "confidence": 90,
        "requires": 1,
    },
    "Yii": {
        "cookies": [r"^YII_CSRF_TOKEN$"],
        "body": [r"yiiframework\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Laminas": {
        "body": [r"laminas\.dev", r"getlaminas\.org"],
        "confidence": 80,
        "requires": 1,
    },

    # Python Frameworks
    "Django": {
        "cookies": [r"^csrftoken$", r"^sessionid$"],
        "body": [r'name=["\']csrfmiddlewaretoken["\']', r"/admin/login/", r"django\.contrib"],
        "confidence": 90,
        "requires": 1,
    },
    "Flask": {
        "headers": {"Server": r"^Werkzeug"},
        "body": [r"flask\.pocoo\.org", r"flask\.palletsprojects"],
        "confidence": 78,
        "requires": 1,
    },
    "FastAPI": {
        "headers": {"Server": r"^uvicorn"},
        "body": [r'"openapi":\s*"3\.', r"/docs", r"/redoc"],
        "confidence": 80,
        "requires": 2,
    },
    "Pyramid": {
        "body": [r"pylonsproject\.org", r"pyramid_"],
        "confidence": 75,
        "requires": 1,
    },

    # Ruby Frameworks
    "Ruby on Rails": {
        "headers": {"X-Powered-By": r"Phusion Passenger"},
        "cookies": [r"_session$"],
        "body": [r'name=["\']authenticity_token["\']', r"rails-ujs", r"/assets/application-[a-f0-9]{16,}"],
        "confidence": 85,
        "requires": 1,
    },
    "Sinatra": {
        "headers": {"Server": r"WEBrick"},
        "body": [r"sinatrarb\.com"],
        "confidence": 75,
        "requires": 1,
    },

    # Node.js Frameworks
    "Express.js": {
        "headers": {"X-Powered-By": r"^Express$"},
        "confidence": 95,
        "requires": 1,
    },
    "Next.js": {
        "headers": {"X-Powered-By": r"^Next\.js", "x-nextjs-cache": r".+"},
        "body": [r"/_next/static/", r"__NEXT_DATA__", r"_next/image"],
        "confidence": 92,
        "requires": 1,
    },
    "Nuxt.js": {
        "headers": {"X-Powered-By": r"Nuxt"},
        "body": [r"/_nuxt/", r"__NUXT__", r"nuxt\.config"],
        "confidence": 90,
        "requires": 1,
    },
    "Gatsby": {
        "body": [r"gatsby-image", r"gatsby-focus-wrapper", r"/page-data/"],
        "confidence": 85,
        "requires": 1,
    },
    "Remix": {
        "body": [r"__remix", r"remix-run"],
        "confidence": 85,
        "requires": 1,
    },
    "Astro": {
        "body": [r"astro-island", r"astro\.build"],
        "confidence": 88,
        "requires": 1,
    },
    "SvelteKit": {
        "body": [r"__sveltekit", r"svelte-kit"],
        "confidence": 88,
        "requires": 1,
    },
    "Nest.js": {
        "body": [r"nestjs\.com", r"@nestjs/"],
        "confidence": 78,
        "requires": 1,
    },
    "Koa": {
        "headers": {"X-Powered-By": r"^koa$"},
        "confidence": 85,
        "requires": 1,
    },
    "Hapi": {
        "body": [r"hapi\.dev", r"@hapi/"],
        "confidence": 78,
        "requires": 1,
    },
    "Fastify": {
        "body": [r"fastify\.io", r"fastify/"],
        "confidence": 78,
        "requires": 1,
    },

    # Java Frameworks
    "Spring Boot": {
        "headers": {"X-Application-Context": r".+"},
        "body": [r"Whitelabel Error Page", r"/actuator/"],
        "confidence": 85,
        "requires": 1,
    },
    "Spring MVC": {
        "body": [r"springframework\.org", r"DispatcherServlet"],
        "confidence": 78,
        "requires": 1,
    },

    # .NET Frameworks
    "ASP.NET MVC": {
        "headers": {"X-AspNetMvc-Version": r"[\d.]+"},
        "confidence": 92,
        "requires": 1,
    },
    "Blazor": {
        "body": [r"_framework/blazor", r"blazor\.webassembly"],
        "confidence": 92,
        "requires": 1,
    },

    # CMS - WordPress with strict detection
    "WordPress": {
        "headers": {"Link": r'rel="https://api\.w\.org/"'},
        "body": [
            r"/wp-content/(?:themes|plugins|uploads)/[^\"'\s]+",
            r"/wp-includes/(?:js|css)/[^\"'\s]+",
            r'<meta[^>]+generator[^>]+WordPress',
            r"wp-emoji-release\.min\.js",
            r"/xmlrpc\.php",
            r"/wp-admin/",
            r"wp-json/wp/v2",
        ],
        "confidence": 95,
        "requires": 1,
    },
    "Drupal": {
        "headers": {"X-Drupal-Cache": r".+", "X-Generator": r"Drupal"},
        "body": [r'content="Drupal', r"Drupal\.settings", r"/sites/default/files/"],
        "confidence": 92,
        "requires": 1,
    },
    "Joomla": {
        "body": [r'content="Joomla', r"/media/jui/", r"/components/com_"],
        "confidence": 88,
        "requires": 1,
    },
    "Ghost": {
        "headers": {"X-Powered-By": r"^Ghost"},
        "body": [r"ghost-(?:admin|api)"],
        "confidence": 92,
        "requires": 1,
    },
    "Strapi": {
        "headers": {"X-Powered-By": r"Strapi"},
        "confidence": 90,
        "requires": 1,
    },
    "Webflow": {
        "body": [r"webflow\.com", r"w-webflow", r"wf-page"],
        "confidence": 92,
        "requires": 1,
    },
    "Wix": {
        "body": [r"wix\.com", r"wixstatic\.com"],
        "confidence": 92,
        "requires": 1,
    },
    "Squarespace": {
        "body": [r"squarespace\.com", r"sqsp\.net"],
        "confidence": 92,
        "requires": 1,
    },
    "TYPO3": {
        "body": [r"typo3temp/", r"typo3conf/", r'content="TYPO3'],
        "confidence": 90,
        "requires": 1,
    },
    "Contao": {
        "body": [r"contao\.org", r"bundles/contao"],
        "confidence": 85,
        "requires": 1,
    },
    "Craft CMS": {
        "body": [r"craftcms\.com", r"Craft\."],
        "confidence": 85,
        "requires": 1,
    },
    "October CMS": {
        "body": [r"octobercms\.com", r"/themes/"],
        "cookies": [r"^october_session$"],
        "confidence": 82,
        "requires": 1,
    },

    # E-commerce
    "Shopify": {
        "headers": {"X-ShopId": r"\d+"},
        "body": [r"cdn\.shopify\.com", r"Shopify\.theme"],
        "confidence": 95,
        "requires": 1,
    },
    "WooCommerce": {
        "body": [r"woocommerce", r"wc-block-", r"/cart/\?add-to-cart"],
        "confidence": 85,
        "requires": 2,
    },
    "Magento": {
        "body": [r"Mage\.Cookies", r"mage/requirejs", r"/static/version"],
        "confidence": 88,
        "requires": 1,
    },
    "PrestaShop": {
        "body": [r"PrestaShop", r"prestashop"],
        "cookies": [r"^PrestaShop-"],
        "confidence": 88,
        "requires": 1,
    },
    "BigCommerce": {
        "body": [r"bigcommerce\.com", r"BCData"],
        "confidence": 88,
        "requires": 1,
    },
    "OpenCart": {
        "body": [r"catalog/view/theme", r"route=common"],
        "confidence": 82,
        "requires": 1,
    },
}
