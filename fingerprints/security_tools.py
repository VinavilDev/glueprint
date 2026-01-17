SECURITY_TOOLS = {
    "reCAPTCHA": {
        "body": [r"google\.com/recaptcha", r"grecaptcha", r"g-recaptcha"],
        "confidence": 95,
        "requires": 1,
    },
    "reCAPTCHA v3": {
        "body": [r"recaptcha/api\.js\?render=", r"grecaptcha\.execute"],
        "confidence": 92,
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
    "FunCaptcha": {
        "body": [r"funcaptcha\.com", r"arkoselabs\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "GeeTest": {
        "body": [r"geetest\.com", r"gt\.js"],
        "confidence": 85,
        "requires": 1,
    },
    "KeyCAPTCHA": {
        "body": [r"keycaptcha\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "Akismet": {
        "body": [r"akismet\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "CleanTalk": {
        "body": [r"cleantalk\.org"],
        "confidence": 82,
        "requires": 1,
    },
    "Honeypot": {
        "body": [r"projecthoneypot\.org"],
        "confidence": 75,
        "requires": 1,
    },
    "Kasada": {
        "body": [r"kasada\.io"],
        "confidence": 85,
        "requires": 1,
    },
    "Shape Security": {
        "body": [r"shape\.com", r"shapesecurity\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "PerimeterX": {
        "body": [r"perimeterx\.com", r"px\.js"],
        "cookies": [r"^_px"],
        "confidence": 90,
        "requires": 1,
    },
    "DataDome": {
        "headers": {"X-DataDome": r".+"},
        "cookies": [r"^datadome$"],
        "body": [r"datadome\.co"],
        "confidence": 95,
        "requires": 1,
    },
    "Akamai Bot Manager": {
        "body": [r"akamaibotmanager", r"_abck"],
        "cookies": [r"^_abck$"],
        "confidence": 88,
        "requires": 1,
    },
    "Distil Networks": {
        "body": [r"distilnetworks\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Human (White Ops)": {
        "body": [r"humansecurity\.com", r"whiteops\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "Auth0": {
        "body": [r"auth0\.com", r"cdn\.auth0\.com"],
        "confidence": 92,
        "requires": 1,
    },
    "Okta": {
        "body": [r"okta\.com", r"oktacdn\.com"],
        "confidence": 92,
        "requires": 1,
    },
    "OneLogin": {
        "body": [r"onelogin\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Ping Identity": {
        "body": [r"pingidentity\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "ForgeRock": {
        "body": [r"forgerock\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Duo Security": {
        "body": [r"duo\.com", r"duosecurity\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Authy": {
        "body": [r"authy\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Google Authenticator": {
        "body": [r"google\.com/.*authenticator"],
        "confidence": 75,
        "requires": 1,
    },
    "YubiKey": {
        "body": [r"yubico\.com", r"yubikey"],
        "confidence": 80,
        "requires": 1,
    },
    "Clerk": {
        "body": [r"clerk\.com", r"clerk\.dev"],
        "confidence": 88,
        "requires": 1,
    },
    "Stytch": {
        "body": [r"stytch\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Passage": {
        "body": [r"passage\.id"],
        "confidence": 78,
        "requires": 1,
    },
    "Magic": {
        "body": [r"magic\.link"],
        "confidence": 80,
        "requires": 1,
    },
    "Descope": {
        "body": [r"descope\.com"],
        "confidence": 75,
        "requires": 1,
    },
    "WorkOS": {
        "body": [r"workos\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "FusionAuth": {
        "body": [r"fusionauth\.io"],
        "confidence": 78,
        "requires": 1,
    },
    "Keycloak": {
        "body": [r"keycloak\.org", r"/auth/realms/"],
        "confidence": 85,
        "requires": 1,
    },
    "AWS Cognito": {
        "body": [r"cognito", r"amazoncognito"],
        "confidence": 82,
        "requires": 1,
    },
    "Firebase Auth": {
        "body": [r"firebase\.google\.com.*auth", r"firebaseAuth"],
        "confidence": 85,
        "requires": 1,
    },
    "Supabase Auth": {
        "body": [r"supabase\.co.*auth", r"supabase\.auth"],
        "confidence": 82,
        "requires": 1,
    },
    "Netlify Identity": {
        "body": [r"netlify-identity-widget"],
        "confidence": 80,
        "requires": 1,
    },
    "Userfront": {
        "body": [r"userfront\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Ory": {
        "body": [r"ory\.sh", r"ory\.am"],
        "confidence": 78,
        "requires": 1,
    },
    "Sentry": {
        "body": [r"browser\.sentry-cdn\.com", r"sentry\.io", r"Sentry\.init"],
        "confidence": 92,
        "requires": 1,
    },
    "Bugsnag": {
        "body": [r"bugsnag\.com", r"d2wy8f7a9ursnm\.cloudfront\.net"],
        "confidence": 88,
        "requires": 1,
    },
    "Rollbar": {
        "body": [r"rollbar\.com", r"Rollbar\.init"],
        "confidence": 88,
        "requires": 1,
    },
    "Datadog RUM": {
        "body": [r"datadoghq\.com", r"DD_RUM"],
        "confidence": 88,
        "requires": 1,
    },
    "New Relic Browser": {
        "body": [r"newrelic\.com", r"js-agent\.newrelic\.com", r"NREUM"],
        "confidence": 90,
        "requires": 1,
    },
    "Raygun": {
        "body": [r"raygun\.com", r"raygun4js"],
        "confidence": 85,
        "requires": 1,
    },
    "TrackJS": {
        "body": [r"trackjs\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Airbrake": {
        "body": [r"airbrake\.io"],
        "confidence": 82,
        "requires": 1,
    },
    "Honeybadger": {
        "body": [r"honeybadger\.io"],
        "confidence": 80,
        "requires": 1,
    },
    "LogRocket": {
        "body": [r"logrocket\.com", r"cdn\.logrocket\.io"],
        "confidence": 88,
        "requires": 1,
    },
    "FullStory": {
        "body": [r"fullstory\.com", r"edge\.fullstory\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "SessionStack": {
        "body": [r"sessionstack\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Zipy": {
        "body": [r"zipy\.ai"],
        "confidence": 78,
        "requires": 1,
    },
    "Highlight.io": {
        "body": [r"highlight\.io"],
        "confidence": 78,
        "requires": 1,
    },
    "Instabug": {
        "body": [r"instabug\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "BetterStack": {
        "body": [r"betterstack\.com", r"logtail\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Splunk RUM": {
        "body": [r"splunk\.com", r"signalfx\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "AppDynamics": {
        "body": [r"appdynamics\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Dynatrace": {
        "body": [r"dynatrace\.com", r"dynatracelabs\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Elastic APM": {
        "body": [r"elastic-apm"],
        "confidence": 78,
        "requires": 1,
    },
    "Grafana": {
        "body": [r"grafana\.com", r"grafana-agent"],
        "confidence": 80,
        "requires": 1,
    },
}
