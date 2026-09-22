import os
import shutil

ROOT = r"c:\Users\Lenovo\OneDrive\Desktop\html"
HTML_DIR = os.path.join(ROOT, "html")
CSS_DIR = os.path.join(ROOT, "css")
JS_DIR = os.path.join(ROOT, "javascript")
ASSETS_CSS = os.path.join(ROOT, "assets", "css")

for d in [HTML_DIR, CSS_DIR, JS_DIR]:
    os.makedirs(d, exist_ok=True)

os.makedirs(ASSETS_CSS, exist_ok=True)

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

print("Generated 15 HTML files with meaningful filenames.")
