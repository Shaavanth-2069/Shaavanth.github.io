import os
import re

ROOT = r"c:\Users\Lenovo\OneDrive\Desktop\html"
HTML_DIR = os.path.join(ROOT, "html")
CSS_DIR = os.path.join(ROOT, "css")
JS_DIR = os.path.join(ROOT, "javascript")
ASSETS_CSS_DIR = os.path.join(ROOT, "assets", "css")

for d in [ROOT, HTML_DIR, CSS_DIR, JS_DIR, ASSETS_CSS_DIR]:
    os.makedirs(d, exist_ok=True)

# Master CSS
CSS_CONTENT = """/* Master Stylesheet - Web Technology Practical Assignment */
:root {
  --primary: #4f46e5;
  --primary-hover: #4338ca;
  --secondary: #06b6d4;
  --accent: #10b981;
  --dark-bg: #0f172a;
  --light-bg: #f8fafc;
  --card-bg: #ffffff;
  --text-main: #1e293b;
  --text-muted: #64748b;
  --border: #e2e8f0;
  --radius: 10px;
  --shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06);
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
  background-color: var(--light-bg);
  color: var(--text-main);
  line-height: 1.6;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* Header & Navigation */
.app-header {
  background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%);
  color: #ffffff;
  padding: 2rem 1.5rem;
  text-align: center;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.app-header h1 { font-size: 2.2rem; font-weight: 700; margin-bottom: 0.4rem; }
.app-header p { font-size: 1rem; color: #c7d2fe; }

.student-meta {
  display: inline-flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1.2rem;
  margin-top: 1rem;
  background: rgba(255, 255, 255, 0.12);
  backdrop-filter: blur(8px);
  padding: 0.5rem 1.2rem;
  border-radius: 9999px;
  font-size: 0.85rem;
  border: 1px solid rgba(255, 255, 255, 0.25);
}

.top-nav {
  background: #ffffff;
  padding: 0.75rem 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid var(--border);
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-brand { font-weight: 700; color: var(--primary); text-decoration: none; font-size: 1.1rem; }
.nav-links { display: flex; gap: 0.75rem; list-style: none; }

.nav-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.45rem 0.9rem;
  background: #f1f5f9;
  color: var(--text-main);
  text-decoration: none;
  font-weight: 600;
  font-size: 0.875rem;
  border-radius: 6px;
  transition: all 0.2s ease;
  border: 1px solid var(--border);
}

.nav-btn:hover, .nav-btn.active {
  background: var(--primary);
  color: #ffffff;
  border-color: var(--primary);
}

.main-container {
  max-width: 1100px;
  margin: 2rem auto;
  padding: 0 1.5rem;
  flex: 1;
  width: 100%;
}

/* Dashboard Cards */
.dash-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.8rem;
  margin-top: 1.5rem;
}

.dash-card {
  background: var(--card-bg);
  border-radius: var(--radius);
  padding: 2rem;
  box-shadow: var(--shadow);
  border: 1px solid var(--border);
  transition: all 0.25s ease;
  display: flex;
  flex-direction: column;
}

.dash-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.1);
  border-color: var(--primary);
}

.dash-icon { font-size: 2.5rem; margin-bottom: 0.8rem; }
.dash-title { font-size: 1.4rem; color: var(--text-main); margin-bottom: 0.4rem; }
.dash-desc { color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.25rem; flex: 1; }

.count-badge {
  display: inline-block;
  font-size: 0.8rem;
  font-weight: 700;
  background: #e0e7ff;
  color: var(--primary);
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  margin-bottom: 1.25rem;
  width: fit-content;
}

.btn-primary {
  display: inline-block;
  text-align: center;
  width: 100%;
  padding: 0.75rem 1.2rem;
  background: var(--primary);
  color: #ffffff;
  text-decoration: none;
  font-weight: 600;
  border-radius: 6px;
  transition: background 0.2s ease;
  border: none;
  cursor: pointer;
}

.btn-primary:hover { background: var(--primary-hover); }

/* Listings */
.search-box {
  width: 100%;
  padding: 0.75rem 1.2rem;
  font-size: 1rem;
  border: 1px solid var(--border);
  border-radius: 8px;
  margin-bottom: 1.5rem;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

.prog-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.2rem;
}

.prog-item {
  background: #ffffff;
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 1.2rem;
  transition: all 0.2s ease;
  display: flex;
  flex-direction: column;
}

.prog-item:hover {
  border-color: var(--primary);
  box-shadow: var(--shadow);
  transform: translateY(-2px);
}

.prog-num { font-size: 0.8rem; font-weight: 700; color: var(--primary); }
.prog-title { font-size: 1.05rem; font-weight: 600; margin: 0.3rem 0; color: var(--text-main); }
.prog-desc { font-size: 0.85rem; color: var(--text-muted); margin-bottom: 0.8rem; flex: 1; }
.prog-link {
  text-decoration: none;
  color: var(--primary);
  font-weight: 600;
  font-size: 0.9rem;
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
}
.prog-link:hover { text-decoration: underline; }

/* Experiment Demo Page */
.exp-card {
  background: #ffffff;
  border-radius: var(--radius);
  border: 1px solid var(--border);
  box-shadow: var(--shadow);
  padding: 2rem;
  margin-bottom: 2rem;
}

.exp-header {
  border-bottom: 2px solid #f1f5f9;
  padding-bottom: 1rem;
  margin-bottom: 1.5rem;
}

.exp-title { font-size: 1.6rem; color: var(--primary); font-weight: 700; }
.exp-desc { color: var(--text-muted); margin-top: 0.4rem; font-size: 0.95rem; }

.demo-box {
  background: #f8fafc;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  padding: 1.5rem;
  margin: 1.2rem 0;
}

.page-footer {
  background: #ffffff;
  border-top: 1px solid var(--border);
  padding: 1.5rem;
  text-align: center;
  margin-top: auto;
  font-size: 0.9rem;
  color: var(--text-muted);
}

.footer-nav {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 0.75rem;
}

.btn-secondary {
  padding: 0.45rem 0.9rem;
  background: #e2e8f0;
  color: var(--text-main);
  text-decoration: none;
  border-radius: 6px;
  font-weight: 600;
  font-size: 0.875rem;
  transition: background 0.2s ease;
}
.btn-secondary:hover { background: #cbd5e1; }

.form-group { margin-bottom: 1rem; }
.form-group label { display: block; font-weight: 600; margin-bottom: 0.3rem; font-size: 0.9rem; }
.form-control { width: 100%; padding: 0.6rem 0.8rem; border: 1px solid var(--border); border-radius: 6px; font-size: 0.95rem; }
.form-control:focus { outline: none; border-color: var(--primary); box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.2); }

.btn-action {
  padding: 0.6rem 1.2rem;
  background: var(--primary);
  color: white;
  border: none;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
}
.btn-action:hover { background: var(--primary-hover); }
"""

with open(os.path.join(ASSETS_CSS_DIR, "style.css"), "w", encoding="utf-8") as f:
    f.write(CSS_CONTENT)

print("Master style.css updated.")
