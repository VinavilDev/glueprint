CSS = {
    # Frameworks
    "Tailwind CSS": {
        "body": [
            r"tailwindcss[/.-]",
            r"tailwind\.config",
            r'class="[^"]*(?:flex|grid)\s+[^"]*(?:gap-|space-)[^"]*"',
        ],
        "confidence": 85,
        "requires": 1,
    },
    "Bootstrap": {
        "body": [
            r"bootstrap[/.-][\d.]+(?:\.min)?\.(?:css|js)",
            r"getbootstrap\.com",
            r'class="[^"]*(?:container|row|col-(?:sm|md|lg|xl)-\d+)[^"]*"',
        ],
        "confidence": 92,
        "requires": 1,
    },
    "Bulma": {
        "body": [r"bulma[/.-][\d.]+", r"bulma\.io"],
        "confidence": 88,
        "requires": 1,
    },
    "Foundation": {
        "body": [r"foundation[/.-][\d.]+", r"foundation\.zurb\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Materialize CSS": {
        "body": [r"materialize[/.-][\d.]+", r"materializecss\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "Semantic UI": {
        "body": [r"semantic[/.-][\d.]+", r"semantic-ui\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "UIkit": {
        "body": [r"uikit[/.-][\d.]+", r"getuikit\.com", r'class="[^"]*uk-[^"]*"'],
        "confidence": 90,
        "requires": 1,
    },
    "Ant Design": {
        "body": [r"antd[/.-][\d.]+", r"ant-design", r'class="[^"]*ant-[^"]*"'],
        "confidence": 88,
        "requires": 1,
    },
    "Material UI": {
        "body": [r"@mui/material", r"material-ui", r'class="[^"]*Mui[^"]*"'],
        "confidence": 85,
        "requires": 1,
    },
    "Chakra UI": {
        "body": [r"@chakra-ui", r"chakra-ui\.com"],
        "confidence": 82,
        "requires": 1,
    },
    "Mantine": {
        "body": [r"@mantine", r"mantine\.dev"],
        "confidence": 82,
        "requires": 1,
    },
    "DaisyUI": {
        "body": [r"daisyui", r'class="[^"]*(?:btn-primary|card-body)[^"]*"'],
        "confidence": 82,
        "requires": 1,
    },
    "Pure CSS": {
        "body": [r"pure[/.-][\d.]+\.css", r"purecss\.io"],
        "confidence": 82,
        "requires": 1,
    },
    "Milligram": {
        "body": [r"milligram[/.-][\d.]+", r"milligram\.io"],
        "confidence": 78,
        "requires": 1,
    },
    "Skeleton": {
        "body": [r"skeleton[/.-][\d.]+\.css", r"getskeleton\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Water.css": {
        "body": [r"water\.css", r"watercss"],
        "confidence": 75,
        "requires": 1,
    },
    "Normalize.css": {
        "body": [r"normalize[/.-][\d.]+\.css", r"necolas\.github\.io/normalize"],
        "confidence": 88,
        "requires": 1,
    },
    "Animate.css": {
        "body": [r"animate[/.-][\d.]+\.css", r"animate\.style", r'class="[^"]*animate__[^"]*"'],
        "confidence": 90,
        "requires": 1,
    },
    "Hover.css": {
        "body": [r"hover[/.-][\d.]+\.css", r"hover-min\.css"],
        "confidence": 78,
        "requires": 1,
    },

    # Icon Libraries
    "Font Awesome": {
        "body": [
            r"font-?awesome[/.-][\d.]+",
            r"fontawesome\.com",
            r'class="[^"]*fa(?:s|r|b|l)?\s+fa-[^"]*"',
            r"kit\.fontawesome\.com",
            r"cdnjs\.cloudflare\.com/ajax/libs/font-awesome",
        ],
        "confidence": 95,
        "requires": 1,
    },
    "Material Icons": {
        "body": [r"material-icons", r"fonts\.googleapis\.com/icon\?family=Material"],
        "confidence": 92,
        "requires": 1,
    },
    "Material Symbols": {
        "body": [r"material-symbols", r"fonts\.googleapis\.com.*Material\+Symbols"],
        "confidence": 88,
        "requires": 1,
    },
    "Feather Icons": {
        "body": [r"feather-icons", r"feathericons\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Heroicons": {
        "body": [r"heroicons", r"@heroicons"],
        "confidence": 82,
        "requires": 1,
    },
    "Lucide": {
        "body": [r"lucide[/.-]", r"lucide-react"],
        "confidence": 80,
        "requires": 1,
    },
    "Phosphor Icons": {
        "body": [r"phosphor-icons", r"phosphoricons\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Tabler Icons": {
        "body": [r"tabler-icons", r"tablericons\.com"],
        "confidence": 78,
        "requires": 1,
    },
    "Remix Icon": {
        "body": [r"remixicon", r'class="[^"]*ri-[^"]*"'],
        "confidence": 82,
        "requires": 1,
    },
    "Ionicons": {
        "body": [r"ionicons[/.-]", r"ionic\.io/ionicons", r"ion-icon"],
        "confidence": 88,
        "requires": 1,
    },
    "Bootstrap Icons": {
        "body": [r"bootstrap-icons", r'class="[^"]*bi-[^"]*"'],
        "confidence": 88,
        "requires": 1,
    },
    "Line Awesome": {
        "body": [r"line-awesome", r'class="[^"]*la(?:s|r|b)?\s+la-[^"]*"'],
        "confidence": 80,
        "requires": 1,
    },
    "Simple Icons": {
        "body": [r"simple-icons", r"simpleicons\.org"],
        "confidence": 78,
        "requires": 1,
    },
    "Boxicons": {
        "body": [r"boxicons", r'class="[^"]*bx-[^"]*"'],
        "confidence": 82,
        "requires": 1,
    },
    "Eva Icons": {
        "body": [r"eva-icons", r"akveo\.github\.io/eva-icons"],
        "confidence": 78,
        "requires": 1,
    },
    "css.gg": {
        "body": [r"css\.gg", r'class="[^"]*gg-[^"]*"'],
        "confidence": 75,
        "requires": 1,
    },
    "IcoMoon": {
        "body": [r"icomoon", r"IcoMoon"],
        "confidence": 80,
        "requires": 1,
    },
    "Flaticon": {
        "body": [r"flaticon\.com", r"fi-[a-z]+-"],
        "confidence": 82,
        "requires": 1,
    },
}
