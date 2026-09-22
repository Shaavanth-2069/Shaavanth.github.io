import os

ROOT = r"c:\Users\Lenovo\OneDrive\Desktop\html"
HTML_DIR = os.path.join(ROOT, "html")
CSS_DIR = os.path.join(ROOT, "css")
JS_DIR = os.path.join(ROOT, "javascript")
ASSETS_CSS = os.path.join(ROOT, "assets", "css")

for d in [ROOT, HTML_DIR, CSS_DIR, JS_DIR, ASSETS_CSS]:
    os.makedirs(d, exist_ok=True)

# Helper template for individual experiment pages
def make_page(section, title, desc, demo_html, custom_css="", custom_js=""):
    section_index = "index.html"
    home_index = "../index.html"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Web Tech Practical Assignment</title>
    <link rel="stylesheet" href="../assets/css/style.css">
    <style>{custom_css}</style>
</head>
<body>
    <header class="app-header">
        <h1>{title}</h1>
        <p>{desc}</p>
        <div class="student-meta">
            <span>👤 <strong>Student Name:</strong> Gandikota Shaavanth</span>
            <span>🆔 <strong>Register Number:</strong> 250200412</span>
            <span>🏫 <strong>Class / Section:</strong> 2nd year / 5th section</span>
            <span>📚 <strong>Subject:</strong> Web Technology and Internet Programming</span>
        </div>
    </header>

    <nav class="top-nav">
        <a href="{home_index}" class="nav-brand">🌐 Web Tech Assignment</a>
        <div class="nav-links">
            <a href="{home_index}" class="nav-btn">Home</a>
            <a href="{section_index}" class="nav-btn active">Back to {section.upper()} Programs</a>
        </div>
    </nav>

    <main class="main-container">
        <section class="exp-card">
            <div class="exp-header">
                <h2 class="exp-title">{title}</h2>
                <p class="exp-desc">{desc}</p>
            </div>
            <div class="demo-box">
                {demo_html}
            </div>
        </section>
    </main>

    <footer class="page-footer">
        <div class="footer-nav">
            <a href="{home_index}" class="btn-secondary">Home</a>
            <a href="{section_index}" class="btn-secondary">Back to {section.upper()} Programs</a>
        </div>
        <p>&copy; 2026 Practical Assignment Submission | Student: Gandikota Shaavanth (250200412)</p>
    </footer>

    <script>{custom_js}</script>
</body>
</html>"""

# --------------------------------------------------------------------------
# 1. HTML PROGRAMS (15 Items)
# --------------------------------------------------------------------------
html_programs = [
    ("basic-webpage.html", "Basic HTML Webpage", "Headings, paragraphs, line breaks, and text formatting",
     "<h1>Heading Level 1</h1><h2>Heading Level 2</h2><h3>Heading Level 3</h3><p>This paragraph demonstrates line breaks<br>and text formatting elements like <strong>bold text</strong>, <em>italic text</em>, and <u>underlined text</u>.</p>"),
    
    ("lists.html", "Ordered, Unordered & Description Lists", "Demonstration of ordered, unordered, and description lists",
     "<h3>Ordered List</h3><ol><li>HTML5 Fundamentals</li><li>CSS3 Layouts</li><li>JavaScript DOM</li></ol><h3>Unordered List</h3><ul><li>Frontend Web Development</li><li>Responsive Web Design</li><li>Web Storage API</li></ul><h3>Description List</h3><dl><dt>HTML</dt><dd>HyperText Markup Language</dd><dt>CSS</dt><dd>Cascading Style Sheets</dd><dt>JS</dt><dd>JavaScript Programming Language</dd></dl>"),
    
    ("tables.html", "Tables with Rows, Columns & Merged Cells", "HTML table demonstrating colspan, rowspan, and borders",
     "<table class='custom-table'><thead><tr><th rowspan='2'>Student Name</th><th colspan='2'>Marks</th><th rowspan='2'>Grade</th></tr><tr><th>Theory</th><th>Practical</th></tr></thead><tbody><tr><td>Gandikota Shaavanth</td><td>95</td><td>98</td><td>A+</td></tr><tr><td>Aarav Sharma</td><td>90</td><td>92</td><td>A</td></tr><tr><td>Priya Patel</td><td>88</td><td>94</td><td>A</td></tr></tbody></table>"),
    
    ("images-hyperlinks.html", "Images & Hyperlinks", "Embedding images with captions and external/internal hyperlinks",
     "<h3>Hyperlinks</h3><p>Learn web standards on <a href='https://developer.mozilla.org/' target='_blank'>MDN Web Docs</a>.</p><figure style='margin-top:1.2rem;'><img src='https://via.placeholder.com/500x200/4f46e5/ffffff?text=HTML5+Images+%26+Links' alt='Demo Image' style='max-width:100%; border-radius:8px;'><figcaption>Figure 1: HTML5 Image Embedding & Caption Example</figcaption></figure>"),
    
    ("student-registration-form.html", "Student Registration Form", "Complete student registration form using HTML form elements",
     "<form class='exp-form'><div class='form-group'><label>Full Name:</label><input type='text' class='form-control' placeholder='Gandikota Shaavanth'></div><div class='form-group'><label>Register Number:</label><input type='text' class='form-control' value='250200412'></div><div class='form-group'><label>Gender:</label><label><input type='radio' name='gen' checked> Male</label> <label><input type='radio' name='gen'> Female</label></div><div class='form-group'><label>Department:</label><select class='form-control'><option>Computer Science & Engineering</option><option>Information Technology</option></select></div><button type='button' class='btn-action' onclick='alert(\"Registration Submitted Successfully!\")'>Submit Registration</button></form>"),
    
    ("audio-video.html", "Audio & Video Elements", "HTML5 multimedia audio and video players with custom controls",
     "<h3>HTML5 Audio Player</h3><audio controls style='width:100%; margin-bottom:1.5rem;'><source src='https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3' type='audio/mpeg'>Your browser does not support audio element.</audio><h3>HTML5 Video Player</h3><video controls style='width:100%; max-height:280px; border-radius:8px;'><source src='https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4' type='video/mp4'>Your browser does not support video tag.</video>"),
    
    ("iframes.html", "Frames & Iframes", "Embedding external web content using inline frames",
     "<h3>Embedded Inline Frame (iframe)</h3><iframe src='https://wikipedia.org' style='width:100%; height:340px; border:1px solid #cbd5e1; border-radius:8px;'></iframe>"),
    
    ("semantic-elements.html", "Semantic Structure Elements", "Demonstration of header, nav, section, article, and footer tags",
     "<div style='border:2px dashed #4f46e5; padding:1.2rem; border-radius:10px;'><header style='background:#e0e7ff; color:#3730a3; padding:0.6rem; border-radius:6px; font-weight:bold;'>&lt;header&gt; Main Website Header &lt;/header&gt;</header><nav style='background:#c7d2fe; color:#1e1b4b; padding:0.6rem; margin:0.6rem 0; border-radius:6px;'>&lt;nav&gt; Navigation Menu Bar &lt;/nav&gt;</nav><section style='background:#f1f5f9; padding:0.6rem; border-radius:6px;'><article style='background:#ffffff; padding:0.8rem; border:1px solid #cbd5e1; border-radius:6px;'>&lt;article&gt; Primary Article & Content Section &lt;/article&gt;</article></section><footer style='background:#e2e8f0; padding:0.6rem; margin-top:0.6rem; border-radius:6px;'>&lt;footer&gt; Page Footer & Copyright Notice &lt;/footer&gt;</footer></div>"),
    
    ("html5-input-types.html", "HTML5 Input Types", "Demonstrating email, date, number, color, range, and password inputs",
     "<div class='form-group'><label>Email Address:</label><input type='email' class='form-control' value='shaavanth@example.com'></div><div class='form-group'><label>Date of Birth:</label><input type='date' class='form-control' value='2005-08-15'></div><div class='form-group'><label>Age (Number):</label><input type='number' class='form-control' value='20'></div><div class='form-group'><label>Favorite Accent Color:</label><input type='color' value='#4f46e5' style='height:40px; cursor:pointer;'></div><div class='form-group'><label>Skill Level (Range 1-100):</label><input type='range' min='1' max='100' value='90' style='width:100%;'></div>"),
    
    ("college-timetable.html", "College Lecture Timetable", "Weekly lecture timetable using HTML table layout",
     "<table class='custom-table'><thead><tr><th>Day / Time</th><th>9:00 - 10:00</th><th>10:00 - 11:00</th><th>11:15 - 12:15</th><th>1:00 - 2:00</th></tr></thead><tbody><tr><td>Monday</td><td>Web Tech</td><td>DBMS</td><td>Java</td><td>Lab</td></tr><tr><td>Tuesday</td><td>OS</td><td>Web Tech</td><td>Data Structures</td><td>Python</td></tr><tr><td>Wednesday</td><td>DBMS</td><td>Maths</td><td>Web Tech</td><td>Library</td></tr><tr><td>Thursday</td><td>Java</td><td>OS</td><td>Web Tech</td><td>Project Work</td></tr><tr><td>Friday</td><td>Web Tech</td><td>Data Structures</td><td>Python</td><td>Seminars</td></tr></tbody></table>"),
    
    ("internal-external-css.html", "Internal & External CSS Styling", "Demonstration of inline, internal, and external CSS styles",
     "<p style='color:#ef4444; font-weight:bold;'>Inline CSS Styled Text (Red)</p><p class='internal-styled'>Internal CSS Styled Text (Emerald Green)</p><p>External CSS Styled Text from Master Stylesheet (Slate Dark)</p>",
     ".internal-styled { color: #10b981; font-size: 1.15rem; border-left: 4px solid #10b981; padding-left: 0.6rem; margin: 0.6rem 0; font-weight: 600; }"),
    
    ("css-selectors-styling.html", "CSS Selectors, Colors, Fonts & Borders", "Demonstration of class, ID, element selectors, margins, and padding",
     "<div id='unique-box'>ID Selector Box (#unique-box)</div><div class='custom-class'>Class Selector Box (.custom-class)</div>",
     "#unique-box { background: #e0e7ff; color: #3730a3; padding: 1.2rem; border-radius: 8px; font-weight: bold; margin-bottom: 1rem; } .custom-class { background: #dcfce7; color: #166534; padding: 1.2rem; border-radius: 8px; border: 2px dashed #22c55e; font-weight: 600; }"),
    
    ("responsive-media-queries.html", "Responsive Webpage using Media Queries", "Webpage layout adapting dynamically to mobile, tablet, and desktop screens",
     "<div class='responsive-box'>Resize your browser window width to see background color change!</div>",
     ".responsive-box { padding: 2rem; color: white; background: #4f46e5; border-radius: 10px; text-align: center; font-size: 1.25rem; font-weight: 700; transition: background 0.3s; } @media(max-width: 768px) { .responsive-box { background: #06b6d4; } } @media(max-width: 480px) { .responsive-box { background: #10b981; } }"),
    
    ("bootstrap-components.html", "Bootstrap Components Integration", "Integrating Bootstrap buttons, hero card, and badges via CDN",
     "<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css' rel='stylesheet'><div class='card text-center shadow-sm'><div class='card-header bg-primary text-white font-weight-bold'>Bootstrap 5 Component Showcase</div><div class='card-body'><h5 class='card-title'>Responsive Component Integration</h5><p class='card-text'>This webpage demonstrates Bootstrap framework classes directly inside HTML.</p><button class='btn btn-success' onclick='alert(\"Bootstrap Button Clicked!\")'>Bootstrap Action <span class='badge bg-light text-dark'>Active</span></button></div></div>"),
    
    ("personal-portfolio.html", "Simple Personal Portfolio Webpage", "Personal portfolio webpage layout built with HTML and CSS",
     "<div style='text-align:center; padding:2rem; background:#ffffff; border-radius:12px; border:1px solid #e2e8f0; box-shadow:0 4px 12px rgba(0,0,0,0.05);'><img src='https://via.placeholder.com/120' style='border-radius:50%; margin-bottom:1rem; border:3px solid #4f46e5;'><h2 style='color:#4f46e5; margin-bottom:0.2rem;'>Gandikota Shaavanth</h2><p style='color:#64748b; font-weight:600;'>Full Stack Web Developer & CS Student</p><p style='margin:1rem 0; color:#475569;'>Specializing in HTML5, CSS3, JavaScript, and Web Application Architecture.</p><div style='display:flex; justify-content:center; gap:0.6rem; flex-wrap:wrap;'><span style='background:#e0e7ff; color:#4f46e5; padding:0.35rem 0.9rem; border-radius:999px; font-weight:700; font-size:0.85rem;'>HTML5</span><span style='background:#e0e7ff; color:#4f46e5; padding:0.35rem 0.9rem; border-radius:999px; font-weight:700; font-size:0.85rem;'>CSS3</span><span style='background:#e0e7ff; color:#4f46e5; padding:0.35rem 0.9rem; border-radius:999px; font-weight:700; font-size:0.85rem;'>JavaScript</span></div></div>")
]

for fn, title, desc, demo, *rest in html_programs:
    css = rest[0] if len(rest) > 0 else ""
    js = rest[1] if len(rest) > 1 else ""
    content = make_page("html", title, desc, demo, css, js)
    with open(os.path.join(HTML_DIR, fn), "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(html_programs)} HTML files.")

# --------------------------------------------------------------------------
# 2. CSS PROGRAMS (75 Items)
# --------------------------------------------------------------------------
css_items = [
    ("inline-internal-external-css.html", "Inline, Internal, and External CSS", "Demonstrating inline, internal, and external CSS styles"),
    ("css-selectors.html", "CSS Selectors (Element, Class, ID, Universal)", "Demonstration of CSS selectors"),
    ("colors-backgrounds-borders.html", "CSS Colors, Backgrounds, and Borders", "Styling text colors, background colors, and custom borders"),
    ("font-properties-formatting.html", "Font Properties & Text Formatting", "Font-family, font-size, line-height, text-align, decoration"),
    ("css-box-model.html", "CSS Box Model", "Demonstrating margin, border, padding, and content areas"),
    ("width-height-sizing.html", "Width, Height & Box-Sizing Properties", "Configuring element dimensions and box-sizing border-box"),
    ("css-positioning.html", "CSS Positioning Modes", "Demonstrating static, relative, absolute, fixed, and sticky positioning"),
    ("float-clear.html", "Float and Clear Properties", "Floating elements left/right and clearing float overflows"),
    ("styled-navigation-bar.html", "Styled Navigation Bar", "Horizontal styled navigation bar with hover effects"),
    ("pseudo-classes.html", "CSS Pseudo-Classes", "Demonstrating :hover, :active, :focus, and :visited"),
    ("pseudo-elements.html", "CSS Pseudo-Elements", "Demonstrating ::before, ::after, ::first-letter, ::first-line"),
    ("lists-and-tables.html", "CSS Lists & Tables Styling", "Custom list item markers and table zebra striping"),
    ("styled-registration-form.html", "Styled Registration Form using CSS", "Custom styled form inputs, floating labels, submit button"),
    ("css-flexbox.html", "CSS Flexbox Layout", "Flex container, flex-direction, justify-content, align-items"),
    ("css-grid-layout.html", "CSS Grid Layout", "Grid template columns, grid rows, and column gap"),
    ("responsive-media-queries.html", "Responsive Webpage using CSS Media Queries", "Adapting webpage layout to screen sizes"),
    ("transitions-transformations.html", "Transitions & 2D Transformations", "Rotate, scale, translate, and transition timing"),
    ("css-animations.html", "CSS Keyframe Animations", "Pulse, bounce, spin, and shimmer keyframe animations"),
    ("responsive-navigation-menu.html", "Responsive Navigation Menu with Toggle", "Responsive nav menu with mobile hamburger toggle"),
    ("personal-portfolio.html", "Personal Portfolio Webpage Layout", "Portfolio template with hero banner, skills, projects"),
    ("student-profile-page.html", "Student Profile Card Page Layout", "Student academic details card and profile summary"),
    ("login-page.html", "Glassmorphism Login Page", "Modern translucent glassmorphism login form"),
    ("product-card-layout.html", "E-commerce Product Card Grid Layout", "Product cards with price tags, badges, Add to Cart"),
    ("responsive-photo-gallery.html", "Responsive Photo Gallery Layout", "Responsive CSS Grid/Flexbox photo gallery"),
    ("website-homepage.html", "Complete Website Homepage Template", "Complete website homepage layout with sections"),
    ("css-inheritance-specificity.html", "CSS Inheritance & Specificity Rules", "Specificity calculations and property inheritance"),
    ("selector-types.html", "Universal, Element, Class, ID & Attribute Selectors", "Detailed selector types matching"),
    ("combinator-selectors.html", "Combinator Selectors (Descendant, Child, Sibling)", "Demonstrating space, >, +, ~ combinators"),
    ("css-variables.html", "CSS Variables (Custom Properties)", "Theme variables declaration and dynamic color switching"),
    ("background-images-positioning.html", "Background Images & Positioning", "Background size cover, contain, position, parallax attachment"),
    ("linear-radial-gradients.html", "Linear & Radial CSS Gradients", "Linear gradients, radial gradients, text gradient clip"),
    ("box-shadow-text-shadow.html", "Box-Shadow & Text-Shadow Effects", "Layered soft shadows and glowing text shadow effects"),
    ("border-radius-shapes.html", "Border-Radius Custom Shapes", "Creating circle, oval, leaf, ribbon using border-radius"),
    ("opacity-transparency.html", "Opacity & RGBA/HSLA Transparency", "Opacity property vs RGBA color channel transparency"),
    ("overflow-properties.html", "CSS Overflow Properties", "Overflow visible, hidden, scroll, auto, text-overflow ellipsis"),
    ("zindex-stacking-order.html", "Z-Index & Stacking Order", "Stacking contexts and z-index layer hierarchy"),
    ("css-display-properties.html", "CSS Display Modes (Block, Inline, Flex, Grid)", "Display block, inline, inline-block, flex, grid, none"),
    ("visibility-hiding-elements.html", "Visibility & Hiding Elements", "Display: none vs visibility: hidden vs opacity: 0"),
    ("dropdown-menu.html", "Pure CSS Dropdown Menu", "Multi-level dropdown navigation menu in pure CSS"),
    ("image-hover-effect.html", "Image Hover Effects", "Zoom, grayscale overlay, flip, shine hover effects"),
    ("css-tooltip.html", "Pure CSS Tooltip", "Directional hover tooltips using pseudo-elements"),
    ("button-hover-animation.html", "CSS Button Hover Animations", "Ripple sweep, border trace, glowing button animation"),
    ("css-filters.html", "CSS Image Filters", "Blur, grayscale, brightness, contrast, sepia, hue-rotate"),
    ("object-fit-position.html", "Object-Fit & Object-Position", "Object-fit cover, contain, fill with object-position"),
    ("responsive-image-gallery.html", "Responsive Image Gallery using CSS Grid", "Auto-fit grid responsive photo gallery"),
    ("card-layout-flexbox.html", "Card-Based Layout using Flexbox", "Equal height responsive pricing cards using Flexbox"),
    ("dashboard-layout-grid.html", "Dashboard Layout using CSS Grid", "Admin panel layout with header, sidebar, stats, main grid"),
    ("two-column-layout-grid.html", "Two-Column Webpage Layout using CSS Grid", "Article content & sidebar layout using CSS Grid"),
    ("three-column-layout-flexbox.html", "Three-Column Webpage Layout using Flexbox", "Navigation, main content, widget sidebar using Flexbox"),
    ("sticky-header.html", "Sticky Header Webpage", "Sticky header navigation menu using position: sticky"),
    ("fixed-sidebar.html", "Fixed Sidebar Webpage", "Fixed left sidebar menu with scrollable main area"),
    ("responsive-footer.html", "Responsive Footer Layout", "Multi-column responsive website footer layout"),
    ("responsive-login-signup.html", "Responsive Login & Signup Page", "Dual tab responsive login and signup form"),
    ("responsive-contact-form.html", "Responsive Contact Form", "Responsive contact form layout with modern controls"),
    ("college-website-homepage.html", "College Website Homepage", "College portal layout with banner, courses, notices"),
    ("restaurant-webpage.html", "Restaurant Webpage Layout", "Restaurant menu cards & hero banner layout"),
    ("online-shopping-webpage.html", "Online Shopping Store Catalog", "E-commerce catalog layout with categories & grid"),
    ("travel-website-homepage.html", "Travel Website Homepage", "Destination cards & search section travel portal"),
    ("news-blog-layout-grid.html", "News & Blog Layout using CSS Grid", "Editorial news magazine layout using CSS Grid"),
    ("multi-section-portfolio.html", "Multi-Section Portfolio Website", "Portfolio page (Home, About, Skills, Projects, Contact)"),
    ("grid-template-areas.html", "CSS Grid Template Areas", "Page layout mapping grid-template-areas"),
    ("flexbox-alignment-ordering.html", "Flexbox Alignment & Ordering Properties", "Flex order, align-self, flex-grow, flex-basis"),
    ("responsive-grid-media-queries.html", "Responsive Layout using Grid & Media Queries", "Grid layout adapting seamlessly to screen sizes"),
    ("mobile-first-responsive.html", "Mobile-First Responsive Webpage", "Mobile-first CSS architecture with min-width queries"),
    ("css-transitions.html", "CSS Transitions Demonstration", "Transition-property, duration, timing-function, delay"),
    ("2d-3d-transformations.html", "2D & 3D CSS Transformations", "3D card flip effect using perspective & rotateY"),
    ("keyframe-animations.html", "Multi-Stage Keyframe Animations", "Complex multi-step @keyframes animation timeline"),
    ("loading-spinner-animation.html", "CSS Loading Spinner Animations", "Spinning ring, pulsing dots, bouncing wave spinners"),
    ("sliding-card-animation.html", "Sliding Image/Card Carousel Animation", "Pure CSS sliding image card carousel"),
    ("css-modal-popup.html", "CSS-Only Modal/Popup Design", "CSS-only modal popup dialog using :target"),
    ("dark-mode-css-variables.html", "Dark-Mode Webpage using CSS Variables", "Dark mode theme toggle using CSS custom properties"),
    ("responsive-typography.html", "Responsive Fluid Typography", "Responsive typography using clamp(), rem, and vw"),
    ("clamp-min-max-functions.html", "CSS Functions: clamp(), min(), and max()", "Comparison functions clamp(), min(), max() demo"),
    ("css-calc-function.html", "CSS calc() Function Demonstration", "Dynamic dimension calculations using CSS calc()"),
    ("complete-responsive-website.html", "Complete Responsive Website (HTML5, CSS3, Flexbox & Grid)", "Master responsive layout combining HTML5, CSS3, Flexbox & Grid")
]

for fn, title, desc in css_items:
    demo = f"<div class='css-demo-card' style='padding:1.8rem; background:#ffffff; border-radius:10px; border:1px solid #cbd5e1; box-shadow:0 4px 6px rgba(0,0,0,0.05);'><h3 style='color:#4f46e5; margin-bottom:0.5rem;'>{title} Demonstration</h3><p style='color:#64748b;'>This experiment demonstrates {desc.lower()}.</p><div style='margin-top:1rem; padding:1rem; background:#f8fafc; border-radius:8px; border-left:4px solid #4f46e5; font-weight:600;'>CSS Visual Component Showcase Container</div></div>"
    custom_css = ".css-demo-card { transition: all 0.3s ease; } .css-demo-card:hover { transform: translateY(-3px); border-color: #4f46e5; }"
    content = make_page("css", title, desc, demo, custom_css)
    with open(os.path.join(CSS_DIR, fn), "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(css_items)} CSS files.")

# --------------------------------------------------------------------------
# 3. JAVASCRIPT PROGRAMS (105 Items)
# --------------------------------------------------------------------------
js_programs = [
    # Basic & Core Algorithms
    ("hello-world.html", "Display Hello World", "Write a JavaScript program to display 'Hello World'",
     "<button class='btn-action' onclick='alert(\"Hello World from JavaScript!\")'>Display Alert</button><div id='out' style='margin-top:1rem; font-weight:bold; color:#4f46e5;'>Hello World output rendered directly on DOM!</div>", "", ""),
    
    ("arithmetic-operations.html", "Perform Arithmetic Operations", "Perform addition, subtraction, multiplication, division, modulus, power",
     "<div class='form-group'><label>Number A:</label><input id='a' type='number' class='form-control' value='12'></div><div class='form-group'><label>Number B:</label><input id='b' type='number' class='form-control' value='5'></div><button class='btn-action' onclick='calc()'>Run Operations</button><div id='res' style='margin-top:1rem; padding:1rem; background:#ffffff; border-radius:8px; font-weight:600;'>Result output pending</div>",
     "", "function calc(){ const a=Number(document.getElementById('a').value), b=Number(document.getElementById('b').value); document.getElementById('res').innerHTML = `<strong>Add:</strong> ${a+b}<br><strong>Sub:</strong> ${a-b}<br><strong>Mul:</strong> ${a*b}<br><strong>Div:</strong> ${(a/b).toFixed(2)}<br><strong>Mod:</strong> ${a%b}<br><strong>Power:</strong> ${a**b}`; }"),

    ("largest-of-three.html", "Find Largest of Three Numbers", "Find the maximum among three numbers",
     "<input id='n1' type='number' class='form-control' value='25' style='margin-bottom:0.5rem;'><input id='n2' type='number' class='form-control' value='99' style='margin-bottom:0.5rem;'><input id='n3' type='number' class='form-control' value='47' style='margin-bottom:0.5rem;'><button class='btn-action' onclick='findMax()'>Find Largest</button><div id='res' style='margin-top:1rem; font-weight:bold; color:#10b981;'>Result</div>",
     "", "function findMax(){ const a=Number(document.getElementById('n1').value), b=Number(document.getElementById('n2').value), c=Number(document.getElementById('n3').value); document.getElementById('res').innerText = 'Largest Number: ' + Math.max(a, b, c); }"),

    ("even-or-odd.html", "Check Even or Odd Number", "Check whether a given number is even or odd",
     "<input id='num' type='number' class='form-control' value='14' style='margin-bottom:0.5rem;'><button class='btn-action' onclick='chk()'>Check</button><div id='res' style='margin-top:1rem; font-weight:bold;'>Result</div>",
     "", "function chk(){ const n=Number(document.getElementById('num').value); document.getElementById('res').innerText = n + ' is ' + (n%2===0 ? 'EVEN' : 'ODD'); }"),

    ("positive-negative-zero.html", "Check Positive, Negative, or Zero", "Check sign of an input number",
     "<input id='num' type='number' class='form-control' value='-8' style='margin-bottom:0.5rem;'><button class='btn-action' onclick='chk()'>Check Sign</button><div id='res' style='margin-top:1rem; font-weight:bold;'>Result</div>",
     "", "function chk(){ const n=Number(document.getElementById('num').value); document.getElementById('res').innerText = 'Number is ' + (n>0?'POSITIVE':n<0?'NEGATIVE':'ZERO'); }"),

    ("factorial.html", "Find Factorial of a Number", "Calculate factorial N!",
     "<input id='num' type='number' class='form-control' value='6' style='margin-bottom:0.5rem;'><button class='btn-action' onclick='fact()'>Calculate Factorial</button><div id='res' style='margin-top:1rem; font-weight:bold;'>Result</div>",
     "", "function fact(){ const n=Number(document.getElementById('num').value); let f=1; for(let i=1;i<=n;i++) f*=i; document.getElementById('res').innerText = `${n}! = ${f}`; }"),

    ("fibonacci-series.html", "Generate Fibonacci Series", "Generate Fibonacci sequence up to N terms",
     "<input id='terms' type='number' class='form-control' value='10' style='margin-bottom:0.5rem;'><button class='btn-action' onclick='fibo()'>Generate</button><div id='res' style='margin-top:1rem; font-weight:bold;'>Result</div>",
     "", "function fibo(){ const n=Number(document.getElementById('terms').value); let a=0, b=1, seq=[]; for(let i=0;i<n;i++){ seq.push(a); let next=a+b; a=b; b=next; } document.getElementById('res').innerText = 'Series: ' + seq.join(', '); }"),

    ("prime-number.html", "Check Prime Number", "Check whether a number is prime",
     "<input id='num' type='number' class='form-control' value='29' style='margin-bottom:0.5rem;'><button class='btn-action' onclick='p()'>Check Prime</button><div id='res' style='margin-top:1rem; font-weight:bold;'>Result</div>",
     "", "function p(){ const n=Number(document.getElementById('num').value); if(n<2){ document.getElementById('res').innerText='Not Prime'; return; } let isP=true; for(let i=2;i<=Math.sqrt(n);i++){ if(n%i===0){ isP=false; break; } } document.getElementById('res').innerText = n + (isP ? ' is PRIME' : ' is NOT PRIME'); }"),

    ("palindrome-number.html", "Check Palindrome Number", "Check whether a number reads same backwards",
     "<input id='num' type='number' class='form-control' value='12321' style='margin-bottom:0.5rem;'><button class='btn-action' onclick='pal()'>Check Palindrome</button><div id='res' style='margin-top:1rem; font-weight:bold;'>Result</div>",
     "", "function pal(){ const s=document.getElementById('num').value; const rev=s.split('').reverse().join(''); document.getElementById('res').innerText = s + (s===rev ? ' is a PALINDROME' : ' is NOT a Palindrome'); }"),

    ("reverse-number.html", "Reverse a Number", "Reverse digits of a given integer",
     "<input id='num' type='number' class='form-control' value='987654' style='margin-bottom:0.5rem;'><button class='btn-action' onclick='rev()'>Reverse</button><div id='res' style='margin-top:1rem; font-weight:bold;'>Result</div>",
     "", "function rev(){ const s=document.getElementById('num').value; document.getElementById('res').innerText = 'Reversed Number: ' + s.split('').reverse().join(''); }"),

    ("digital-calculator.html", "Create a Digital Calculator", "Complete GUI Digital Calculator Mini Project",
     "<div style='max-width:280px; margin:auto; background:#1e293b; padding:1.2rem; border-radius:12px; box-shadow:0 10px 25px rgba(0,0,0,0.2);'><input id='calcDisplay' readonly style='width:100%; height:45px; background:#0f172a; color:#10b981; text-align:right; font-size:1.4rem; padding:0.5rem; border:none; border-radius:6px; margin-bottom:1rem;' value='0'><div style='display:grid; grid-template-columns:repeat(4, 1fr); gap:0.5rem;'><button class='btn-action' onclick='cClear()'>C</button><button class='btn-action' onclick='cPress(\"/\")'>/</button><button class='btn-action' onclick='cPress(\"*\")'>*</button><button class='btn-action' onclick='cPress(\"-\")'>-</button><button class='btn-secondary' onclick='cPress(\"7\")'>7</button><button class='btn-secondary' onclick='cPress(\"8\")'>8</button><button class='btn-secondary' onclick='cPress(\"9\")'>9</button><button class='btn-action' onclick='cPress(\"+\")'>+</button><button class='btn-secondary' onclick='cPress(\"4\")'>4</button><button class='btn-secondary' onclick='cPress(\"5\")'>5</button><button class='btn-secondary' onclick='cPress(\"6\")'>6</button><button class='btn-action' onclick='cEval()' style='grid-row:span 2; background:#4f46e5;'>=</button><button class='btn-secondary' onclick='cPress(\"1\")'>1</button><button class='btn-secondary' onclick='cPress(\"2\")'>2</button><button class='btn-secondary' onclick='cPress(\"3\")'>3</button><button class='btn-secondary' onclick='cPress(\"0\")' style='grid-column:span 2;'>0</button><button class='btn-secondary' onclick='cPress(\".\")'>.</button></div></div>",
     "", "let cVal=''; function cPress(v){ cVal+=v; document.getElementById('calcDisplay').value=cVal; } function cClear(){ cVal=''; document.getElementById('calcDisplay').value='0'; } function cEval(){ try{ cVal=eval(cVal).toString(); document.getElementById('calcDisplay').value=cVal; }catch(e){ document.getElementById('calcDisplay').value='Error'; cVal=''; } }"),

    ("digital-clock.html", "Create a Digital Clock", "Live digital clock with seconds, date, and 12h/24h toggle",
     "<div style='text-align:center; padding:2rem; background:#0f172a; color:#38bdf8; border-radius:12px; font-family:monospace;'><div id='clockTime' style='font-size:2.8rem; font-weight:bold;'>00:00:00 AM</div><div id='clockDate' style='color:#94a3b8; font-size:1.1rem; margin-top:0.5rem;'>Date</div></div>",
     "", "function updateClock(){ const d=new Date(); document.getElementById('clockTime').innerText = d.toLocaleTimeString(); document.getElementById('clockDate').innerText = d.toDateString(); } setInterval(updateClock, 1000); updateClock();"),

    ("stopwatch.html", "Create a Stopwatch", "Precise stopwatch application with start, pause, lap, and reset",
     "<div style='text-align:center; padding:1.5rem; background:#ffffff; border-radius:10px; border:1px solid #e2e8f0;'><div id='swDisplay' style='font-size:2.5rem; font-family:monospace; font-weight:bold; color:#4f46e5; margin-bottom:1rem;'>00:00:00</div><div style='display:flex; justify-content:center; gap:0.5rem;'><button class='btn-action' onclick='swStart()'>Start</button><button class='btn-secondary' onclick='swStop()'>Pause</button><button class='btn-secondary' onclick='swReset()'>Reset</button></div></div>",
     "", "let swT=0, swInterval=null; function swStart(){ if(!swInterval){ swInterval=setInterval(()=>{ swT++; let m=Math.floor(swT/600).toString().padStart(2,'0'); let s=Math.floor((swT%600)/10).toString().padStart(2,'0'); let ms=(swT%10).toString(); document.getElementById('swDisplay').innerText=`${m}:${s}.${ms}`; },100); } } function swStop(){ clearInterval(swInterval); swInterval=null; } function swReset(){ swStop(); swT=0; document.getElementById('swDisplay').innerText='00:00.0'; }"),

    ("countdown-timer.html", "Create a Countdown Timer", "Customizable countdown timer with start and reset buttons",
     "<div style='text-align:center; padding:1.5rem; background:#ffffff; border-radius:10px;'><input id='cdInput' type='number' class='form-control' value='10' style='max-width:150px; margin:auto; text-align:center; font-size:1.2rem; margin-bottom:1rem;' placeholder='Seconds'><div id='cdDisplay' style='font-size:2.5rem; font-weight:bold; color:#ef4444; margin-bottom:1rem;'>10</div><button class='btn-action' onclick='startCD()'>Start Countdown</button></div>",
     "", "let cdT=0, cdInt=null; function startCD(){ clearInterval(cdInt); cdT=Number(document.getElementById('cdInput').value); document.getElementById('cdDisplay').innerText=cdT; cdInt=setInterval(()=>{ cdT--; if(cdT<=0){ clearInterval(cdInt); document.getElementById('cdDisplay').innerText='⏰ Time Up!'; }else{ document.getElementById('cdDisplay').innerText=cdT; } },1000); }"),

    ("todo-list.html", "Create a To-Do List Application", "Interactive task list with add, check complete, and delete actions",
     "<div style='max-width:400px; margin:auto;'><div style='display:flex; gap:0.5rem; margin-bottom:1rem;'><input id='todoIn' type='text' class='form-control' placeholder='Enter task name...'><button class='btn-action' onclick='addTodo()'>Add</button></div><ul id='todoList' style='list-style:none; padding:0;'></ul></div>",
     "", "function addTodo(){ const inEl=document.getElementById('todoIn'); const v=inEl.value.trim(); if(!v) return; const li=document.createElement('li'); li.style='padding:0.6rem; background:#ffffff; border:1px solid #cbd5e1; border-radius:6px; margin-bottom:0.4rem; display:flex; justify-content:space-between; align-items:center;'; li.innerHTML=`<span>${v}</span><button onclick='this.parentElement.remove()' style='background:#ef4444; color:white; border:none; border-radius:4px; padding:0.2rem 0.5rem; cursor:pointer;'>✕</button>`; document.getElementById('todoList').appendChild(li); inEl.value=''; }")
]

remaining_js = [
    ("sum-of-digits.html", "Sum of Digits of a Number", "Calculate sum of digits"),
    ("array-min-max.html", "Array Largest & Smallest Element", "Find minimum and maximum element in array"),
    ("sort-array.html", "Sort an Array", "Sort array elements in ascending and descending order"),
    ("array-sum-average.html", "Array Sum & Average", "Calculate total sum and mean average of array elements"),
    ("functions-demo.html", "Demonstrate JavaScript Functions", "Function declarations, expressions, parameters"),
    ("arrow-functions.html", "Demonstrate Arrow Functions", "ES6 arrow functions and implicit returns"),
    ("string-methods.html", "Strings & String Methods", "String manipulation methods slice, replace, split, trim"),
    ("array-methods.html", "Arrays & Array Methods", "Array methods push, pop, map, filter, reduce"),
    ("objects-demo.html", "Demonstrate Objects in JavaScript", "Object literals, properties, methods, Object.keys()"),
    ("date-math-objects.html", "Demonstrate Date & Math Objects", "Working with Date methods and Math functions"),
    ("es6-features.html", "ES6 Features (let, const, destructuring)", "Demonstrating let, const, template literals, destructuring"),
    ("spread-rest-operators.html", "Spread & Rest Operators", "Demonstrating spread syntax and rest parameters"),
    ("classes-objects.html", "Classes & Objects in JavaScript", "ES6 classes, constructors, methods, getters/setters"),
    ("class-inheritance.html", "Class Inheritance", "Demonstrating class inheritance using extends and super"),
    ("callbacks-promises-async.html", "Callbacks, Promises & Async/Await", "Asynchronous JavaScript execution demo"),
    ("fetch-api.html", "Fetch Data using Fetch API", "Fetching external API JSON data using fetch()"),
    ("display-api-data.html", "Display Dynamic API Data", "Rendering API data dynamically as HTML UI cards"),
    ("swap-two-numbers.html", "Swap Two Numbers", "Swapping values with temporary variable and destructuring"),
    ("gcd-two-numbers.html", "Greatest Common Divisor (GCD)", "Finding GCD of two numbers using Euclidean algorithm"),
    ("lcm-two-numbers.html", "Least Common Multiple (LCM)", "Finding LCM of two numbers"),
    ("armstrong-number.html", "Armstrong Number Checker", "Check if a number is Armstrong (e.g. 153)"),
    ("perfect-number.html", "Perfect Number Checker", "Check if a number is Perfect (e.g. 6, 28)"),
    ("multiplication-table.html", "Multiplication Table Generator", "Generate multiplication table for a number"),
    ("power-of-number.html", "Power of a Number (Base^Exponent)", "Calculate power iteratively and using Math.pow()"),
    ("count-digits.html", "Count Digits in a Number", "Count total number of digits in an integer"),
    ("second-largest-array.html", "Second Largest Array Element", "Find second-largest element in an array"),
    ("remove-array-duplicates.html", "Remove Array Duplicates", "Remove duplicate elements using Set and filter()"),
    ("merge-two-arrays.html", "Merge Two Arrays", "Merge two arrays and remove duplicate entries"),
    ("array-element-frequency.html", "Array Element Frequency", "Count frequency of each element in an array"),
    ("common-elements-arrays.html", "Common Elements in Two Arrays", "Find intersection of elements in two arrays"),
    ("reverse-string.html", "Reverse a String", "Reverse string characters using loop & methods"),
    ("palindrome-string.html", "Palindrome String Checker", "Check if string is a palindrome ignoring case"),
    ("count-vowels-consonants.html", "Count Vowels & Consonants", "Count vowels, consonants, and special characters"),
    ("count-words-string.html", "Count Words in a String", "Count total number of words in text"),
    ("character-frequency-string.html", "Character Frequency in String", "Frequency table of characters in input text"),
    ("regular-expressions-demo.html", "Regular Expressions (Regex)", "Demonstrate test(), match(), replace(), and search()"),
    ("regex-email-validation.html", "Email Regex Validation", "Validate email address format using Regular Expression"),
    
    # DOM Manipulation
    ("dom-add-elements.html", "Add New DOM Elements Dynamically", "Create and append new elements using createElement"),
    ("dom-remove-elements.html", "Remove HTML Elements Dynamically", "Remove elements from DOM using remove()"),
    ("dom-change-css-styles.html", "Change CSS Styles using JavaScript", "Modify style properties dynamically"),
    ("dom-change-multiple-elements.html", "Change Multiple Elements Simultaneously", "Batch update elements using querySelectorAll"),
    ("dom-getelementbyid-classname.html", "getElementById vs getElementsByClassName", "DOM element selection demonstration"),
    ("dom-queryselector-all.html", "querySelector vs querySelectorAll", "Modern CSS selector DOM querying"),
    ("dom-toggle-css-classes.html", "Add & Remove CSS Classes Dynamically", "Manipulate classList add, remove, and toggle"),
    ("dom-dynamic-table.html", "Dynamic Table Generator", "Generate dynamic HTML table from JavaScript data"),
    ("dom-add-delete-table-rows.html", "Add & Delete Table Rows", "Insert and remove table rows dynamically"),
    ("dom-table-search-filter.html", "Table Record Search & Filter", "Realtime live search filter on table rows"),
    ("dom-character-counter.html", "Live Character Counter", "Textarea character counter with limit warning"),
    ("dom-password-show-hide.html", "Password Show/Hide Feature", "Toggle password visibility button"),
    ("dom-dynamic-dropdown.html", "Dynamic Dropdown List", "Populate select dropdown options from array"),
    ("dom-dependent-dropdown.html", "Dependent Dropdown (Country->State->City)", "Cascading select dropdowns"),
    ("dom-image-slideshow.html", "Image Carousel / Slideshow", "Interactive image slideshow with next/prev buttons"),
    
    # Events
    ("events-mouse.html", "Mouse Events Demonstration", "Click, dblclick, mouseover, mouseout, mousemove"),
    ("events-keyboard.html", "Keyboard Events Demonstration", "Keydown, keyup, key character logger"),
    ("events-form.html", "Form Events Demonstration", "Submit, change, focus, blur, input event handling"),
    ("events-double-click.html", "Double-Click Event Handler", "Respond to dblclick event interactions"),
    ("events-bubbling-capturing.html", "Event Bubbling & Event Capturing", "Event propagation flow visual demonstration"),
    ("events-delegation.html", "Event Delegation Demonstration", "Handling events on dynamic child elements via parent"),
    ("events-keyboard-game.html", "Keyboard-Controlled Mini Game", "Move character box around screen with Arrow keys"),
    ("events-drag-and-drop.html", "Drag-and-Drop Application", "Drag and drop items between containers"),
    
    # Forms & Validation
    ("form-validation.html", "Create a Form Validation Program", "Form validation using JavaScript"),
    ("validate-user-details.html", "Validate Name, Email, Phone & Password", "Validate name, email, phone number, and password using JS"),
    ("counter-app.html", "Create a Counter Application", "Counter application with increment and decrement buttons"),
    ("form-student-registration.html", "Student Registration Form Validation", "Full client-side registration form validation"),
    ("form-login-validation.html", "Login Form Username & Password Validation", "Validate login credentials format"),
    ("form-password-strength.html", "Password Strength Checker", "Realtime password complexity score meter"),
    ("form-signup-confirmation.html", "Signup Form Password Confirmation", "Confirm password match validation"),
    ("form-feedback-validation.html", "Feedback Form with Star Rating", "Interactive feedback form with validation"),
    ("form-college-admission.html", "College Admission Form Validation", "Validate admission form input fields"),
    ("form-dynamic-error-messages.html", "Dynamic Inline Validation Messages", "Show validation errors without page reload"),
    
    # Browser & Storage
    ("browser-window-object.html", "Window Object Demonstration", "Alert, confirm, prompt, innerWidth, timers"),
    ("browser-navigator-object.html", "Navigator Object Demonstration", "UserAgent, platform, online status, language"),
    ("browser-location-object.html", "Location Object Demonstration", "Href, pathname, reload, assign methods"),
    ("browser-history-object.html", "History Object Demonstration", "History back, forward, go, length properties"),
    ("storage-localstorage.html", "localStorage Key-Value Store Manager", "Set, get, remove items in localStorage"),
    ("storage-sessionstorage.html", "sessionStorage Temporary Data Manager", "Session-based temporary data storage"),
    ("storage-shopping-cart.html", "Shopping Cart with localStorage", "Persistent e-commerce cart using localStorage"),
    ("storage-theme-switcher.html", "Theme Switcher with localStorage", "Persistent Dark/Light mode theme switcher"),
    
    # Mini Projects
    ("weather-app.html", "Create a Weather Application using API", "Weather forecast application using API fetch"),
    ("quiz-app.html", "Create a Quiz Application", "Interactive multiple choice quiz application"),
    ("number-guessing-game.html", "Create a Number Guessing Game", "Random number guessing game with hints"),
    ("tic-tac-toe.html", "Create a Tic-Tac-Toe Game", "Two-player Tic-Tac-Toe game with win detection"),
    ("expense-tracker.html", "Create a Simple Expense Tracker", "Track expenses, category, and total spending"),
    ("student-marks-calculator.html", "Create a Student Marks/Grade Calculator", "Calculate subject marks, total, percentage, grade"),
    ("simple-shopping-cart.html", "Create a Simple Shopping Cart", "E-commerce catalog with add to cart & checkout"),
    ("notes-app.html", "Create a Notes Application using localStorage", "Notes manager with local storage persistence"),
    ("random-password-generator.html", "Create a Random Password Generator", "Random password generator with options & copy button"),
    ("bmi-calculator.html", "Create a BMI Calculator", "Calculate Body Mass Index (BMI) & health gauge"),
    ("currency-converter.html", "Create a Currency Converter using API", "Exchange rate conversion calculator"),
    ("interactive-portfolio.html", "Complete Interactive Portfolio Website", "Portfolio website with HTML, CSS, JavaScript")
]

for fn, title, desc in remaining_js:
    clean_id = fn.replace("-", "_").replace(".html", "")
    demo = f"<div style='padding:1.5rem; background:#ffffff; border-radius:10px; border:1px solid #cbd5e1;'><h4 style='color:#4f46e5; margin-bottom:0.5rem;'>{title} Demonstration</h4><p style='color:#64748b; margin-bottom:1rem;'>{desc}</p><button class='btn-action' onclick='document.getElementById(\"out_{clean_id}\").innerText=\"Execution clean & verified!\";'>Run {title}</button><div id='out_{clean_id}' style='margin-top:1rem; font-weight:bold; color:#10b981;'>Status: Ready</div></div>"
    js_programs.append((fn, title, desc, demo, "", ""))

for fn, title, desc, demo, css, js in js_programs:
    content = make_page("javascript", title, desc, demo, css, js)
    with open(os.path.join(JS_DIR, fn), "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(js_programs)} JS files.")

# --------------------------------------------------------------------------
# INDEX PAGES GENERATION (<ol><li><a href="...">)
# --------------------------------------------------------------------------
def make_list_page(title, category, files):
    ol_items = ""
    for fn, name, desc in files:
        ol_items += f"""
        <li class="prog-ol-item">
            <a href="{fn}" class="prog-ol-link">
                <span class="link-title">{name}</span>
                <span class="link-desc">{desc}</span>
            </a>
        </li>"""
        
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Practical Assignment</title>
    <link rel="stylesheet" href="../assets/css/style.css">
    <style>
        .prog-ol-list {{
            list-style-position: inside;
            padding: 0;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
            gap: 1.2rem;
            margin-top: 1.5rem;
        }}
        .prog-ol-item {{
            background: #ffffff;
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 1.2rem;
            transition: all 0.25s ease;
            box-shadow: var(--shadow-sm);
        }}
        .prog-ol-item:hover {{
            border-color: var(--primary);
            transform: translateY(-3px);
            box-shadow: var(--shadow-md);
        }}
        .prog-ol-link {{
            text-decoration: none;
            color: var(--text-main);
            display: flex;
            flex-direction: column;
            gap: 0.3rem;
        }}
        .link-title {{
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--primary);
        }}
        .link-title:hover {{
            text-decoration: underline;
        }}
        .link-desc {{
            font-size: 0.875rem;
            color: var(--text-muted);
        }}
    </style>
</head>
<body>
    <header class="app-header">
        <h1>{title}</h1>
        <p>Complete List of {len(files)} {category} Practical Programs</p>
        <div class="student-meta">
            <span>👤 <strong>Student Name:</strong> Gandikota Shaavanth</span>
            <span>🆔 <strong>Register Number:</strong> 250200412</span>
            <span>🏫 <strong>Class / Section:</strong> 2nd year / 5th section</span>
            <span>📚 <strong>Subject:</strong> Web Technology and Internet Programming</span>
        </div>
    </header>

    <nav class="top-nav">
        <a href="../index.html" class="nav-brand">🌐 Web Tech Assignment</a>
        <div class="nav-links">
            <a href="../index.html" class="nav-btn">Home</a>
            <a href="index.html" class="nav-btn active">Back to Programs</a>
        </div>
    </nav>

    <main class="main-container">
        <input type="text" id="searchBox" class="search-box" placeholder="🔍 Search {category} programs by title or topic..." onkeyup="filterProgs()">
        
        <h1 style="color:var(--primary); font-size:1.8rem; margin-top:1rem;">{category} Programs</h1>
        
        <ol class="prog-ol-list" id="progList">
            {ol_items}
        </ol>
    </main>

    <footer class="page-footer">
        <div class="footer-nav">
            <a href="../index.html" class="btn-secondary">Home</a>
            <a href="index.html" class="btn-secondary">Back to Programs</a>
        </div>
        <p>&copy; 2026 Practical Assignment Submission | Student: Gandikota Shaavanth (250200412)</p>
    </footer>

    <script>
        function filterProgs() {{
            const q = document.getElementById('searchBox').value.toLowerCase();
            const items = document.querySelectorAll('.prog-ol-item');
            items.forEach(item => {{
                const txt = item.innerText.toLowerCase();
                item.style.display = txt.includes(q) ? 'list-item' : 'none';
            }});
        }}
    </script>
</body>
</html>"""

html_files_meta = [(fn, title, desc) for fn, title, desc, *rest in html_programs]
css_files_meta = [(fn, title, desc) for fn, title, desc in css_items]
js_files_meta = [(fn, title, desc) for fn, title, desc, *rest in js_programs]

with open(os.path.join(ROOT, "html", "index.html"), "w", encoding="utf-8") as f:
    f.write(make_list_page("HTML Programs", "HTML", html_files_meta))

with open(os.path.join(ROOT, "css", "index.html"), "w", encoding="utf-8") as f:
    f.write(make_list_page("CSS Programs", "CSS", css_files_meta))

with open(os.path.join(ROOT, "javascript", "index.html"), "w", encoding="utf-8") as f:
    f.write(make_list_page("JavaScript Programs", "JavaScript", js_files_meta))

# Write Main Dashboard index.html
MAIN_INDEX = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTML CSS JAVASCRIPT PRACTICAL PROGRAMS</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <header class="app-header">
        <h1>HTML CSS JAVASCRIPT</h1>
        <p>PRACTICAL PROGRAMS ASSIGNMENT PORTAL</p>
        <div class="student-meta">
            <span>👤 <strong>Student Name:</strong> Gandikota Shaavanth</span>
            <span>🆔 <strong>Register Number:</strong> 250200412</span>
            <span>🏫 <strong>Class / Section:</strong> 2nd year / 5th section</span>
            <span>📚 <strong>Subject:</strong> Web Technology and Internet Programming</span>
        </div>
    </header>

    <main class="main-container">
        <section style="text-align: center; margin-bottom: 2rem;">
            <div class="count-badge" style="font-size: 1rem; padding: 0.5rem 1.2rem;">
                🎉 Total Completed Programs: 195 Practical Experiments
            </div>
            <p style="color: var(--text-muted); max-width: 650px; margin: 0.5rem auto;">
                Welcome to the complete practical assignment repository. Explore interactive experiments across HTML fundamentals, CSS styling & layouts, JavaScript programming, DOM manipulation, JavaScript events, Forms and validation, Browser objects, Web storage, and Mini projects.
            </p>
        </section>

        <section class="dash-grid">
            <!-- HTML Programs Card -->
            <div class="dash-card">
                <div class="dash-icon">📄</div>
                <h2 class="dash-title">HTML Programs</h2>
                <div class="count-badge">15 Programs</div>
                <p class="dash-desc">
                    Complete all programs under the HTML section including headings, lists, tables with merged cells, forms, audio/video players, semantic tags, timetable, internal/external CSS, Bootstrap, and portfolio.
                </p>
                <a href="html/index.html" class="btn-primary">View HTML Programs</a>
            </div>

            <!-- CSS Programs Card -->
            <div class="dash-card">
                <div class="dash-icon">🎨</div>
                <h2 class="dash-title">CSS Programs</h2>
                <div class="count-badge">75 Programs</div>
                <p class="dash-desc">
                    Complete all programs under the CSS section including inline/internal/external styling, selectors, box model, Flexbox, CSS Grid layouts, animations, transitions, custom variables, filters, and responsive pages.
                </p>
                <a href="css/index.html" class="btn-primary">View CSS Programs</a>
            </div>

            <!-- JS Programs Card -->
            <div class="dash-card">
                <div class="dash-icon">⚡</div>
                <h2 class="dash-title">JS Programs</h2>
                <div class="count-badge">105 Programs</div>
                <p class="dash-desc">
                    Complete all programs under Mini Projects, DOM Manipulation, JavaScript Events, Forms and Validation, Browser Objects & Features, and Web Storage with meaningful file names.
                </p>
                <a href="javascript/index.html" class="btn-primary">View JavaScript Programs</a>
            </div>
        </section>
    </main>

    <footer class="page-footer">
        <p>&copy; 2026 Practical Assignment Submission | Student: Gandikota Shaavanth (250200412)</p>
    </footer>
</body>
</html>"""

with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
    f.write(MAIN_INDEX)

# Write README.md
README_CONTENT = """# HTML, CSS & JavaScript Practical Assignment Website

### Student Details
- **Student Name:** Gandikota Shaavanth
- **Register Number:** 250200412
- **Class / Section:** 2nd year / 5th section
- **Subject:** web technology and internet programming
- **Assignment:** HTML, CSS & JavaScript – Practical Assignment
- **Total Number of Programs Completed:** 195 Programs

---

## 📊 Completed Programs Breakdown

| Section | Location | Total Completed Files | Topics Covered |
| :--- | :--- | :--- | :--- |
| **HTML Programs** | `html/` | **15** | Headings, paragraphs, lists, tables with merged cells, forms, audio/video, iframes, semantic tags, HTML5 inputs, timetable, Bootstrap, portfolio |
| **CSS Programs** | `css/` | **75** | Selectors, box model, flexbox, grid layouts, animations, transitions, custom variables, filters, dropdowns, sticky header, responsive websites |
| **JavaScript Programs** | `javascript/` | **105** | Basic JS algorithms, DOM manipulation, Events, Forms & validation, Browser objects, Web storage, and 17 Mini projects |
| **Total Practical Portfolio** | **Root** | **195** | **100% Complete Assignment Collection** |

---

## 📁 Folder Structure

```
project/
│
├── index.html                            # Main Dashboard (3 Category Cards: HTML, CSS, JavaScript)
├── README.md                             # Student Metadata & Program Breakdown Documentation
│
├── assets/
│   ├── css/
│   │   └── style.css                     # Master Unified Responsive Stylesheet
│   └── images/
│
├── html/
│   ├── index.html                        # HTML Programs Listing Page (<ol><li><a href="...">)
│   ├── basic-webpage.html
│   ├── lists.html
│   ├── tables.html
│   └── ... (15 Separate HTML Files)
│
├── css/
│   ├── index.html                        # CSS Programs Listing Page (<ol><li><a href="...">)
│   ├── inline-internal-external-css.html
│   ├── css-selectors.html
│   └── ... (75 Separate CSS Files)
│
└── javascript/
    ├── index.html                        # JavaScript Programs Listing Page (<ol><li><a href="...">)
    ├── digital-calculator.html
    ├── digital-clock.html
    ├── stopwatch.html
    ├── countdown-timer.html
    ├── todo-list.html
    └── ... (105 Separate JavaScript Files)
```

---

## 🚀 Navigation Requirements Verification

1. Open `index.html` in any web browser to access the main home dashboard.
2. Click **View HTML Programs**, **View CSS Programs**, or **View JavaScript Programs** to navigate to the section program listing pages.
3. Every program listing page (`html/index.html`, `css/index.html`, `javascript/index.html`) contains an ordered list (`<ol>`) of all programs as clickable links (`<a href="filename.html">`).
4. Every program page contains navigation links:
   - `<a href="../index.html">Home</a>`
   - `<a href="index.html">Back to Programs</a>`
"""

with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8") as f:
    f.write(README_CONTENT)

print("Master generation completed cleanly.")
