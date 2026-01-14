FRONTEND = {
    "React": {
        "body": [
            r"_reactRootContainer",
            r'data-reactroot',
            r"react-dom[/@]",
            r"react\.production\.min\.js",
            r"__REACT_DEVTOOLS",
        ],
        "confidence": 85,
        "requires": 1,
    },
    "Vue.js": {
        "body": [
            r"data-v-[a-f0-9]{6,8}",
            r"Vue\.config",
            r"vue\.runtime",
            r"vue\.global\.prod",
            r"__VUE__",
        ],
        "confidence": 85,
        "requires": 1,
    },
    "Angular": {
        "body": [
            r"ng-version=",
            r"ng-app=",
            r"angular\.min\.js",
            r"@angular/core",
        ],
        "confidence": 88,
        "requires": 1,
    },
    "Svelte": {
        "body": [
            r"svelte-[a-z0-9]{6,}",
            r"__svelte",
            r"svelte\.dev",
        ],
        "confidence": 85,
        "requires": 1,
    },
    "Preact": {
        "body": [r"preact[/.-]", r"preactjs\.com", r"preact\.min\.js"],
        "confidence": 85,
        "requires": 1,
    },
    "Solid.js": {
        "body": [r"solid-js", r"_\$HY"],
        "confidence": 80,
        "requires": 1,
    },
    "Alpine.js": {
        "body": [r'x-data="', r"x-bind:", r"alpinejs\.dev", r"alpine\.min\.js"],
        "confidence": 85,
        "requires": 1,
    },
    "HTMX": {
        "body": [r'hx-get="', r'hx-post="', r"htmx\.org", r"htmx\.min\.js"],
        "confidence": 90,
        "requires": 1,
    },
    "Stimulus": {
        "body": [r'data-controller="', r"stimulus\.hotwired"],
        "confidence": 85,
        "requires": 1,
    },
    "Turbo": {
        "body": [r"turbo\.hotwired", r"data-turbo", r"turbo-frame"],
        "confidence": 85,
        "requires": 1,
    },
    "Lit": {
        "body": [r"lit-element", r"lit-html", r"@lit/"],
        "confidence": 82,
        "requires": 1,
    },
    "Ember.js": {
        "body": [r"ember\.js", r"emberjs\.com", r"data-ember"],
        "confidence": 85,
        "requires": 1,
    },
    "Backbone.js": {
        "body": [r"backbone[/.-][\d.]+", r"backbone\.min\.js", r"Backbone\."],
        "confidence": 82,
        "requires": 1,
    },
    "Knockout": {
        "body": [r"knockout[/.-][\d.]+", r"ko\.applyBindings"],
        "confidence": 82,
        "requires": 1,
    },
    "Mithril": {
        "body": [r"mithril[/.-][\d.]+", r"mithril\.min\.js"],
        "confidence": 80,
        "requires": 1,
    },
    "Qwik": {
        "body": [r"qwik\.builder\.io", r"qwikloader"],
        "confidence": 85,
        "requires": 1,
    },
    "Inferno": {
        "body": [r"inferno[/.-][\d.]+", r"infernojs\.org"],
        "confidence": 80,
        "requires": 1,
    },
    "Riot.js": {
        "body": [r"riot[/.-][\d.]+", r"riot\.min\.js"],
        "confidence": 78,
        "requires": 1,
    },
    "Aurelia": {
        "body": [r"aurelia[/.-]", r"aurelia\.io"],
        "confidence": 78,
        "requires": 1,
    },
    "Stencil": {
        "body": [r"stenciljs\.com", r"stencil/"],
        "confidence": 78,
        "requires": 1,
    },
}
