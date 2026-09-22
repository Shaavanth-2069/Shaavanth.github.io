import os

ROOT = r"c:\Users\Lenovo\OneDrive\Desktop\html"

# Main index.html
MAIN_INDEX = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Technology & Internet Programming - Practical Assignment Portal</title>
    <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
    <header class="app-header">
        <h1>HTML, CSS & JAVASCRIPT</h1>
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
                🎉 Total Practical Programs Completed: 195 Programs
            </div>
            <p style="color: var(--text-muted); max-width: 650px; margin: 0.5rem auto;">
                Welcome to the complete practical assignment repository. Explore interactive experiments across HTML5 fundamentals, CSS3 layouts and animations, and JavaScript DOM & Mini Projects.
            </p>
        </section>

        <section class="dash-grid">
            <!-- HTML Programs Card -->
            <div class="dash-card">
                <div class="dash-icon">📄</div>
                <h2 class="dash-title">HTML Programs</h2>
                <div class="count-badge">15 Completed Programs</div>
                <p class="dash-desc">
                    Includes basic HTML elements, lists, tables with merged cells, multimedia audio/video, forms, semantic layout tags, timetable, internal/external CSS integration, and Bootstrap components.
                </p>
                <a href="html/index.html" class="btn-primary">View HTML Programs</a>
            </div>

            <!-- CSS Programs Card -->
            <div class="dash-card">
                <div class="dash-icon">🎨</div>
                <h2 class="dash-title">CSS Programs</h2>
                <div class="count-badge">75 Completed Programs</div>
                <p class="dash-desc">
                    Demonstrating inline/internal/external styling, selectors, box model, positioning, Flexbox, CSS Grid layouts, @keyframes animations, filters, transitions, custom variables, and responsive websites.
                </p>
                <a href="css/index.html" class="btn-primary">View CSS Programs</a>
            </div>

            <!-- JS Programs Card -->
            <div class="dash-card">
                <div class="dash-icon">⚡</div>
                <h2 class="dash-title">JavaScript Programs</h2>
                <div class="count-badge">105 Completed Programs</div>
                <p class="dash-desc">
                    Comprehensive collection covering algorithmic programs, DOM manipulation, event listeners, form validation, browser objects, Web Storage (localStorage/sessionStorage), and 17 Mini Projects.
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

print("Created main index.html dashboard.")
