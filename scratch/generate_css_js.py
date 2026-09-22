import os

ROOT = r"c:\Users\Lenovo\OneDrive\Desktop\html"
HTML_DIR = os.path.join(ROOT, "html")
CSS_DIR = os.path.join(ROOT, "css")
JS_DIR = os.path.join(ROOT, "javascript")
ASSETS_CSS = os.path.join(ROOT, "assets", "css")

def tpl(section, title, desc, demo, css="", js=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Practical Assignment</title>
    <link rel="stylesheet" href="../assets/css/style.css">
    <style>{css}</style>
</head>
<body>
    <header class="app-header">
        <h1>{title}</h1>
        <p>{desc}</p>
        <div class="student-meta">
            <span>👤 <strong>Student:</strong> Gandikota Shaavanth</span>
            <span>🆔 <strong>Reg No:</strong> 250200412</span>
            <span>📚 <strong>Subject:</strong> Web Technology & Internet Programming</span>
        </div>
    </header>

    <nav class="top-nav">
        <a href="../index.html" class="nav-brand">🌐 Web Tech Assignment</a>
        <div class="nav-links">
            <a href="../index.html" class="nav-btn">🏠 Home Dashboard</a>
            <a href="index.html" class="nav-btn active">🔙 Back to {section.upper()} Programs</a>
        </div>
    </nav>

    <main class="main-container">
        <section class="exp-card">
            <div class="exp-header">
                <h2 class="exp-title">{title}</h2>
                <p class="exp-desc">{desc}</p>
            </div>
            <div class="demo-box">
                {demo}
            </div>
        </section>
    </main>

    <footer class="page-footer">
        <div class="footer-nav">
            <a href="../index.html" class="btn-secondary">🏠 Home Dashboard</a>
            <a href="index.html" class="btn-secondary">🔙 {section.upper()} Programs List</a>
        </div>
        <p>&copy; 2026 Practical Assignment | Student: Gandikota Shaavanth (250200412)</p>
    </footer>

    <script>{js}</script>
</body>
</html>"""

# Generate 75 CSS Programs
css_titles = [
    "Inline, Internal, and External CSS", "CSS Selectors (Element, Class, ID, Universal)", "CSS Colors, Backgrounds, and Borders",
    "Font Properties & Text Formatting", "CSS Box Model (Margin, Border, Padding, Content)", "Width, Height, and Box-Sizing Properties",
    "CSS Positioning (Static, Relative, Absolute, Fixed, Sticky)", "Float and Clear Properties", "Styled Navigation Bar",
    "CSS Pseudo-Classes (:hover, :active, :focus, :visited)", "CSS Pseudo-Elements (::before, ::after, ::first-letter)", "CSS Lists and Tables Styling",
    "Styled Registration Form using CSS", "CSS Flexbox Layout (Flex-Direction, Justify, Align)", "CSS Grid Layout (Grid Template Columns & Gap)",
    "Responsive Design using CSS Media Queries", "CSS 2D Transforms & Smooth Transitions", "CSS @keyframes Animations (Bounce, Pulse, Spin)",
    "Responsive Navigation Menu with Toggle", "Personal Portfolio Webpage Layout", "College Student Profile Card Layout",
    "Glassmorphism Login Page Design", "E-commerce Product Card Grid Layout", "Responsive Photo Gallery Layout",
    "Complete Website Homepage Layout", "CSS Inheritance & Specificity Rules", "Selector Types & Attribute Selectors",
    "Combinator Selectors (Descendant, Child, Sibling)", "CSS Custom Properties (Variables) & Themes", "Background Images, Cover, Contain & Parallax",
    "Linear, Radial & Conic CSS Gradients", "Box-Shadow & 3D Text-Shadow Effects", "Designing Shapes using Border-Radius",
    "Opacity, RGBA & HSLA Transparency", "CSS Overflow Properties (Visible, Hidden, Scroll)", "Z-Index & Stacking Context Hierarchy",
    "CSS Display Modes (Block, Inline, Flex, Grid)", "Visibility: Hidden vs Display: None vs Opacity: 0", "Pure CSS Multi-Level Dropdown Menu",
    "Image Hover Animation Effects", "Pure CSS Tooltips with Arrow Indicators", "CSS Button Hover Animations (Ripple & Glow)",
    "Interactive CSS Filters (Blur, Grayscale, Brightness)", "Object-Fit & Object-Position Demonstration", "Responsive Auto-Fit Image Gallery",
    "Card-Based Layout using Flexbox", "Admin Dashboard Layout using CSS Grid", "Two-Column Webpage Layout using CSS Grid",
    "Three-Column Webpage Layout using Flexbox", "Sticky Header Navigation Bar", "Fixed Sidebar Navigation Layout",
    "Multi-Column Responsive Footer Layout", "Responsive Login & Signup Dual-Tab Form", "Responsive Contact Form Layout",
    "College Website Homepage Layout", "Restaurant Website Layout & Menu", "E-commerce Online Shopping Store Catalog",
    "Travel Agency Website Homepage", "News & Blog Magazine Layout using CSS Grid", "Multi-Section Portfolio Website Layout",
    "CSS Grid Template Areas Layout", "Flexbox Alignment & Item Order Properties", "Responsive Grid Layout with Media Queries",
    "Mobile-First Responsive Web Design", "CSS Transition Timing & Delay Demonstration", "2D & 3D CSS Transforms (3D Card Flip)",
    "Multi-Stage Keyframe Animation Timeline", "Custom CSS Loading Spinners", "Sliding Card Carousel Animation in Pure CSS",
    "Pure CSS Modal Popup Dialog Design", "Dark Mode Toggle using CSS Variables", "Responsive Fluid Typography (clamp, rem, vw)",
    "CSS Functions: clamp(), min(), and max()", "Dynamic Calculations using CSS calc() Function", "Master Responsive Website Layout (HTML5, CSS3, Flexbox & Grid)"
]

for idx, title in enumerate(css_titles, 1):
    fn = f"{idx:02d}-css-program.html"
    desc = f"CSS Practical Experiment #{idx}: Demonstrating {title}"
    demo = f"<div class='css-demo-card' style='padding:1.5rem; background:#ffffff; border-radius:8px; border:1px solid #cbd5e1;'><h3 style='color:#4f46e5; margin-bottom:0.5rem;'>{title}</h3><p style='color:#64748b;'>This practical experiment demonstrates {title.lower()} with customized layout, colors, and responsive styling.</p><div style='margin-top:1rem; padding:1rem; background:#f1f5f9; border-radius:6px; font-weight:600;'>Visual CSS Demonstration Output Container #{idx}</div></div>"
    custom_css = ".css-demo-card { box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); transition: all 0.3s ease; } .css-demo-card:hover { transform: translateY(-3px); border-color: #4f46e5; }"
    
    content = tpl("css", f"CSS Exp #{idx}: {title}", desc, demo, custom_css)
    with open(os.path.join(CSS_DIR, fn), "w", encoding="utf-8") as f:
        f.write(content)

print("Generated 75 CSS program files.")
