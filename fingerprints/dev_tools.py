DEV_TOOLS = {
    # CI/CD
    "GitHub Actions": {
        "body": [r"github\.com/.*actions", r"actions/checkout"],
        "confidence": 75,
        "requires": 1,
    },
    "GitLab CI": {
        "body": [r"gitlab-ci", r"gitlab\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "CircleCI": {
        "body": [r"circleci\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Travis CI": {
        "body": [r"travis-ci\.org", r"travis-ci\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Jenkins": {
        "body": [r"jenkins", r"Jenkins"],
        "headers": {"X-Jenkins": r".+"},
        "confidence": 85,
        "requires": 1,
    },
    "TeamCity": {
        "body": [r"teamcity"],
        "confidence": 78,
        "requires": 1,
    },
    "Bamboo": {
        "body": [r"bamboo\.atlassian"],
        "confidence": 75,
        "requires": 1,
    },
    "Azure DevOps": {
        "body": [r"dev\.azure\.com", r"visualstudio\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Bitbucket Pipelines": {
        "body": [r"bitbucket-pipelines"],
        "confidence": 75,
        "requires": 1,
    },
    "Buildkite": {
        "body": [r"buildkite\.com"],
        "confidence": 75,
        "requires": 1,
    },
    "Semaphore": {
        "body": [r"semaphoreci\.com"],
        "confidence": 72,
        "requires": 1,
    },
    "Codefresh": {
        "body": [r"codefresh\.io"],
        "confidence": 72,
        "requires": 1,
    },
    "Drone": {
        "body": [r"drone\.io"],
        "confidence": 72,
        "requires": 1,
    },

    # Deployment Platforms
    "Heroku": {
        "headers": {"Via": r"heroku"},
        "body": [r"herokuapp\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "Railway": {
        "body": [r"railway\.app"],
        "confidence": 85,
        "requires": 1,
    },
    "Render": {
        "body": [r"onrender\.com", r"render\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Fly.io": {
        "headers": {"Fly-Request-Id": r".+"},
        "body": [r"fly\.io", r"fly\.dev"],
        "confidence": 88,
        "requires": 1,
    },
    "PlanetScale": {
        "body": [r"planetscale\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Supabase": {
        "body": [r"supabase\.co", r"supabase\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "Neon": {
        "body": [r"neon\.tech"],
        "confidence": 80,
        "requires": 1,
    },
    "Upstash": {
        "body": [r"upstash\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Deno Deploy": {
        "body": [r"deno\.dev", r"deno\.land"],
        "confidence": 82,
        "requires": 1,
    },
    "Cloudflare Workers": {
        "headers": {"CF-Worker": r".+"},
        "body": [r"workers\.dev"],
        "confidence": 88,
        "requires": 1,
    },
    "Cloudflare Pages": {
        "body": [r"pages\.dev"],
        "confidence": 85,
        "requires": 1,
    },
    "AWS Lambda": {
        "headers": {"X-Amz-Cf-Id": r".+"},
        "body": [r"lambda\.amazonaws"],
        "confidence": 82,
        "requires": 1,
    },
    "Google Cloud Functions": {
        "body": [r"cloudfunctions\.net"],
        "confidence": 82,
        "requires": 1,
    },
    "Azure Functions": {
        "body": [r"azurewebsites\.net", r"\.azure\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "DigitalOcean App Platform": {
        "body": [r"ondigitalocean\.app"],
        "confidence": 85,
        "requires": 1,
    },
    "Glitch": {
        "body": [r"glitch\.me", r"glitch\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Replit": {
        "body": [r"replit\.com", r"repl\.co"],
        "confidence": 88,
        "requires": 1,
    },
    "CodeSandbox": {
        "body": [r"codesandbox\.io", r"csb\.app"],
        "confidence": 85,
        "requires": 1,
    },
    "StackBlitz": {
        "body": [r"stackblitz\.com", r"stackblitz\.io"],
        "confidence": 82,
        "requires": 1,
    },

    # Containerization
    "Docker": {
        "body": [r"docker\.com", r"docker\.io"],
        "confidence": 75,
        "requires": 1,
    },
    "Kubernetes": {
        "body": [r"kubernetes\.io", r"k8s\.io"],
        "confidence": 75,
        "requires": 1,
    },
    "Rancher": {
        "body": [r"rancher\.com"],
        "confidence": 72,
        "requires": 1,
    },
    "Portainer": {
        "body": [r"portainer\.io"],
        "confidence": 72,
        "requires": 1,
    },

    # Monitoring
    "Prometheus": {
        "body": [r"prometheus\.io"],
        "confidence": 75,
        "requires": 1,
    },
    "Grafana Cloud": {
        "body": [r"grafana\.net"],
        "confidence": 78,
        "requires": 1,
    },
    "Datadog": {
        "body": [r"datadoghq\.com", r"dd-agent"],
        "confidence": 88,
        "requires": 1,
    },
    "New Relic": {
        "body": [r"newrelic\.com", r"nr-data\.net"],
        "confidence": 90,
        "requires": 1,
    },
    "AppDynamics": {
        "body": [r"appdynamics\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Dynatrace": {
        "body": [r"dynatrace\.com", r"js\.dynatrace"],
        "confidence": 85,
        "requires": 1,
    },
    "Elastic APM": {
        "body": [r"elastic-apm-js"],
        "confidence": 78,
        "requires": 1,
    },
    "Splunk": {
        "body": [r"splunk\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Sumo Logic": {
        "body": [r"sumologic\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Logz.io": {
        "body": [r"logz\.io"],
        "confidence": 75,
        "requires": 1,
    },
    "Loggly": {
        "body": [r"loggly\.com"],
        "confidence": 75,
        "requires": 1,
    },
    "Papertrail": {
        "body": [r"papertrailapp\.com"],
        "confidence": 75,
        "requires": 1,
    },
    "LogDNA": {
        "body": [r"logdna\.com", r"mezmo\.com"],
        "confidence": 75,
        "requires": 1,
    },

    # Search
    "Elasticsearch": {
        "body": [r"elasticsearch", r"elastic\.co"],
        "confidence": 82,
        "requires": 1,
    },
    "Algolia": {
        "body": [r"algolia\.com", r"algolianet\.com", r"algoliasearch"],
        "confidence": 92,
        "requires": 1,
    },
    "Meilisearch": {
        "body": [r"meilisearch", r"meili\.pw"],
        "confidence": 78,
        "requires": 1,
    },
    "Typesense": {
        "body": [r"typesense", r"typesense\.org"],
        "confidence": 78,
        "requires": 1,
    },
    "Solr": {
        "body": [r"solr", r"apache\.org/solr"],
        "confidence": 78,
        "requires": 1,
    },
    "Swiftype": {
        "body": [r"swiftype\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Coveo": {
        "body": [r"coveo\.com"],
        "confidence": 80,
        "requires": 1,
    },

    # Feature Flags
    "LaunchDarkly": {
        "body": [r"launchdarkly\.com", r"ld\.js"],
        "confidence": 88,
        "requires": 1,
    },
    "Split.io": {
        "body": [r"split\.io"],
        "confidence": 82,
        "requires": 1,
    },
    "Optimizely": {
        "body": [r"optimizely\.com", r"optimizely\.js"],
        "confidence": 90,
        "requires": 1,
    },
    "VWO": {
        "body": [r"visualwebsiteoptimizer\.com", r"vwo\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "AB Tasty": {
        "body": [r"abtasty\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Google Optimize": {
        "body": [r"optimize\.google\.com", r"gtag.*optimize"],
        "confidence": 88,
        "requires": 1,
    },
    "Kameleoon": {
        "body": [r"kameleoon\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "ConfigCat": {
        "body": [r"configcat\.com"],
        "confidence": 75,
        "requires": 1,
    },
    "Statsig": {
        "body": [r"statsig\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Unleash": {
        "body": [r"unleash-hosted\.com", r"getunleash\.io"],
        "confidence": 75,
        "requires": 1,
    },
    "Flagsmith": {
        "body": [r"flagsmith\.com"],
        "confidence": 72,
        "requires": 1,
    },
    "PostHog": {
        "body": [r"posthog\.com", r"app\.posthog\.com"],
        "confidence": 85,
        "requires": 1,
    },

    # Cloud Storage
    "AWS S3": {
        "body": [r"s3\.amazonaws\.com", r"s3-.*\.amazonaws\.com", r"\.s3\."],
        "confidence": 90,
        "requires": 1,
    },
    "Google Cloud Storage": {
        "body": [r"storage\.googleapis\.com", r"storage\.cloud\.google"],
        "confidence": 88,
        "requires": 1,
    },
    "Azure Blob Storage": {
        "body": [r"blob\.core\.windows\.net"],
        "confidence": 88,
        "requires": 1,
    },
    "Backblaze B2": {
        "body": [r"backblazeb2\.com", r"f000\.backblazeb2"],
        "confidence": 82,
        "requires": 1,
    },
    "Wasabi": {
        "body": [r"wasabisys\.com"],
        "confidence": 80,
        "requires": 1,
    },
    "DigitalOcean Spaces": {
        "body": [r"digitaloceanspaces\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Vultr Object Storage": {
        "body": [r"vultr\.objects"],
        "confidence": 78,
        "requires": 1,
    },
    "Linode Object Storage": {
        "body": [r"linodeobjects\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Cloudinary": {
        "body": [r"cloudinary\.com", r"res\.cloudinary\.com"],
        "confidence": 92,
        "requires": 1,
    },
    "Imgix": {
        "body": [r"imgix\.net", r"imgix\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "ImageKit": {
        "body": [r"imagekit\.io", r"ik\.imagekit\.io"],
        "confidence": 85,
        "requires": 1,
    },
    "Uploadcare": {
        "body": [r"uploadcare\.com", r"ucarecdn\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Filestack": {
        "body": [r"filestack\.com", r"filestackapi\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Transloadit": {
        "body": [r"transloadit\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Mux": {
        "body": [r"mux\.com", r"stream\.mux\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Bunny CDN": {
        "body": [r"bunnycdn\.com", r"b-cdn\.net"],
        "confidence": 88,
        "requires": 1,
    },
    "KeyCDN": {
        "body": [r"keycdn\.com", r"kxcdn\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "StackPath": {
        "body": [r"stackpath\.com", r"stackpathdns\.com"],
        "confidence": 82,
        "requires": 1,
    },
}
