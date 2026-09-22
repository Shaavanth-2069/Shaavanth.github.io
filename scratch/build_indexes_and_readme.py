import os

ROOT = r"c:\Users\Lenovo\OneDrive\Desktop\html"

# HTML Listing Page
html_files = [
    ("01-basic-webpage.html", "Basic HTML Webpage", "Headings, paragraphs, line breaks, formatting"),
    ("02-ordered-unordered-lists.html", "Ordered, Unordered & Description Lists", "Lists structure and nested list items"),
    ("03-tables-merged-cells.html", "Tables with Merged Cells", "Colspan, rowspan, headers, and borders"),
    ("04-images-hyperlinks.html", "Images & Hyperlinks", "Image tags, figure captions, and links"),
    ("05-student-registration-form.html", "Student Registration Form", "Form input fields, radio, dropdowns, submit"),
    ("06-audio-video-elements.html", "Audio & Video Elements", "HTML5 audio player and video player controls"),
    ("07-frames-iframes.html", "Iframes Webpage", "Embedding external content using inline frames"),
    ("08-semantic-elements.html", "Semantic Structure Elements", "Header, nav, section, article, and footer"),
    ("09-html5-input-types.html", "HTML5 Input Types", "Email, date, number, color, range, password"),
    ("10-college-timetable.html", "College Lecture Timetable", "Structured HTML table timetable grid"),
    ("11-internal-external-css.html", "Internal & External CSS", "Inline, internal, and external CSS styles"),
    ("12-css-selectors-styling.html", "CSS Selectors & Styling", "Element, class, ID selectors, fonts, borders"),
    ("13-responsive-media-queries.html", "Responsive Media Queries", "Layout adaptation for desktop, tablet, mobile"),
    ("14-bootstrap-components.html", "Bootstrap 5 Components", "Navbar, hero, buttons, cards via CDN"),
    ("15-simple-portfolio.html", "Simple Personal Portfolio", "HTML & CSS personal portfolio section")
]

def make_list_page(title, category, files, rel_home="../index.html"):
    items_html = ""
    for idx, (fn, name, desc) in enumerate(files, 1):
        items_html += f"""
        <div class="prog-item">
            <span class="prog-num"># {idx:02d}</span>
            <h3 class="prog-title">{name}</h3>
            <p class="prog-desc">{desc}</p>
            <a href="{fn}" class="prog-link">View Program &rarr;</a>
        </div>"""
        
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Practical Assignment</title>
    <link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>
    <header class="app-header">
        <h1>{title}</h1>
        <p>Complete List of Completed {category} Practical Experiments</p>
        <div class="student-meta">
            <span>👤 <strong>Student:</strong> Gandikota Shaavanth</span>
            <span>🆔 <strong>Reg No:</strong> 250200412</span>
            <span>📚 <strong>Subject:</strong> Web Technology & Internet Programming</span>
        </div>
    </header>

    <nav class="top-nav">
        <a href="{rel_home}" class="nav-brand">🌐 Web Tech Assignment</a>
        <div class="nav-links">
            <a href="{rel_home}" class="nav-btn">🏠 Home Dashboard</a>
            <a href="#" class="nav-btn active">{category} Programs ({len(files)})</a>
        </div>
    </nav>

    <main class="main-container">
        <input type="text" id="searchBox" class="search-box" placeholder="🔍 Search {category} programs by title or description..." onkeyup="filterProgs()">
        <div class="prog-grid" id="progGrid">
            {items_html}
        </div>
    </main>

    <footer class="page-footer">
        <div class="footer-nav">
            <a href="{rel_home}" class="btn-secondary">🏠 Home Dashboard</a>
        </div>
        <p>&copy; 2026 Practical Assignment | Gandikota Shaavanth (250200412)</p>
    </footer>

    <script>
        function filterProgs() {{
            const q = document.getElementById('searchBox').value.toLowerCase();
            const items = document.querySelectorAll('.prog-item');
            items.forEach(item => {{
                const txt = item.innerText.toLowerCase();
                item.style.display = txt.includes(q) ? 'flex' : 'none';
            }});
        }}
    </script>
</body>
</html>"""

with open(os.path.join(ROOT, "html", "index.html"), "w", encoding="utf-8") as f:
    f.write(make_list_page("HTML Programs", "HTML", html_files))

print("Created html/index.html")
