import os

ROOT = r"c:\Users\Lenovo\OneDrive\Desktop\html"
HTML_DIR = os.path.join(ROOT, "html")
CSS_DIR = os.path.join(ROOT, "css")
JS_DIR = os.path.join(ROOT, "javascript")
ASSETS_CSS = os.path.join(ROOT, "assets", "css")

for d in [ROOT, HTML_DIR, CSS_DIR, JS_DIR, ASSETS_CSS]:
    os.makedirs(d, exist_ok=True)

# Shared HTML Template
def page_tpl(section, title, desc, demo, css="", js=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Web Tech Assignment</title>
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
        <a href="../index.html" class="nav-brand">🌐 Practical Assignment</a>
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
        <p>&copy; 2026 Practical Assignment | Gandikota Shaavanth (250200412)</p>
    </footer>

    <script>{js}</script>
</body>
</html>"""

print("Base page template initialized.")
