import os

ROOT = r"c:\Users\Lenovo\OneDrive\Desktop\html"
HTML_DIR = os.path.join(ROOT, "html")
CSS_DIR = os.path.join(ROOT, "css")
JS_DIR = os.path.join(ROOT, "javascript")
ASSETS_CSS = os.path.join(ROOT, "assets", "css")

for d in [ROOT, HTML_DIR, CSS_DIR, JS_DIR, ASSETS_CSS]:
    os.makedirs(d, exist_ok=True)

# Helper function to generate an HTML program page template
def make_program_page(section, filename, title, description, demo_html, custom_css="", custom_js=""):
    rel_css_path = "../assets/css/style.css"
    section_index = "index.html"
    home_index = "../index.html"
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Practical Assignment</title>
    <link rel="stylesheet" href="{rel_css_path}">
    <style>
        {custom_css}
    </style>
</head>
<body>
    <header class="app-header">
        <h1>{title}</h1>
        <p>{description}</p>
        <div class="student-meta">
            <span>👤 <strong>Student:</strong> Gandikota Shaavanth</span>
            <span>🆔 <strong>Reg No:</strong> 250200412</span>
            <span>📚 <strong>Subject:</strong> Web Technology & Internet Programming</span>
        </div>
    </header>

    <nav class="top-nav">
        <a href="{home_index}" class="nav-brand">🌐 Web Tech Assignment</a>
        <div class="nav-links">
            <a href="{home_index}" class="nav-btn">🏠 Home Dashboard</a>
            <a href="{section_index}" class="nav-btn active">🔙 Back to {section.upper()} Programs</a>
        </div>
    </nav>

    <main class="main-container">
        <section class="exp-card">
            <div class="exp-header">
                <h2 class="exp-title">{title}</h2>
                <p class="exp-desc">{description}</p>
            </div>

            <div class="demo-box">
                {demo_html}
            </div>
        </section>
    </main>

    <footer class="page-footer">
        <div class="footer-nav">
            <a href="{home_index}" class="btn-secondary">🏠 Dashboard</a>
            <a href="{section_index}" class="btn-secondary">🔙 {section.upper()} Program List</a>
        </div>
        <p>&copy; 2026 Practical Assignment | Student: Gandikota Shaavanth (250200412)</p>
    </footer>

    <script>
        {custom_js}
    </script>
</body>
</html>"""

print("Helper template generator ready.")
