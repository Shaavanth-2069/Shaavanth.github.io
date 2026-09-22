import os
import sys

ROOT = r"c:\Users\Lenovo\OneDrive\Desktop\html"
HTML_DIR = os.path.join(ROOT, "html")
CSS_DIR = os.path.join(ROOT, "css")
JS_DIR = os.path.join(ROOT, "javascript")
ASSETS_CSS = os.path.join(ROOT, "assets", "css")

for d in [ROOT, HTML_DIR, CSS_DIR, JS_DIR, ASSETS_CSS]:
    os.makedirs(d, exist_ok=True)

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

# HTML Programs List (15)
html_list = [
    ("01-basic-webpage.html", "Basic HTML Webpage", "Headings, paragraphs, line breaks, and text formatting",
     "<h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3><p>This is a paragraph demonstrating line breaks<br>and text formatting elements like <strong>bold text</strong>, <em>italic text</em>, and <u>underlined text</u>.</p>", "", ""),
    
    ("02-ordered-unordered-lists.html", "HTML Lists Showcase", "Ordered, unordered, and description lists",
     "<h3>Ordered List</h3><ol><li>First Item</li><li>Second Item</li><li>Third Item</li></ol><h3>Unordered List</h3><ul><li>HTML5</li><li>CSS3</li><li>JavaScript</li></ul><h3>Description List</h3><dl><dt>HTML</dt><dd>HyperText Markup Language</dd><dt>CSS</dt><dd>Cascading Style Sheets</dd></dl>", "", ""),
    
    ("03-tables-merged-cells.html", "HTML Tables & Merged Cells", "Table with rows, columns, borders, colspan, and rowspan",
     "<table class='custom-table'><thead><tr><th rowspan='2'>Student Name</th><th colspan='2'>Marks</th></tr><tr><th>Theory</th><th>Practical</th></tr></thead><tbody><tr><td>Gandikota Shaavanth</td><td>95</td><td>98</td></tr><tr><td>Aarav Sharma</td><td>90</td><td>92</td></tr></tbody></table>", "", ""),
    
    ("04-images-hyperlinks.html", "Images & Hyperlinks", "Embedding images, image captions, and hyperlinks",
     "<h3>Hyperlinks & Image</h3><p>Visit <a href='https://developer.mozilla.org/' target='_blank'>MDN Web Docs</a> for documentation.</p><figure style='margin-top:1rem;'><img src='https://via.placeholder.com/400x180/4f46e5/ffffff?text=HTML5+Images' alt='Sample Image' style='max-width:100%; border-radius:8px;'><figcaption>Figure 1: HTML5 Image Demonstration</figcaption></figure>", "", ""),
    
    ("05-student-registration-form.html", "Student Registration Form", "Comprehensive HTML form elements",
     "<form class='exp-form'><div class='form-group'><label>Full Name:</label><input type='text' class='form-control' placeholder='Gandikota Shaavanth'></div><div class='form-group'><label>Gender:</label><input type='radio' name='gen' checked> Male <input type='radio' name='gen'> Female</div><div class='form-group'><label>Course:</label><select class='form-control'><option>Computer Science</option><option>Information Technology</option></select></div><button type='button' class='btn-action' onclick='alert(\"Form Submitted!\")'>Submit Registration</button></form>", "", ""),
    
    ("06-audio-video-elements.html", "Audio & Video Elements", "HTML5 multimedia audio and video players with controls",
     "<h3>Audio Player</h3><audio controls style='width:100%; margin-bottom:1.5rem;'><source src='https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3' type='audio/mpeg'>Your browser does not support audio element.</audio><h3>Video Player</h3><video controls style='width:100%; max-height:280px; border-radius:8px;'><source src='https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4' type='video/mp4'>Your browser does not support video tag.</video>", "", ""),
    
    ("07-frames-iframes.html", "HTML Iframes", "Embedding external web content using inline frames",
     "<h3>Embedded Inline Frame (iframe)</h3><iframe src='https://wikipedia.org' style='width:100%; height:320px; border:1px solid #cbd5e1; border-radius:8px;'></iframe>", "", ""),
    
    ("08-semantic-elements.html", "Semantic Structure Elements", "Demonstration of header, nav, section, article, and footer tags",
     "<div style='border:1px dashed #4f46e5; padding:1rem; border-radius:8px;'><header style='background:#e0e7ff; padding:0.5rem; border-radius:4px;'>&lt;header&gt; Header Banner &lt;/header&gt;</header><nav style='background:#c7d2fe; padding:0.5rem; margin:0.5rem 0; border-radius:4px;'>&lt;nav&gt; Navigation Bar &lt;/nav&gt;</nav><section style='background:#f1f5f9; padding:0.5rem; border-radius:4px;'><article style='background:#ffffff; padding:0.5rem; border:1px solid #cbd5e1; border-radius:4px;'>&lt;article&gt; Article Content Section &lt;/article&gt;</article></section><footer style='background:#e2e8f0; padding:0.5rem; margin-top:0.5rem; border-radius:4px;'>&lt;footer&gt; Footer &lt;/footer&gt;</footer></div>", "", ""),
    
    ("09-html5-input-types.html", "HTML5 Input Types", "Email, date, number, password, color, and range inputs",
     "<div class='form-group'><label>Email:</label><input type='email' class='form-control' value='shaavanth@example.com'></div><div class='form-group'><label>Date of Birth:</label><input type='date' class='form-control' value='2005-08-15'></div><div class='form-group'><label>Age (Number):</label><input type='number' class='form-control' value='20'></div><div class='form-group'><label>Favorite Color:</label><input type='color' value='#4f46e5' style='height:40px; cursor:pointer;'></div><div class='form-group'><label>Satisfaction Range:</label><input type='range' min='1' max='100' value='85' style='width:100%;'></div>", "", ""),
    
    ("10-college-timetable.html", "College Timetable", "Weekly lecture timetable using HTML table layout",
     "<table class='custom-table'><thead><tr><th>Day / Time</th><th>9:00 - 10:00</th><th>10:00 - 11:00</th><th>11:15 - 12:15</th><th>1:00 - 2:00</th></tr></thead><tbody><tr><td>Monday</td><td>Web Tech</td><td>DBMS</td><td>Java</td><td>Lab</td></tr><tr><td>Tuesday</td><td>OS</td><td>Web Tech</td><td>Data Structures</td><td>Python</td></tr><tr><td>Wednesday</td><td>DBMS</td><td>Maths</td><td>Web Tech</td><td>Library</td></tr></tbody></table>", "", ""),
    
    ("11-internal-external-css.html", "Internal & External CSS", "Demonstration of inline, internal, and external CSS styling",
     "<p style='color:red; font-weight:bold;'>Inline CSS Styled Text</p><p class='internal-styled'>Internal CSS Styled Text (Green)</p><p>External CSS Styled Text from Master Stylesheet (Dark Slate)</p>",
     ".internal-styled { color: #10b981; font-size: 1.1rem; border-left: 4px solid #10b981; padding-left: 0.5rem; margin: 0.5rem 0; }", ""),
    
    ("12-css-selectors-styling.html", "CSS Selectors & Styling", "Demonstrating class, ID, element selectors, fonts, and borders",
     "<div id='unique-box'>ID Selector Box (#unique-box)</div><div class='custom-class'>Class Selector Box (.custom-class)</div>",
     "#unique-box { background: #e0e7ff; color: #3730a3; padding: 1rem; border-radius: 6px; font-weight: bold; margin-bottom: 0.8rem; } .custom-class { background: #dcfce7; color: #166534; padding: 1rem; border-radius: 6px; border: 2px dashed #22c55e; }", ""),
    
    ("13-responsive-media-queries.html", "CSS Media Queries", "Responsive webpage layout adapting to screen sizes",
     "<div class='responsive-box'>Resize your browser window to test background color change!</div>",
     ".responsive-box { padding: 1.5rem; color: white; background: #4f46e5; border-radius: 8px; text-align: center; font-size: 1.2rem; } @media(max-width: 768px) { .responsive-box { background: #06b6d4; } } @media(max-width: 480px) { .responsive-box { background: #10b981; } }", ""),
    
    ("14-bootstrap-components.html", "Bootstrap 5 Components", "Integrating Bootstrap buttons, cards, and badges via CDN",
     "<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css' rel='stylesheet'><div class='card text-center'><div class='card-header bg-primary text-white'>Bootstrap Card Header</div><div class='card-body'><h5 class='card-title'>Bootstrap Integration</h5><p class='card-text'>This component utilizes Bootstrap 5 styling.</p><button class='btn btn-success'>Bootstrap Success Button <span class='badge bg-light text-dark'>New</span></button></div></div>", "", ""),
    
    ("15-simple-portfolio.html", "Simple Personal Portfolio", "Personal portfolio webpage layout built with HTML & CSS",
     "<div style='text-align:center; padding:1.5rem; background:#ffffff; border-radius:10px; border:1px solid #e2e8f0;'><img src='https://via.placeholder.com/120' style='border-radius:50%; margin-bottom:1rem;'><h3 style='color:#4f46e5;'>Gandikota Shaavanth</h3><p style='color:#64748b;'>Full Stack Web Developer & Computer Science Student</p><div style='margin-top:1rem; display:flex; justify-content:center; gap:0.5rem; flex-wrap:wrap;'><span style='background:#e0e7ff; color:#4f46e5; padding:0.3rem 0.8rem; border-radius:999px; font-weight:600;'>HTML5</span><span style='background:#e0e7ff; color:#4f46e5; padding:0.3rem 0.8rem; border-radius:999px; font-weight:600;'>CSS3</span><span style='background:#e0e7ff; color:#4f46e5; padding:0.3rem 0.8rem; border-radius:999px; font-weight:600;'>JavaScript</span></div></div>", "", "")
]

# Write HTML Files
for fn, title, desc, demo, css, js in html_list:
    content = tpl("html", title, desc, demo, css, js)
    with open(os.path.join(HTML_DIR, fn), "w", encoding="utf-8") as f:
        f.write(content)

print("Generated 15 HTML program files.")
