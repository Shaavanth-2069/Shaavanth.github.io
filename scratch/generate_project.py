import os
import json

ROOT_DIR = r"c:\Users\Lenovo\OneDrive\Desktop\html"

HTML_DIR = os.path.join(ROOT_DIR, "html")
CSS_DIR = os.path.join(ROOT_DIR, "css")
JS_DIR = os.path.join(ROOT_DIR, "javascript")
ASSETS_CSS_DIR = os.path.join(ROOT_DIR, "assets", "css")

os.makedirs(HTML_DIR, exist_ok=True)
os.makedirs(CSS_DIR, exist_ok=True)
os.makedirs(JS_DIR, exist_ok=True)
os.makedirs(ASSETS_CSS_DIR, exist_ok=True)

# Shared CSS Content
STYLE_CSS = """/* Web Technology Practical Assignment - Master Stylesheet */
:root {
  --primary-color: #4f46e5;
  --primary-hover: #4338ca;
  --secondary-color: #06b6d4;
  --accent-color: #10b981;
  --dark-bg: #0f172a;
  --light-bg: #f8fafc;
  --card-bg: #ffffff;
  --text-main: #1e293b;
  --text-muted: #64748b;
  --border-color: #e2e8f0;
  --radius-sm: 6px;
  --radius-md: 12px;
  --radius-lg: 16px;
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.1);
  --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06);
  --shadow-lg: 0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -2px rgba(0,0,0,0.05);
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
  background-color: var(--light-bg);
  color: var(--text-main);
  line-height: 1.6;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.app-header {
  background: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #4338ca 100%);
  color: #ffffff;
  padding: 2.2rem 1.5rem;
  text-align: center;
  box-shadow: var(--shadow-md);
}

.app-header h1 { font-size: 2rem; font-weight: 700; margin-bottom: 0.4rem; }
.app-header p { font-size: 0.95rem; color: #c7d2fe; }

.student-badge {
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
  border-bottom: 1px solid var(--border-color);
  box-shadow: var(--shadow-sm);
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-brand { font-weight: 700; color: var(--primary-color); text-decoration: none; font-size: 1.1rem; }

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
  border-radius: var(--radius-sm);
  transition: all 0.2s ease;
  border: 1px solid var(--border-color);
}

.nav-btn:hover, .nav-btn.active {
  background: var(--primary-color);
  color: #ffffff;
  border-color: var(--primary-color);
}

.main-container {
  max-width: 1100px;
  margin: 2rem auto;
  padding: 0 1.5rem;
  flex: 1;
  width: 100%;
}

.dashboard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.8rem;
  margin-top: 1.5rem;
}

.dash-card {
  background: var(--card-bg);
  border-radius: var(--radius-md);
  padding: 2rem;
  box-shadow: var(--shadow-sm);
  border: 1px solid var(--border-color);
  transition: all 0.25s ease;
  display: flex;
  flex-direction: column;
}

.dash-card:hover {
  transform: translateY(-5px);
  box-shadow: var(--shadow-lg);
  border-color: var(--primary-color);
}

.dash-icon { font-size: 2.5rem; margin-bottom: 1rem; }
.dash-title { font-size: 1.4rem; color: var(--text-main); margin-bottom: 0.5rem; }
.dash-desc { color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.25rem; flex: 1; }
.dash-badge {
  display: inline-block;
  font-size: 0.8rem;
  font-weight: 700;
  background: #e0e7ff;
  color: var(--primary-color);
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  margin-bottom: 1.25rem;
}

.btn-primary {
  display: inline-block;
  text-align: center;
  width: 100%;
  padding: 0.75rem 1.2rem;
  background: var(--primary-color);
  color: #ffffff;
  text-decoration: none;
  font-weight: 600;
  border-radius: var(--radius-sm);
  transition: background 0.2s ease;
  border: none;
  cursor: pointer;
}

.btn-primary:hover { background: var(--primary-hover); }

/* Program List Styling */
.search-box {
  width: 100%;
  padding: 0.75rem 1.2rem;
  font-size: 1rem;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  margin-bottom: 1.5rem;
  box-shadow: var(--shadow-sm);
}

.program-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.2rem;
}

.program-item {
  background: #ffffff;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-sm);
  padding: 1.2rem;
  transition: all 0.2s ease;
  display: flex;
  flex-direction: column;
}

.program-item:hover {
  border-color: var(--primary-color);
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}

.program-num { font-size: 0.8rem; font-weight: 700; color: var(--primary-color); }
.program-name { font-size: 1.05rem; font-weight: 600; margin: 0.3rem 0; color: var(--text-main); }
.program-link {
  margin-top: auto;
  padding-top: 0.75rem;
  text-decoration: none;
  color: var(--primary-color);
  font-weight: 600;
  font-size: 0.9rem;
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
}
.program-link:hover { text-decoration: underline; }

/* Program Page Layout */
.experiment-box {
  background: #ffffff;
  border-radius: var(--radius-md);
  border: 1px solid var(--border-color);
  box-shadow: var(--shadow-sm);
  padding: 2rem;
  margin-bottom: 2rem;
}

.exp-header {
  border-bottom: 2px solid #f1f5f9;
  padding-bottom: 1rem;
  margin-bottom: 1.5rem;
}

.exp-title { font-size: 1.6rem; color: var(--primary-color); font-weight: 700; }
.exp-desc { color: var(--text-muted); margin-top: 0.4rem; font-size: 0.95rem; }

.demo-container {
  background: #f8fafc;
  border: 1px solid #cbd5e1;
  border-radius: var(--radius-sm);
  padding: 1.5rem;
  margin: 1.2rem 0;
  min-height: 120px;
}

.page-footer {
  background: #ffffff;
  border-top: 1px solid var(--border-color);
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
  padding: 0.5rem 1rem;
  background: #e2e8f0;
  color: var(--text-main);
  text-decoration: none;
  border-radius: var(--radius-sm);
  font-weight: 600;
  transition: background 0.2s ease;
}
.btn-secondary:hover { background: #cbd5e1; }

.form-group { margin-bottom: 1rem; }
.form-group label { display: block; font-weight: 600; margin-bottom: 0.3rem; font-size: 0.9rem; }
.form-control { width: 100%; padding: 0.6rem 0.8rem; border: 1px solid var(--border-color); border-radius: var(--radius-sm); font-size: 0.95rem; }
.form-control:focus { outline: none; border-color: var(--primary-color); box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.2); }
"""

with open(os.path.join(ASSETS_CSS_DIR, "style.css"), "w", encoding="utf-8") as f:
    f.write(STYLE_CSS)

print("Master style.css written.")
