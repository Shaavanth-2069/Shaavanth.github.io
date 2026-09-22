import os

ROOT = r"c:\Users\Lenovo\OneDrive\Desktop\html"
HTML_DIR = os.path.join(ROOT, "html")
CSS_DIR = os.path.join(ROOT, "css")
JS_DIR = os.path.join(ROOT, "javascript")

from build_122_js_portal import js_122_list
from build_meaningful_assignment import html_programs
from build_meaningful_css_js import css_items

valid_html_files = {"index.html"}.union({fn for fn, *rest in html_programs})
valid_css_files = {"index.html"}.union({fn for fn, *rest in css_items})
valid_js_files = {"index.html"}.union({fn for fn, *rest in js_122_list})

# Clean HTML folder
for f in os.listdir(HTML_DIR):
    if f not in valid_html_files:
        try: os.remove(os.path.join(HTML_DIR, f))
        except: pass

# Clean CSS folder
for f in os.listdir(CSS_DIR):
    if f not in valid_css_files:
        try: os.remove(os.path.join(CSS_DIR, f))
        except: pass

# Clean JS folder
for f in os.listdir(JS_DIR):
    if f not in valid_js_files:
        try: os.remove(os.path.join(JS_DIR, f))
        except: pass

print("Cleanup complete.")
print("HTML count:", len(os.listdir(HTML_DIR)), "(Expected 16: 15 programs + 1 index.html)")
print("CSS count:", len(os.listdir(CSS_DIR)), "(Expected 76: 75 programs + 1 index.html)")
print("JS count:", len(os.listdir(JS_DIR)), "(Expected 123: 122 programs + 1 index.html)")
