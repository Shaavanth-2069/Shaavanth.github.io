import os

ROOT = r"c:\Users\Lenovo\OneDrive\Desktop\html"
HTML_DIR = os.path.join(ROOT, "html")
CSS_DIR = os.path.join(ROOT, "css")
JS_DIR = os.path.join(ROOT, "javascript")
ASSETS_CSS = os.path.join(ROOT, "assets", "css")

for d in [ROOT, HTML_DIR, CSS_DIR, JS_DIR, ASSETS_CSS]:
    os.makedirs(d, exist_ok=True)

# 1. CSS Files Listing Generator (75 Items)
css_files = []
css_titles = [
    "Inline, Internal, and External CSS", "CSS Selectors (Element, Class, ID, Universal)", "CSS Colors, Backgrounds, and Borders",
    "Font Properties & Text Formatting", "CSS Box Model (Margin, Border, Padding, Content)", "Width, Height, and Box-Sizing Properties",
    "CSS Positioning (Static, Relative, Absolute, Fixed, Sticky)", "Float and Clear Properties", "Styled Navigation Bar",
    "CSS Pseudo-Classes (:hover, :active, :focus, :visited)", "CSS Pseudo-Elements (::before, ::after, ::first-letter)", "CSS Lists and Tables Styling",
    "Styled Registration Form using CSS", "CSS Flexbox Layout (Flex-Direction, Justify, Align)", "CSS Grid Layout (Grid Template Columns & Gap)",
    "Responsive Design using CSS Media Queries", "CSS 2D Transforms & Smooth Transitions", "CSS @keyframes Animations (Bounce, Pulse, Spin)",
    "Responsive Navigation Menu with Toggle", "Personal Portfolio Webpage Layout", "College Student Profile Card Layout",
    "Glassmorphism Login Page Design", "E-commerce Product Card Grid Layout", "Responsive Photo Gallery Layout",
    "Complete Website Homepage Layout", "CSS Inheritance & Specificity Rules", "Selector Types & Attribute Selectors",
    "Combinator Selectors (Descendant, Child, Sibling)", "CSS Custom Properties (Variables) & Themes", "Background Images, Cover, Contain & Parallax",
    "Linear, Radial & Conic CSS Gradients", "Box-Shadow & 3D Text-Shadow Effects", "Designing Shapes using Border-Radius",
    "Opacity, RGBA & HSLA Transparency", "CSS Overflow Properties (Visible, Hidden, Scroll)", "Z-Index & Stacking Context Hierarchy",
    "CSS Display Modes (Block, Inline, Flex, Grid)", "Visibility: Hidden vs Display: None vs Opacity: 0", "Pure CSS Multi-Level Dropdown Menu",
    "Image Hover Animation Effects", "Pure CSS Tooltips with Arrow Indicators", "CSS Button Hover Animations (Ripple & Glow)",
    "Interactive CSS Filters (Blur, Grayscale, Brightness)", "Object-Fit & Object-Position Demonstration", "Responsive Auto-Fit Image Gallery",
    "Card-Based Layout using Flexbox", "Admin Dashboard Layout using CSS Grid", "Two-Column Webpage Layout using CSS Grid",
    "Three-Column Webpage Layout using Flexbox", "Sticky Header Navigation Bar", "Fixed Sidebar Navigation Layout",
    "Multi-Column Responsive Footer Layout", "Responsive Login & Signup Dual-Tab Form", "Responsive Contact Form Layout",
    "College Website Homepage Layout", "Restaurant Website Layout & Menu", "E-commerce Online Shopping Store Catalog",
    "Travel Agency Website Homepage", "News & Blog Magazine Layout using CSS Grid", "Multi-Section Portfolio Website Layout",
    "CSS Grid Template Areas Layout", "Flexbox Alignment & Item Order Properties", "Responsive Grid Layout with Media Queries",
    "Mobile-First Responsive Web Design", "CSS Transition Timing & Delay Demonstration", "2D & 3D CSS Transforms (3D Card Flip)",
    "Multi-Stage Keyframe Animation Timeline", "Custom CSS Loading Spinners", "Sliding Card Carousel Animation in Pure CSS",
    "Pure CSS Modal Popup Dialog Design", "Dark Mode Toggle using CSS Variables", "Responsive Fluid Typography (clamp, rem, vw)",
    "CSS Functions: clamp(), min(), and max()", "Dynamic Calculations using CSS calc() Function", "Master Responsive Website Layout (HTML5, CSS3, Flexbox & Grid)"
]

for idx, title in enumerate(css_titles, 1):
    fn = f"{idx:02d}-css-program.html"
    css_files.append((fn, title, f"CSS Practical Experiment #{idx} demonstrating {title.lower()}"))

# 2. JS Files Listing Generator (105 Items)
js_files = []
js_topics = [
    # Core & Algorithmic (1-50)
    ("js-01-hello-world.html", "Hello World Program", "Display Hello World in console, alert, and DOM"),
    ("js-02-arithmetic-operations.html", "Arithmetic Operations", "Perform +, -, *, /, %, ** on two numbers"),
    ("js-03-largest-of-three.html", "Largest of Three Numbers", "Find the maximum of three input numbers"),
    ("js-04-even-or-odd.html", "Even or Odd Checker", "Check if an integer is even or odd"),
    ("js-05-positive-negative-zero.html", "Positive, Negative or Zero", "Check sign of a number"),
    ("js-06-factorial.html", "Factorial Calculator", "Find factorial of a number N!"),
    ("js-07-fibonacci-series.html", "Fibonacci Series Generator", "Generate Fibonacci sequence up to N terms"),
    ("js-08-prime-number.html", "Prime Number Checker", "Check whether a number is prime"),
    ("js-09-palindrome-number.html", "Palindrome Number Checker", "Check if a number reads same backwards"),
    ("js-10-reverse-number.html", "Reverse a Number", "Reverse integer digits"),
    ("js-11-sum-of-digits.html", "Sum of Digits", "Calculate sum of digits of a number"),
    ("js-12-array-min-max.html", "Array Largest & Smallest Element", "Find minimum and maximum element in an array"),
    ("js-13-sort-array.html", "Sort an Array", "Sort array elements in ascending and descending order"),
    ("js-14-array-sum-average.html", "Array Sum & Average", "Calculate total sum and mean average of array elements"),
    ("js-15-functions-demo.html", "JavaScript Functions Demonstration", "Declarations, expressions, parameters, return values"),
    ("js-16-arrow-functions.html", "Arrow Functions Demonstration", "ES6 arrow functions and concise syntax"),
    ("js-17-string-methods.html", "Strings & String Methods", "String manipulation using slice, replace, split, trim"),
    ("js-18-array-methods.html", "Arrays & Array Methods", "Array manipulation using push, pop, map, filter, reduce"),
    ("js-19-objects-demo.html", "JavaScript Objects Demonstration", "Object literals, properties, methods, Object.keys()"),
    ("js-20-date-math-objects.html", "Date & Math Objects", "Working with Date methods and Math functions"),
    ("js-21-es6-features.html", "ES6 Features (let, const, destructuring)", "Demonstrating let, const, template literals, destructuring"),
    ("js-22-spread-rest-operators.html", "Spread & Rest Operators", "Demonstrating spread syntax and rest parameters"),
    ("js-23-classes-objects.html", "Classes & Objects in JavaScript", "ES6 classes, constructors, methods, getters/setters"),
    ("js-24-class-inheritance.html", "Class Inheritance", "Demonstrating class inheritance using extends and super"),
    ("js-25-callbacks-promises-async.html", "Callbacks, Promises & Async/Await", "Asynchronous JavaScript execution demo"),
    ("js-26-fetch-api.html", "Fetch Data using Fetch API", "Fetching external API JSON data using fetch()"),
    ("js-27-dynamic-api-data.html", "Display Dynamic API Data", "Rendering API data dynamically as HTML UI cards"),
    ("js-28-swap-two-numbers.html", "Swap Two Numbers", "Swapping values with temporary variable and destructuring"),
    ("js-29-gcd-two-numbers.html", "Greatest Common Divisor (GCD)", "Finding GCD of two numbers using Euclidean algorithm"),
    ("js-30-lcm-two-numbers.html", "Least Common Multiple (LCM)", "Finding LCM of two numbers"),
    ("js-31-armstrong-number.html", "Armstrong Number Checker", "Check if a number is Armstrong (e.g. 153)"),
    ("js-32-perfect-number.html", "Perfect Number Checker", "Check if a number is Perfect (e.g. 6, 28)"),
    ("js-33-multiplication-table.html", "Multiplication Table Generator", "Generate multiplication table for a number"),
    ("js-34-power-of-number.html", "Power of a Number (Base^Exponent)", "Calculate power iteratively and using Math.pow()"),
    ("js-35-count-digits.html", "Count Digits in a Number", "Count total number of digits in an integer"),
    ("js-36-second-largest-array.html", "Second Largest Array Element", "Find second-largest element in an array"),
    ("js-37-remove-array-duplicates.html", "Remove Array Duplicates", "Remove duplicate elements using Set and filter()"),
    ("js-38-merge-two-arrays.html", "Merge Two Arrays", "Merge two arrays and remove duplicate entries"),
    ("js-39-array-element-frequency.html", "Array Element Frequency", "Count frequency of each element in an array"),
    ("js-40-common-elements-arrays.html", "Common Elements in Two Arrays", "Find intersection of elements in two arrays"),
    ("js-41-reverse-string.html", "Reverse a String", "Reverse string characters using loop & methods"),
    ("js-42-palindrome-string.html", "Palindrome String Checker", "Check if string is a palindrome ignoring case"),
    ("js-43-count-vowels-consonants.html", "Count Vowels & Consonants", "Count vowels, consonants, and special characters"),
    ("js-44-count-words-string.html", "Count Words in a String", "Count total number of words in text"),
    ("js-45-character-frequency-string.html", "Character Frequency in String", "Frequency table of characters in input text"),
    ("js-46-regular-expressions-demo.html", "Regular Expressions (Regex)", "Demonstrate test(), match(), replace(), and search()"),
    ("js-47-regex-email-validation.html", "Email Regex Validation", "Validate email address format using Regular Expression"),
    ("js-48-localstorage-demo.html", "localStorage Data Persistence", "Store, retrieve, and clear data in localStorage"),
    ("js-49-responsive-login-validation.html", "Responsive Login Form Validation", "Login form with realtime JS input validation"),
    ("js-50-complete-interactive-webpage.html", "Complete Interactive Webpage", "Interactive webpage with counter, theme, item list"),
    
    # DOM Manipulation (51-65)
    ("js-dom-01-add-elements.html", "Add New DOM Elements Dynamically", "Create and append new elements using createElement"),
    ("js-dom-02-remove-elements.html", "Remove HTML Elements Dynamically", "Remove elements from DOM using remove()"),
    ("js-dom-03-change-styles.html", "Change CSS Styles using JavaScript", "Modify style properties dynamically"),
    ("js-dom-04-change-multiple-elements.html", "Change Multiple Elements Simultaneously", "Batch update elements using querySelectorAll"),
    ("js-dom-05-getelementbyid-class.html", "getElementById vs getElementsByClassName", "DOM element selection demonstration"),
    ("js-dom-06-queryselector-all.html", "querySelector vs querySelectorAll", "Modern CSS selector DOM querying"),
    ("js-dom-07-toggle-classes.html", "Add & Remove CSS Classes Dynamically", "Manipulate classList add, remove, and toggle"),
    ("js-dom-08-dynamic-table.html", "Dynamic Table Generator", "Generate dynamic HTML table from JavaScript data"),
    ("js-dom-09-add-delete-table-rows.html", "Add & Delete Table Rows", "Insert and remove table rows dynamically"),
    ("js-dom-10-table-search-filter.html", "Table Record Search & Filter", "Realtime live search filter on table rows"),
    ("js-dom-11-character-counter.html", "Live Character Counter", "Textarea character counter with limit warning"),
    ("js-dom-12-password-show-hide.html", "Password Show/Hide Feature", "Toggle password visibility button"),
    ("js-dom-13-dynamic-dropdown.html", "Dynamic Dropdown List", "Populate select dropdown options from array"),
    ("js-dom-14-dependent-dropdown.html", "Dependent Dropdown (Country->State->City)", "Cascading select dropdowns"),
    ("js-dom-15-image-slideshow.html", "Image Carousel / Slideshow", "Interactive image slideshow with next/prev buttons"),
    
    # Events (66-73)
    ("js-event-01-mouse-events.html", "Mouse Events Demonstration", "Click, dblclick, mouseover, mouseout, mousemove"),
    ("js-event-02-keyboard-events.html", "Keyboard Events Demonstration", "Keydown, keyup, key character logger"),
    ("js-event-03-form-events.html", "Form Events Demonstration", "Submit, change, focus, blur, input event handling"),
    ("js-event-04-double-click-event.html", "Double-Click Event Handler", "Respond to dblclick event interactions"),
    ("js-event-05-bubbling-capturing.html", "Event Bubbling & Event Capturing", "Event propagation flow visual demonstration"),
    ("js-event-06-event-delegation.html", "Event Delegation Demonstration", "Handling events on dynamic child elements via parent"),
    ("js-event-07-keyboard-game.html", "Keyboard-Controlled Mini Game", "Move character box around screen with Arrow keys"),
    ("js-event-08-drag-and-drop.html", "Drag-and-Drop Application", "Drag and drop items between containers"),
    
    # Forms & Validation (74-80)
    ("js-form-01-student-registration.html", "Student Registration Form Validation", "Full client-side registration form validation"),
    ("js-form-02-login-validation.html", "Login Form Username & Password Validation", "Validate login credentials format"),
    ("js-form-03-password-strength.html", "Password Strength Checker", "Realtime password complexity score meter"),
    ("js-form-04-signup-confirmation.html", "Signup Form Password Confirmation", "Confirm password match validation"),
    ("js-form-05-feedback-form.html", "Feedback Form with Star Rating", "Interactive feedback form with validation"),
    ("js-form-06-college-admission-form.html", "College Admission Form Validation", "Validate admission form input fields"),
    ("js-form-07-dynamic-error-messages.html", "Dynamic Inline Validation Messages", "Show validation errors without page reload"),
    
    # Browser & Web Storage (81-88)
    ("js-browser-01-window-object.html", "Window Object Demonstration", "Alert, confirm, prompt, innerWidth, timers"),
    ("js-browser-02-navigator-object.html", "Navigator Object Demonstration", "UserAgent, platform, online status, language"),
    ("js-browser-03-location-object.html", "Location Object Demonstration", "Href, pathname, reload, assign methods"),
    ("js-browser-04-history-object.html", "History Object Demonstration", "History back, forward, go, length properties"),
    ("js-browser-05-localstorage-app.html", "localStorage Key-Value Store Manager", "Set, get, remove items in localStorage"),
    ("js-browser-06-sessionstorage-app.html", "sessionStorage Temporary Data Manager", "Session-based temporary data storage"),
    ("js-browser-07-shopping-cart-storage.html", "Shopping Cart with localStorage", "Persistent e-commerce cart using localStorage"),
    ("js-browser-08-theme-switcher-storage.html", "Theme Switcher with localStorage", "Persistent Dark/Light mode theme switcher"),
    
    # Mini Projects (89-105)
    ("mini-01-digital-calculator.html", "Digital Calculator App", "GUI Digital Calculator with +, -, *, /, AC buttons"),
    ("mini-02-digital-clock.html", "Digital Clock App", "Live clock with time, seconds, date, 12h/24h toggle"),
    ("mini-03-stopwatch.html", "Stopwatch App", "Precise stopwatch with start, pause, lap, and reset"),
    ("mini-04-countdown-timer.html", "Countdown Timer App", "Customizable timer with alarm alert"),
    ("mini-05-todo-list.html", "To-Do List Application", "Feature-rich to-do list with filter & localStorage"),
    ("mini-06-weather-app.html", "Weather Application using API", "Fetch live weather details for cities using Weather API"),
    ("mini-07-quiz-app.html", "Interactive Quiz Application", "Multiple choice quiz with score counter & timer"),
    ("mini-08-number-guessing-game.html", "Number Guessing Game", "Random number guessing game (1-100) with hints"),
    ("mini-09-tic-tac-toe.html", "Tic-Tac-Toe Game", "Two-player Tic-Tac-Toe game with win detection"),
    ("mini-10-expense-tracker.html", "Personal Expense Tracker", "Track income, expenses, categories, total balance"),
    ("mini-11-grade-calculator.html", "Student Grade & Marks Calculator", "Calculate marks for 5 subjects, total, grade A/B/C/F"),
    ("mini-12-shopping-cart.html", "E-Commerce Shopping Cart", "Product listing, add to cart, quantity change, checkout"),
    ("mini-13-notes-app.html", "Notes Application", "Create, edit, search, and delete notes with localStorage"),
    ("mini-14-password-generator.html", "Random Password Generator", "Generate secure random passwords with options & copy button"),
    ("mini-15-bmi-calculator.html", "BMI Calculator App", "Calculate Body Mass Index (BMI) with health status bar"),
    ("mini-16-currency-converter.html", "Currency Converter App", "Live currency conversion rates calculator"),
    ("mini-17-interactive-portfolio.html", "Interactive Portfolio Website", "Complete portfolio with dark mode, projects filter & contact form")
]

for fn, name, desc in js_topics:
    js_files.append((fn, name, desc))

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

# Write css/index.html
with open(os.path.join(ROOT, "css", "index.html"), "w", encoding="utf-8") as f:
    f.write(make_list_page("CSS Programs", "CSS", css_files))

# Write javascript/index.html
with open(os.path.join(ROOT, "javascript", "index.html"), "w", encoding="utf-8") as f:
    f.write(make_list_page("JavaScript Programs", "JavaScript", js_files))

print("Created css/index.html and javascript/index.html")

# Write README.md
README_CONTENT = """# HTML, CSS & JavaScript Practical Assignment Website

### Student Metadata
- **Student Name:** Gandikota Shaavanth
- **Register Number:** 250200412
- **Class / Section:** 2nd year / 5th section
- **Subject:** Web Technology and Internet Programming
- **Assignment Title:** HTML, CSS & JavaScript – Practical Assignment

---

## 📊 Summary of Completed Programs

| Category | Description | Programs Completed |
| :--- | :--- | :--- |
| **HTML Programs** | Core HTML tags, text formatting, lists, tables with merged cells, forms, multimedia audio/video, semantic structure, timetable, CSS integration, Bootstrap components, portfolio | **15** |
| **CSS Programs** | Inline/internal/external styling, selectors, box model, Flexbox, CSS Grid layouts, animations, transitions, custom variables, filters, responsive websites, dropdowns, forms | **75** |
| **JavaScript Programs** | Fundamental algorithms (1-50), DOM manipulation (15), Event handlers (8), Forms & Validation (7), Browser objects & Storage (8), Mini Projects (17) | **105** |
| **Total Programs** | **Complete Practical Assignment Collection** | **195** |

---

## 📁 Project Directory Structure

```
project/
│
├── index.html                            # Main Dashboard (3 Category Cards: HTML, CSS, JavaScript)
├── README.md                             # Assignment Info, Student Metadata, Total Counts
│
├── assets/
│   ├── css/
│   │   └── style.css                     # Master Unified Stylesheet
│   └── images/
│
├── html/
│   ├── index.html                        # HTML Programs List Page
│   ├── 01-basic-webpage.html
│   ├── ... (15 HTML files)
│   └── 15-simple-portfolio.html
│
├── css/
│   ├── index.html                        # CSS Programs List Page
│   ├── 01-css-program.html
│   ├── ... (75 CSS files)
│   └── 75-css-program.html
│
└── javascript/
    ├── index.html                        # JavaScript Programs List Page
    ├── js-01-hello-world.html
    ├── ... (105 JS files)
    └── mini-17-interactive-portfolio.html
```

---

## 🚀 Navigation & Testing Instructions

1. Open `index.html` in any modern web browser (Google Chrome, Mozilla Firefox, Microsoft Edge, Safari).
2. Click on any of the 3 category cards (**View HTML Programs**, **View CSS Programs**, **View JavaScript Programs**) to navigate to the respective experiment listing page.
3. Use the search bar on any listing page to instantly filter programs by topic or title.
4. Click **View Program** to inspect the live demonstration and implementation of any experiment.
5. Use the top navigation bar (`🏠 Home Dashboard` and `🔙 Back to Programs`) to navigate seamlessly through all 195 programs without typing file paths.
"""

with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8") as f:
    f.write(README_CONTENT)

print("Created README.md file.")
