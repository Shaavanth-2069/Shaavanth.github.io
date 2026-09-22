import os

ROOT = r"c:\Users\Lenovo\OneDrive\Desktop\html"
CSS_DIR = os.path.join(ROOT, "css")
JS_DIR = os.path.join(ROOT, "javascript")
os.makedirs(CSS_DIR, exist_ok=True)
os.makedirs(JS_DIR, exist_ok=True)

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

print(f"Generated {len(css_items)} CSS files with meaningful filenames.")
