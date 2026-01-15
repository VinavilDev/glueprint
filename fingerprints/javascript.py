JAVASCRIPT = {
    # Core Libraries
    "jQuery": {
        "body": [
            r"jquery[/.-][\d.]+\.(?:min\.)?js",
            r"jQuery\s+(?:JavaScript Library\s+)?v?[\d.]+",
            r"/jquery\.min\.js",
            r"jquery\.com/jquery",
        ],
        "confidence": 92,
        "requires": 1,
    },
    "jQuery UI": {
        "body": [
            r"jquery-ui[/.-][\d.]+",
            r"jquery\.ui\.[a-z]+\.js",
            r"/ui/[\d.]+/jquery-ui",
            r"ui-widget",
            r"jQuery UI [\d.]+",
        ],
        "confidence": 90,
        "requires": 1,
    },
    "jQuery Migrate": {
        "body": [r"jquery-migrate[/.-][\d.]+", r"jquery\.migrate\.min"],
        "confidence": 85,
        "requires": 1,
    },
    "Zepto": {
        "body": [r"zepto[/.-][\d.]+", r"zeptojs\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Lodash": {
        "body": [r"lodash[/.-][\d.]+", r"lodash\.min\.js", r"_\.VERSION"],
        "confidence": 88,
        "requires": 1,
    },
    "Underscore": {
        "body": [r"underscore[/.-][\d.]+", r"underscore-min\.js"],
        "confidence": 85,
        "requires": 1,
    },
    "Axios": {
        "body": [r"axios[/.-][\d.]+", r"axios\.min\.js"],
        "confidence": 85,
        "requires": 1,
    },
    "Moment.js": {
        "body": [r"moment[/.-][\d.]+", r"moment\.min\.js", r"momentjs\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Day.js": {
        "body": [r"dayjs[/.-][\d.]+", r"dayjs\.min\.js"],
        "confidence": 85,
        "requires": 1,
    },
    "date-fns": {
        "body": [r"date-fns[/.-]", r"dateFns"],
        "confidence": 82,
        "requires": 1,
    },
    "Luxon": {
        "body": [r"luxon[/.-][\d.]+", r"luxon\.min\.js"],
        "confidence": 82,
        "requires": 1,
    },

    # Animation
    "GSAP": {
        "body": [r"gsap[/.-][\d.]+", r"TweenMax", r"TweenLite", r"greensock\.com", r"gsap\.to\s*\("],
        "confidence": 92,
        "requires": 1,
    },
    "Anime.js": {
        "body": [r"anime[/.-][\d.]+\.(?:min\.)?js", r"animejs\.com", r"anime\s*\(\s*\{"],
        "confidence": 92,
        "requires": 1,
    },
    "Velocity.js": {
        "body": [r"velocity[/.-][\d.]+", r"velocity\.min\.js", r"Velocity\s*\("],
        "confidence": 85,
        "requires": 1,
    },
    "Popmotion": {
        "body": [r"popmotion[/.-]", r"popmotion\.io"],
        "confidence": 82,
        "requires": 1,
    },
    "Lottie": {
        "body": [r"lottie[/.-]", r"lottie-web", r"lottiefiles\.com", r"bodymovin"],
        "confidence": 90,
        "requires": 1,
    },
    "Framer Motion": {
        "body": [r"framer-motion", r"framer\.com/motion"],
        "confidence": 85,
        "requires": 1,
    },
    "AOS": {
        "body": [r"aos[/.-][\d.]+", r'data-aos="', r"aos\.css"],
        "confidence": 90,
        "requires": 1,
    },
    "ScrollReveal": {
        "body": [r"scrollreveal[/.-]", r"ScrollReveal\s*\(\s*\)"],
        "confidence": 85,
        "requires": 1,
    },
    "Barba.js": {
        "body": [r"barba[/.-]", r"barba\.js", r"@barba/core"],
        "confidence": 85,
        "requires": 1,
    },
    "LocomotiveScroll": {
        "body": [r"locomotive-scroll", r"locomotivemtl"],
        "confidence": 85,
        "requires": 1,
    },
    "Rellax": {
        "body": [r"rellax[/.-][\d.]+", r"rellax\.min\.js"],
        "confidence": 82,
        "requires": 1,
    },
    "Parallax.js": {
        "body": [r"parallax[/.-][\d.]+\.js", r"Parallax\s*\("],
        "confidence": 80,
        "requires": 1,
    },
    "ScrollMagic": {
        "body": [r"scrollmagic[/.-]", r"ScrollMagic\.Controller"],
        "confidence": 85,
        "requires": 1,
    },
    "GreenSock ScrollTrigger": {
        "body": [r"ScrollTrigger", r"gsap\.registerPlugin\s*\(\s*ScrollTrigger"],
        "confidence": 85,
        "requires": 1,
    },

    # Visualization
    "D3.js": {
        "body": [r"d3[/.-]v?[\d.]+", r"d3\.min\.js", r"d3js\.org"],
        "confidence": 92,
        "requires": 1,
    },
    "Chart.js": {
        "body": [r"chart[/.-][\d.]+\.js", r"chartjs\.org", r"new\s+Chart\s*\("],
        "confidence": 92,
        "requires": 1,
    },
    "Three.js": {
        "body": [r"three[/.-][\d.]+", r"three\.min\.js", r"THREE\.Scene", r"threejs\.org"],
        "confidence": 92,
        "requires": 1,
    },
    "Plotly": {
        "body": [r"plotly[/.-][\d.]+", r"plotly\.min\.js", r"Plotly\.newPlot"],
        "confidence": 88,
        "requires": 1,
    },
    "ApexCharts": {
        "body": [r"apexcharts[/.-]", r"ApexCharts"],
        "confidence": 85,
        "requires": 1,
    },
    "ECharts": {
        "body": [r"echarts[/.-]", r"echarts\.min\.js"],
        "confidence": 85,
        "requires": 1,
    },
    "Highcharts": {
        "body": [r"highcharts[/.-]", r"Highcharts\.chart"],
        "confidence": 90,
        "requires": 1,
    },
    "amCharts": {
        "body": [r"amcharts[/.-]", r"am4core", r"amcharts\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "Leaflet": {
        "body": [r"leaflet[/.-][\d.]+", r"leafletjs\.com", r"L\.map\s*\("],
        "confidence": 92,
        "requires": 1,
    },
    "Mapbox GL": {
        "body": [r"mapbox-gl[/.-]", r"mapboxgl\.accessToken"],
        "confidence": 88,
        "requires": 1,
    },
    "Google Maps API": {
        "body": [r"maps\.googleapis\.com", r"google\.maps\.", r"new\s+google\.maps"],
        "confidence": 95,
        "requires": 1,
    },
    "p5.js": {
        "body": [r"p5[/.-][\d.]+", r"p5\.min\.js"],
        "confidence": 85,
        "requires": 1,
    },
    "Paper.js": {
        "body": [r"paper[/.-][\d.]+", r"paper-full\.min\.js"],
        "confidence": 82,
        "requires": 1,
    },
    "Fabric.js": {
        "body": [r"fabric[/.-][\d.]+", r"fabric\.min\.js"],
        "confidence": 82,
        "requires": 1,
    },
    "PixiJS": {
        "body": [r"pixi[/.-][\d.]+", r"pixi\.min\.js", r"PIXI\.Application"],
        "confidence": 88,
        "requires": 1,
    },
    "Phaser": {
        "body": [r"phaser[/.-][\d.]+", r"phaser\.min\.js"],
        "confidence": 88,
        "requires": 1,
    },
    "Babylon.js": {
        "body": [r"babylon[/.-][\d.]+", r"babylonjs\.com"],
        "confidence": 85,
        "requires": 1,
    },

    # Sliders & Carousels
    "Swiper": {
        "body": [r"swiper[/.-][\d.]+", r"swiper-bundle", r"swiperjs\.com", r"new\s+Swiper\s*\(", r"swiper-slide"],
        "confidence": 92,
        "requires": 1,
    },
    "Slick": {
        "body": [r"slick[/.-][\d.]+", r"slick\.min\.js", r"\.slick\s*\(", r"slick-slider"],
        "confidence": 90,
        "requires": 1,
    },
    "Splide": {
        "body": [r"splide[/.-]", r"splidejs\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Glide.js": {
        "body": [r"glide[/.-][\d.]+", r"glidejs\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "Flickity": {
        "body": [r"flickity[/.-]", r"flickity\.pkgd"],
        "confidence": 88,
        "requires": 1,
    },
    "Owl Carousel": {
        "body": [r"owl\.carousel", r"owlcarousel", r"owl-carousel"],
        "confidence": 88,
        "requires": 1,
    },
    "Tiny Slider": {
        "body": [r"tiny-slider", r"tns-controls"],
        "confidence": 82,
        "requires": 1,
    },
    "Embla Carousel": {
        "body": [r"embla-carousel", r"EmblaCarousel"],
        "confidence": 80,
        "requires": 1,
    },

    # Lightbox & Gallery
    "Lightbox": {
        "body": [r"lightbox[/.-][\d.]+", r"ekko-lightbox"],
        "confidence": 82,
        "requires": 1,
    },
    "PhotoSwipe": {
        "body": [r"photoswipe[/.-]", r"PhotoSwipe\s*\("],
        "confidence": 88,
        "requires": 1,
    },
    "Fancybox": {
        "body": [r"fancybox[/.-][\d.]+", r"fancyapps\.com", r"data-fancybox"],
        "confidence": 90,
        "requires": 1,
    },
    "GLightbox": {
        "body": [r"glightbox[/.-]", r"GLightbox\s*\("],
        "confidence": 82,
        "requires": 1,
    },
    "SimpleLightbox": {
        "body": [r"simplelightbox[/.-]", r"SimpleLightbox"],
        "confidence": 80,
        "requires": 1,
    },
    "Magnific Popup": {
        "body": [r"magnific-popup", r"magnificPopup"],
        "confidence": 85,
        "requires": 1,
    },
    "baguetteBox": {
        "body": [r"baguettebox[/.-]", r"baguetteBox"],
        "confidence": 78,
        "requires": 1,
    },

    # UI Components
    "Tippy.js": {
        "body": [r"tippy[/.-][\d.]+", r"tippy\.js", r"@tippyjs"],
        "confidence": 88,
        "requires": 1,
    },
    "Popper.js": {
        "body": [r"popper[/.-][\d.]+", r"@popperjs", r"createPopper"],
        "confidence": 88,
        "requires": 1,
    },
    "Floating UI": {
        "body": [r"floating-ui", r"@floating-ui"],
        "confidence": 82,
        "requires": 1,
    },
    "SweetAlert2": {
        "body": [r"sweetalert2[/.-][\d.]+", r"sweetalert2", r"Swal\.fire"],
        "confidence": 90,
        "requires": 1,
    },
    "Toastr": {
        "body": [r"toastr[/.-][\d.]+", r"toastr\.min\.js"],
        "confidence": 85,
        "requires": 1,
    },
    "Notyf": {
        "body": [r"notyf[/.-]", r"new\s+Notyf"],
        "confidence": 82,
        "requires": 1,
    },
    "iziToast": {
        "body": [r"izitoast[/.-]", r"iziToast\."],
        "confidence": 82,
        "requires": 1,
    },
    "Select2": {
        "body": [r"select2[/.-][\d.]+", r"\.select2\s*\(", r"select2\.min"],
        "confidence": 88,
        "requires": 1,
    },
    "Choices.js": {
        "body": [r"choices[/.-][\d.]+", r"new\s+Choices\s*\("],
        "confidence": 82,
        "requires": 1,
    },
    "Flatpickr": {
        "body": [r"flatpickr[/.-]", r"flatpickr\.min", r"flatpickr-input"],
        "confidence": 88,
        "requires": 1,
    },
    "Pikaday": {
        "body": [r"pikaday[/.-]", r"new\s+Pikaday"],
        "confidence": 82,
        "requires": 1,
    },
    "Cleave.js": {
        "body": [r"cleave[/.-][\d.]+", r"new\s+Cleave"],
        "confidence": 82,
        "requires": 1,
    },
    "IMask": {
        "body": [r"imask[/.-]", r"IMask\s*\("],
        "confidence": 80,
        "requires": 1,
    },
    "Masonry": {
        "body": [r"masonry[/.-][\d.]+", r"masonry\.pkgd", r"Masonry\s*\("],
        "confidence": 88,
        "requires": 1,
    },
    "Isotope": {
        "body": [r"isotope[/.-][\d.]+", r"isotope\.pkgd"],
        "confidence": 88,
        "requires": 1,
    },
    "Typed.js": {
        "body": [r"typed[/.-][\d.]+", r"new\s+Typed\s*\("],
        "confidence": 85,
        "requires": 1,
    },
    "CountUp.js": {
        "body": [r"countup[/.-][\d.]+", r"CountUp\s*\("],
        "confidence": 82,
        "requires": 1,
    },
    "Waypoints": {
        "body": [r"waypoints[/.-][\d.]+", r"waypoints\.min\.js"],
        "confidence": 82,
        "requires": 1,
    },

    # Forms & Validation
    "Parsley": {
        "body": [r"parsley[/.-][\d.]+", r"data-parsley"],
        "confidence": 85,
        "requires": 1,
    },
    "jQuery Validate": {
        "body": [r"jquery\.validate", r"jquery-validation"],
        "confidence": 88,
        "requires": 1,
    },
    "Dropzone": {
        "body": [r"dropzone[/.-][\d.]+", r"dropzone\.min\.js", r"Dropzone\.options"],
        "confidence": 90,
        "requires": 1,
    },
    "FilePond": {
        "body": [r"filepond[/.-]", r"FilePond\.create"],
        "confidence": 85,
        "requires": 1,
    },
    "Uppy": {
        "body": [r"uppy[/.-]", r"Uppy\s*\("],
        "confidence": 82,
        "requires": 1,
    },

    # Text & Editor
    "Quill": {
        "body": [r"quill[/.-][\d.]+", r"quilljs\.com", r"new\s+Quill"],
        "confidence": 90,
        "requires": 1,
    },
    "TinyMCE": {
        "body": [r"tinymce[/.-][\d.]+", r"tinymce\.min\.js", r"tiny\.cloud"],
        "confidence": 90,
        "requires": 1,
    },
    "CKEditor": {
        "body": [r"ckeditor[/.-][\d.]+", r"CKEDITOR", r"ckeditor\.com"],
        "confidence": 90,
        "requires": 1,
    },
    "Draft.js": {
        "body": [r"draft-js", r"DraftEditor"],
        "confidence": 82,
        "requires": 1,
    },
    "Tiptap": {
        "body": [r"@tiptap", r"tiptap\.dev"],
        "confidence": 82,
        "requires": 1,
    },
    "Highlight.js": {
        "body": [r"highlight[/.-][\d.]+\.js", r"hljs\.highlightAll", r"highlightjs\.org"],
        "confidence": 88,
        "requires": 1,
    },
    "Prism.js": {
        "body": [r"prism[/.-][\d.]+", r"prismjs\.com"],
        "confidence": 88,
        "requires": 1,
    },
    "CodeMirror": {
        "body": [r"codemirror[/.-][\d.]+", r"CodeMirror\s*\("],
        "confidence": 88,
        "requires": 1,
    },
    "Monaco Editor": {
        "body": [r"monaco-editor", r"monaco\.editor"],
        "confidence": 88,
        "requires": 1,
    },
    "Ace Editor": {
        "body": [r"ace[/.-]builds", r"ace\.edit\s*\("],
        "confidence": 85,
        "requires": 1,
    },

    # Tables & Grids
    "DataTables": {
        "body": [r"datatables[/.-][\d.]+", r"DataTable\s*\(", r"datatables\.net"],
        "confidence": 92,
        "requires": 1,
    },
    "AG Grid": {
        "body": [r"ag-grid", r"agGrid"],
        "confidence": 88,
        "requires": 1,
    },
    "Tabulator": {
        "body": [r"tabulator[/.-]", r"Tabulator\s*\("],
        "confidence": 85,
        "requires": 1,
    },
    "Handsontable": {
        "body": [r"handsontable", r"Handsontable\s*\("],
        "confidence": 85,
        "requires": 1,
    },

    # Media
    "howler.js": {
        "body": [r"howler[/.-][\d.]+", r"new\s+Howl\s*\("],
        "confidence": 88,
        "requires": 1,
    },
    "Tone.js": {
        "body": [r"tone[/.-][\d.]+", r"Tone\.start"],
        "confidence": 82,
        "requires": 1,
    },
    "WaveSurfer": {
        "body": [r"wavesurfer[/.-]", r"WaveSurfer\.create"],
        "confidence": 88,
        "requires": 1,
    },
    "Video.js": {
        "body": [r"video[/.-][\d.]+\.js", r"videojs\s*\(", r"video-js"],
        "confidence": 90,
        "requires": 1,
    },
    "Plyr": {
        "body": [r"plyr[/.-][\d.]+", r"new\s+Plyr\s*\(", r"plyr\.css"],
        "confidence": 88,
        "requires": 1,
    },
    "hls.js": {
        "body": [r"hls[/.-][\d.]+\.js", r"Hls\.isSupported"],
        "confidence": 85,
        "requires": 1,
    },
    "dash.js": {
        "body": [r"dash[/.-][\d.]+\.js", r"dashjs"],
        "confidence": 82,
        "requires": 1,
    },

    # Misc
    "Socket.io": {
        "body": [r"socket\.io[/.-][\d.]+", r"socket\.io\.min\.js", r"io\s*\(\s*['\"]"],
        "confidence": 90,
        "requires": 1,
    },
    "Hammer.js": {
        "body": [r"hammer[/.-][\d.]+", r"Hammer\s*\("],
        "confidence": 82,
        "requires": 1,
    },
    "Modernizr": {
        "body": [r"modernizr[/.-][\d.]+", r"Modernizr\."],
        "confidence": 88,
        "requires": 1,
    },
    "Lazysizes": {
        "body": [r"lazysizes[/.-]", r"lazyload", r"lazysizes\.min\.js"],
        "confidence": 85,
        "requires": 1,
    },
    "lozad": {
        "body": [r"lozad[/.-]", r"lozad\.min\.js"],
        "confidence": 80,
        "requires": 1,
    },
    "Clipboard.js": {
        "body": [r"clipboard[/.-][\d.]+\.js", r"ClipboardJS"],
        "confidence": 85,
        "requires": 1,
    },
    "LocalForage": {
        "body": [r"localforage[/.-]", r"localforage\.min\.js"],
        "confidence": 82,
        "requires": 1,
    },
    "FullCalendar": {
        "body": [r"fullcalendar[/.-]", r"FullCalendar\.Calendar"],
        "confidence": 90,
        "requires": 1,
    },
    "Cropper.js": {
        "body": [r"cropper[/.-][\d.]+", r"new\s+Cropper\s*\("],
        "confidence": 85,
        "requires": 1,
    },
    "Sortable": {
        "body": [r"sortable[/.-][\d.]+", r"Sortable\.create", r"sortablejs\.com"],
        "confidence": 85,
        "requires": 1,
    },
    "dragula": {
        "body": [r"dragula[/.-][\d.]+", r"dragula\s*\("],
        "confidence": 82,
        "requires": 1,
    },
    "Handlebars": {
        "body": [r"handlebars[/.-][\d.]+", r"Handlebars\.compile"],
        "confidence": 88,
        "requires": 1,
    },
    "Mustache": {
        "body": [r"mustache[/.-][\d.]+", r"Mustache\.render"],
        "confidence": 85,
        "requires": 1,
    },
    "i18next": {
        "body": [r"i18next[/.-][\d.]+", r"i18next\.t\s*\("],
        "confidence": 85,
        "requires": 1,
    },
    "RequireJS": {
        "body": [r"require\.js", r"requirejs[/.-]", r"require\.config"],
        "confidence": 85,
        "requires": 1,
    },
    "SystemJS": {
        "body": [r"system\.js", r"System\.import"],
        "confidence": 82,
        "requires": 1,
    },
    "Babel Polyfill": {
        "body": [r"babel-polyfill", r"@babel/polyfill"],
        "confidence": 78,
        "requires": 1,
    },
    "core-js": {
        "body": [r"core-js[/.-][\d.]+"],
        "confidence": 78,
        "requires": 1,
    },
    "Polyfill.io": {
        "body": [r"polyfill\.io", r"cdn\.polyfill\.io"],
        "confidence": 88,
        "requires": 1,
    },
    "Twitter Emoji (Twemoji)": {
        "body": [r"twemoji", r"twemoji\.maxcdn", r"twemoji\.js", r"cdn\.jsdelivr\.net/npm/@twemoji"],
        "confidence": 92,
        "requires": 1,
    },
}
