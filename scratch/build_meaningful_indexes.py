import os

ROOT = r"c:\Users\Lenovo\OneDrive\Desktop\html"

# Import html_programs, css_items, js_programs from generators
from build_meaningful_assignment import html_programs
from build_meaningful_css_js import css_items
from build_meaningful_js import js_programs

html_files_meta = [(fn, title, desc) for fn, title, desc, *rest in html_programs]
css_files_meta = [(fn, title, desc) for fn, title, desc in css_items]
js_files_meta = [(fn, title, desc) for fn, title, desc, *rest in js_programs]

# Helper function to generate ordered list page (<ol><li><a href="...">Title</a></li></ol>)
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

# Write section index pages
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

print("Generated full project with meaningful filenames, index listing pages (<ol><li><a href='...'>), and README.md.")
