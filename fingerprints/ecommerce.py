ECOMMERCE = {
    "Shopify": {
        "headers": {"X-ShopId": r"\d+"},
        "body": [r"cdn\.shopify\.com", r"Shopify\.theme", r"myshopify\.com"],
        "confidence": 95,
        "requires": 1,
    },
    "WooCommerce": {
        "body": [r"woocommerce", r"wc-block-", r"/cart/\?add-to-cart", r"wc-add-to-cart"],
        "confidence": 90,
        "requires": 1,
    },
    "Magento": {
        "body": [r"Mage\.Cookies", r"mage/requirejs", r"/static/version", r"magento"],
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
        "body": [r"bigcommerce\.com", r"BCData", r"bigcommerce"],
        "confidence": 88,
        "requires": 1,
    },
    "OpenCart": {
        "body": [r"catalog/view/theme", r"route=common", r"opencart"],
        "confidence": 82,
        "requires": 1,
    },
    "Wix Stores": {
        "body": [r"wix\.com", r"wixstatic\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Squarespace Commerce": {
        "body": [r"squarespace\.com", r"sqsp\.net"],
        "confidence": 85,
        "requires": 1,
    },
    "Volusion": {
        "body": [r"volusion\.com", r"a]volusion"],
        "confidence": 82,
        "requires": 1,
    },
    "3dcart": {
        "body": [r"3dcart\.com", r"shift4shop"],
        "confidence": 80,
        "requires": 1,
    },
    "Ecwid": {
        "body": [r"ecwid\.com", r"app\.ecwid\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Big Cartel": {
        "body": [r"bigcartel\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Snipcart": {
        "body": [r"snipcart\.com", r"snipcart"],
        "confidence": 85,
        "requires": 1,
    },
    "Gumroad": {
        "body": [r"gumroad\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Sellfy": {
        "body": [r"sellfy\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Paddle": {
        "body": [r"paddle\.com", r"cdn\.paddle\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "FastSpring": {
        "body": [r"fastspring\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Chargebee": {
        "body": [r"chargebee\.com", r"js\.chargebee\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Recurly": {
        "body": [r"recurly\.com", r"js\.recurly\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Zuora": {
        "body": [r"zuora\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "Chargify": {
        "body": [r"chargify\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "Stripe Billing": {
        "body": [r"billing\.stripe\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "PayPal Commerce": {
        "body": [r"paypal\.com/sdk", r"paypalobjects\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "Klarna": {
        "body": [r"klarna\.com", r"klarna-payments"],
        "confidence": 90,
        "requires": 1,
    },
    "Afterpay": {
        "body": [r"afterpay\.com", r"static\.afterpay\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Affirm": {
        "body": [r"affirm\.com", r"cdn1\.affirm\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Sezzle": {
        "body": [r"sezzle\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Zip (QuadPay)": {
        "body": [r"quadpay\.com", r"zip\.co"],
        "confidence": 82,
        "requires": 1,
    },
    "Clearpay": {
        "body": [r"clearpay\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "LayBuy": {
        "body": [r"laybuy\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Splitit": {
        "body": [r"splitit\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Bolt": {
        "body": [r"bolt\.com", r"connect\.bolt\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Shop Pay": {
        "body": [r"shop\.app", r"shop\.pay"],
        "confidence": 88,
        "requires": 1,
    },
    "Amazon Pay": {
        "body": [r"amazonpay\.com", r"payments\.amazon"],
        "confidence": 90,
        "requires": 1,
    },
    "Apple Pay": {
        "body": [r"apple-pay-button", r"ApplePaySession"],
        "confidence": 88,
        "requires": 1,
    },
    "Google Pay": {
        "body": [r"pay\.google\.com", r"google-pay-button"],
        "confidence": 90,
        "requires": 1,
    },
    "Venmo": {
        "body": [r"venmo\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Alipay": {
        "body": [r"alipay\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "WeChat Pay": {
        "body": [r"wechatpay", r"wx\.qq\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Razorpay": {
        "body": [r"razorpay\.com", r"checkout\.razorpay\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "Paytm": {
        "body": [r"paytm\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "PhonePe": {
        "body": [r"phonepe\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Mollie": {
        "body": [r"mollie\.com", r"js\.mollie\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Adyen": {
        "body": [r"adyen\.com", r"checkoutshopper"],
        "confidence": 88,
        "requires": 1,
    },
    "Worldpay": {
        "body": [r"worldpay\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Checkout.com": {
        "body": [r"checkout\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "2Checkout": {
        "body": [r"2checkout\.com", r"verifone\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Authorize.net": {
        "body": [r"authorize\.net", r"accept\.js"],
        "confidence": 85,
        "requires": 1,
    },
    "Cybersource": {
        "body": [r"cybersource\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Braintree": {
        "body": [r"braintreepayments\.com", r"braintreegateway\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "Square": {
        "body": [r"squareup\.com", r"square\.site"],
        "confidence": 88,
        "requires": 1,
    },
    "Yotpo": {
        "body": [r"yotpo\.com", r"staticw2\.yotpo\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Judge.me": {
        "body": [r"judge\.me"],
        "confidence": 85,
        "requires": 1,
    },
    "Stamped.io": {
        "body": [r"stamped\.io"],
        "confidence": 85,
        "requires": 1,
    },
    "Loox": {
        "body": [r"loox\.io"],
        "confidence": 82,
        "requires": 1,
    },
    "Okendo": {
        "body": [r"okendo\.io"],
        "confidence": 82,
        "requires": 1,
    },
    "Trustpilot": {
        "body": [r"trustpilot\.com", r"widget\.trustpilot\.com"],
        "confidence": 92,
        "requires": 1,
    },
    "Reviews.io": {
        "body": [r"reviews\.io"],
        "confidence": 85,
        "requires": 1,
    },
    "Bazaarvoice": {
        "body": [r"bazaarvoice\.com", r"bv\.js"],
        "confidence": 88,
        "requires": 1,
    },
    "PowerReviews": {
        "body": [r"powerreviews\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Feefo": {
        "body": [r"feefo\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Reevoo": {
        "body": [r"reevoo\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Shopper Approved": {
        "body": [r"shopperapproved\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Nosto": {
        "body": [r"nosto\.com", r"connect\.nosto\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Dynamic Yield": {
        "body": [r"dynamicyield\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Barilliance": {
        "body": [r"barilliance\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "RichRelevance": {
        "body": [r"richrelevance\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "Klevu": {
        "body": [r"klevu\.com", r"js\.klevu\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Searchspring": {
        "body": [r"searchspring\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Constructor.io": {
        "body": [r"constructor\.io"],
        "confidence": 82,
        "requires": 1,
    },
    "Doofinder": {
        "body": [r"doofinder\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "Findify": {
        "body": [r"findify\.io"],
        "confidence": 80,
        "requires": 1,
    },
    "Algolia Recommend": {
        "body": [r"algolia\.com/recommend"],
        "confidence": 82,
        "requires": 1,
    },
    "LimeSpot": {
        "body": [r"limespot\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Rebuy": {
        "body": [r"rebuyengine\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "Bold Commerce": {
        "body": [r"boldcommerce\.com", r"boldapps\.net"],
        "confidence": 82,
        "requires": 1,
    },
    "ReCharge": {
        "body": [r"rechargepayments\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Ordergroove": {
        "body": [r"ordergroove\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Smartrr": {
        "body": [r"smartrr\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Skio": {
        "body": [r"skio\.com"],
        "confidence": 75,
        "requires": 1,
    },
    "Loop Returns": {
        "body": [r"loopreturns\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "Returnly": {
        "body": [r"returnly\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Narvar": {
        "body": [r"narvar\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "AfterShip": {
        "body": [r"aftership\.com", r"track\.aftership\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Route": {
        "body": [r"route\.com", r"routeapp\.io"],
        "confidence": 82,
        "requires": 1,
    },
    "ShipBob": {
        "body": [r"shipbob\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "ShipStation": {
        "body": [r"shipstation\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "Shippo": {
        "body": [r"goshippo\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "EasyPost": {
        "body": [r"easypost\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Returngo": {
        "body": [r"returngo\.ai"],
        "confidence": 75,
        "requires": 1,
    },
    "Happy Returns": {
        "body": [r"happyreturns\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Optinmonster": {
        "body": [r"optinmonster\.com", r"omappapi\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Privy": {
        "body": [r"privy\.com", r"widget\.privy\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Justuno": {
        "body": [r"justuno\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Wisepops": {
        "body": [r"wisepops\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "Sleeknote": {
        "body": [r"sleeknote\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "OptiMonk": {
        "body": [r"optimonk\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Sumo": {
        "body": [r"sumo\.com", r"sumocdn\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Hello Bar": {
        "body": [r"hellobar\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Gorgias": {
        "body": [r"gorgias\.io", r"gorgias\.chat"],
        "confidence": 85,
        "requires": 1,
    },
    "Reamaze": {
        "body": [r"reamaze\.com", r"reamaze\.js"],
        "confidence": 82,
        "requires": 1,
    },
    "Gladly": {
        "body": [r"gladly\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Kustomer": {
        "body": [r"kustomer\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "Richpanel": {
        "body": [r"richpanel\.com"],
        "confidence": 78,
        "requires": 1,
    },
}
