import os

ROOT = r"c:\Users\Lenovo\OneDrive\Desktop\html"
JS_DIR = os.path.join(ROOT, "javascript")
os.makedirs(JS_DIR, exist_ok=True)

# Categorized JS Programs structure
categories = [
    {
        "id": "mini-projects",
        "title": "🚀 Mini Projects",
        "badge": "17 Programs",
        "desc": "Complete interactive web applications built with HTML, CSS, and JavaScript",
        "items": [
            ("digital-calculator.html", "Digital Calculator Mini Project", "Complete GUI digital calculator with buttons and screen display"),
            ("digital-clock.html", "Digital Clock Mini Project", "Live digital clock with seconds, date, and 12h/24h toggle"),
            ("stopwatch.html", "Stopwatch Mini Project", "Precise stopwatch application with start, pause, lap, and reset"),
            ("countdown-timer.html", "Countdown Timer Mini Project", "Customizable timer with start and reset buttons"),
            ("todo-list.html", "To-Do List Application", "Interactive task list with add, check complete, and delete actions"),
            ("weather-app.html", "Weather Application using API", "Fetch live weather forecast for cities using Open-Meteo API"),
            ("quiz-app.html", "Quiz Application Mini Project", "Interactive multiple choice quiz with score counter and timer"),
            ("number-guessing-game.html", "Number Guessing Game", "Random number guessing game (1-100) with attempts & hints"),
            ("tic-tac-toe.html", "Tic-Tac-Toe Game Mini Project", "Two-player Tic-Tac-Toe game with win detection"),
            ("expense-tracker.html", "Simple Expense Tracker", "Track income, expenses, categories, total balance"),
            ("student-marks-calculator.html", "Student Marks/Grade Calculator", "Calculate subject marks, total, percentage, GPA, grade"),
            ("simple-shopping-cart.html", "Simple Shopping Cart Mini Project", "Product catalog with add to cart, item quantities, subtotal"),
            ("notes-app.html", "Notes Application using localStorage", "Notes manager with local storage persistence"),
            ("random-password-generator.html", "Random Password Generator", "Generate secure random passwords with options & copy button"),
            ("bmi-calculator.html", "BMI Calculator Mini Project", "Calculate Body Mass Index (BMI) with health status bar"),
            ("currency-converter.html", "Currency Converter using API", "Live currency conversion rates calculator"),
            ("interactive-portfolio.html", "Complete Interactive Portfolio Website", "Portfolio website with HTML, CSS, JavaScript, and project filter")
        ]
    },
    {
        "id": "dom-manipulation",
        "title": "🛠️ DOM Manipulation",
        "badge": "15 Programs",
        "desc": "Dynamic element creation, removal, styling, querying, and dynamic table operations",
        "items": [
            ("js-066-dom-add-elements.html", "Add New Elements Dynamically", "Create and append new DOM elements dynamically using createElement"),
            ("js-067-dom-remove-elements.html", "Remove HTML Elements Dynamically", "Dynamically remove elements from the DOM using remove()"),
            ("js-068-dom-change-css-styles.html", "Change CSS Styles using JavaScript", "Modify style properties dynamically using element.style"),
            ("js-069-dom-change-multiple-elements.html", "Change Multiple Elements Simultaneously", "Batch update multiple elements using querySelectorAll"),
            ("js-070-dom-getelementbyid-classname.html", "getElementById vs getElementsByClassName", "Demonstrate DOM element selection methods"),
            ("js-071-dom-queryselector-all.html", "querySelector vs querySelectorAll", "Modern CSS selector DOM querying demonstration"),
            ("js-072-dom-toggle-css-classes.html", "Create and Remove CSS Classes Dynamically", "Manipulate classList add, remove, and toggle"),
            ("js-073-dom-dynamic-table.html", "Dynamic Table using JavaScript", "Generate dynamic HTML table from JavaScript JSON data"),
            ("js-074-dom-add-delete-table-rows.html", "Add and Delete Rows from a Table", "Insert and remove table rows dynamically"),
            ("js-075-dom-table-search-filter.html", "Search/Filter Table Records", "Realtime live search filter on table rows"),
            ("js-076-dom-character-counter.html", "Live Character Counter for Textarea", "Textarea character counter with limit warning"),
            ("js-077-dom-password-show-hide.html", "Password Show/Hide Feature", "Toggle password visibility button"),
            ("js-078-dom-dynamic-dropdown.html", "Dynamic Dropdown List", "Populate select dropdown options dynamically from array"),
            ("js-079-dom-dependent-dropdown.html", "Dependent Dropdown (Country->State->City)", "Cascading select dropdowns"),
            ("js-080-dom-image-slideshow.html", "Image Slideshow/Carousel using JavaScript", "Interactive image slideshow with next/prev buttons")
        ]
    },
    {
        "id": "events",
        "title": "⚡ JavaScript Events",
        "badge": "8 Programs",
        "desc": "Mouse, keyboard, form events, double-click, event bubbling/capturing, and drag-and-drop",
        "items": [
            ("js-081-events-mouse.html", "Mouse Events using JavaScript", "Demonstrate click, dblclick, mouseover, mouseout, mousemove"),
            ("js-082-events-keyboard.html", "Keyboard Events using JavaScript", "Demonstrate keydown, keyup, and keycode logger"),
            ("js-083-events-form.html", "Form Events (submit, change, focus, blur)", "Demonstrate form input event handling"),
            ("js-084-events-double-click.html", "Respond to Double-Click Events", "Create a webpage that responds to dblclick events"),
            ("js-085-events-bubbling-capturing.html", "Event Bubbling and Event Capturing", "Event propagation flow visual demonstration"),
            ("js-086-events-delegation.html", "Event Delegation", "Demonstrate handling events on dynamic child elements via parent"),
            ("js-087-events-keyboard-game.html", "Keyboard-Controlled Webpage/Game", "Move character box around screen with Arrow keys"),
            ("js-088-events-drag-and-drop.html", "Drag-and-Drop Application", "Drag and drop items between containers using HTML5 Drag API")
        ]
    },
    {
        "id": "forms-validation",
        "title": "📝 Forms & Validation",
        "badge": "7 Programs",
        "desc": "Client-side validation, password strength meters, confirmation checks, and error rendering",
        "items": [
            ("js-089-form-student-registration.html", "Student Registration Form Validation", "Create a student registration form with JavaScript validation"),
            ("js-090-form-login-validation.html", "Login Form Username & Password Validation", "Create a login form with username and password validation"),
            ("js-091-form-password-strength.html", "Password Strength Checker", "Realtime password complexity score meter"),
            ("js-092-form-signup-confirmation.html", "Signup Form with Password Confirmation", "Confirm password match validation"),
            ("js-093-form-feedback-validation.html", "Feedback Form with Validation", "Feedback form with star rating and validation"),
            ("js-094-form-college-admission.html", "College Admission Form Validation", "Validate admission form input fields"),
            ("js-095-form-dynamic-error-messages.html", "Display Dynamic Error Messages", "Display validation error messages dynamically without reloading")
        ]
    },
    {
        "id": "browser-objects",
        "title": "🌐 Browser Objects & Features",
        "badge": "4 Programs",
        "desc": "Window, Navigator, Location, and History browser API objects",
        "items": [
            ("js-096-browser-window-object.html", "Window Object", "Demonstrate alert, confirm, prompt, innerWidth, and timers"),
            ("js-097-browser-navigator-object.html", "Navigator Object", "Demonstrate userAgent, platform, online status, language"),
            ("js-098-browser-location-object.html", "Location Object", "Demonstrate href, pathname, reload, assign methods"),
            ("js-099-browser-history-object.html", "History Object", "Demonstrate history back, forward, go, length properties")
        ]
    },
    {
        "id": "web-storage",
        "title": "💾 Web Storage",
        "badge": "4 Programs",
        "desc": "Data persistence using localStorage and sessionStorage APIs",
        "items": [
            ("js-100-storage-localstorage.html", "Program using localStorage", "Store, retrieve, and clear items in localStorage"),
            ("js-101-storage-sessionstorage.html", "Program using sessionStorage", "Session-based temporary data storage manager"),
            ("js-102-storage-shopping-cart.html", "Shopping Cart using localStorage", "Persistent e-commerce cart using localStorage"),
            ("js-103-storage-theme-switcher.html", "Theme Switcher using localStorage", "Persistent Dark/Light mode theme switcher")
        ]
    },
    {
        "id": "general-js",
        "title": "📌 General & Algorithmic JavaScript",
        "badge": "65 Programs",
        "desc": "Basic programs, control structures, ES6 features, array methods, and algorithmic logic",
        "items": [
            ("js-001-hello-world.html", "Display Hello World", "Write a JavaScript program to display 'Hello World'"),
            ("js-002-arithmetic-operations.html", "Perform Arithmetic Operations", "Write a JavaScript program to perform arithmetic operations"),
            ("js-003-largest-of-three.html", "Largest of Three Numbers", "Write a program to find the largest of three numbers"),
            ("js-004-even-or-odd.html", "Even or Odd Checker", "Write a program to check whether a number is even or odd"),
            ("js-005-positive-negative-zero.html", "Positive, Negative, or Zero", "Write a program to check whether a number is positive, negative, or zero"),
            ("js-006-factorial.html", "Factorial of a Number", "Write a program to find the factorial of a number"),
            ("js-007-fibonacci-series.html", "Fibonacci Series Generator", "Write a program to generate the Fibonacci series"),
            ("js-008-prime-number.html", "Prime Number Checker", "Write a program to check whether a number is prime"),
            ("js-009-palindrome-number.html", "Palindrome Number Checker", "Write a program to check whether a number is a palindrome"),
            ("js-010-reverse-number.html", "Reverse a Number", "Write a program to reverse a number"),
            ("js-011-sum-of-digits.html", "Sum of Digits", "Write a program to find the sum of digits of a number"),
            ("js-012-array-min-max.html", "Largest and Smallest Array Element", "Write a program to find the largest and smallest element in an array"),
            ("js-013-sort-array.html", "Sort an Array", "Write a program to sort an array"),
            ("js-014-array-sum-average.html", "Sum and Average of Array Elements", "Write a program to find the sum and average of array elements"),
            ("js-015-functions-demo.html", "JavaScript Functions", "Write a program to demonstrate JavaScript functions"),
            ("js-016-arrow-functions.html", "Arrow Functions", "Write a program using arrow functions"),
            ("js-017-string-methods.html", "Strings and String Methods", "Write a program demonstrating strings and string methods"),
            ("js-018-array-methods.html", "Arrays and Array Methods", "Write a program demonstrating arrays and array methods"),
            ("js-019-objects-demo.html", "Objects in JavaScript", "Write a program demonstrating objects in JavaScript"),
            ("js-020-date-math-objects.html", "Date and Math Objects", "Write a program demonstrating Date and Math objects"),
            ("js-021-change-text-js.html", "Change Text using JavaScript", "Create a webpage that changes text using JavaScript"),
            ("js-022-change-bg-color-js.html", "Change Background Color using JavaScript", "Change the background color of a webpage using JavaScript"),
            ("js-023-button-click-event.html", "Button Click Event", "Create a button click event using JavaScript"),
            ("js-024-show-hide-element.html", "Show/Hide HTML Element", "Create a program to show/hide an HTML element"),
            ("js-025-change-image-js.html", "Change Image on Button Click", "Create a program to change an image when a button is clicked"),
            ("js-026-digital-clock-dom.html", "Digital Clock (DOM)", "Create a digital clock using JavaScript"),
            ("js-027-simple-calculator-dom.html", "Simple Calculator (DOM)", "Create a simple calculator using HTML, CSS, and JavaScript"),
            ("js-028-number-guessing-dom.html", "Number Guessing Game (DOM)", "Create a number guessing game"),
            ("js-029-form-validation-basic.html", "Form Validation Program", "Create a form validation program"),
            ("js-030-validate-user-fields.html", "Validate Name, Email, Phone & Password", "Validate name, email, phone number, and password using JavaScript"),
            ("js-031-todo-list-dom.html", "To-Do List (DOM)", "Create a to-do list using JavaScript"),
            ("js-032-quiz-app-dom.html", "Simple Quiz Application (DOM)", "Create a simple quiz application"),
            ("js-033-counter-app.html", "Counter Application", "Create a counter application with increment and decrement buttons"),
            ("js-034-stopwatch-dom.html", "Stopwatch (DOM)", "Create a stopwatch using JavaScript"),
            ("js-035-countdown-timer-dom.html", "Countdown Timer (DOM)", "Create a countdown timer using JavaScript"),
            ("js-036-es6-features.html", "ES6 let, const, template literals, destructuring", "Demonstrate ES6 let, const, template literals, and destructuring"),
            ("js-037-spread-rest-operators.html", "Spread and Rest Operators", "Demonstrate spread and rest operators"),
            ("js-038-classes-objects.html", "Classes and Objects", "Demonstrate classes and objects"),
            ("js-039-class-inheritance.html", "Inheritance in JavaScript", "Demonstrate inheritance in JavaScript"),
            ("js-040-callbacks-promises-async.html", "Callbacks, Promises, and Async/Await", "Demonstrate callbacks, promises, and async/await"),
            ("js-041-fetch-api.html", "Fetch Data using Fetch API", "Fetch data from an API using Fetch API"),
            ("js-042-display-api-data.html", "Display API Data Dynamically", "Display API data dynamically on a webpage"),
            ("js-043-localstorage-demo.html", "Store and Retrieve Data in LocalStorage", "Store and retrieve data using localStorage"),
            ("js-044-responsive-login-validation.html", "Responsive Login Form with Validation", "Create a responsive login form with JavaScript validation"),
            ("js-045-complete-interactive-webpage.html", "Complete Interactive Webpage", "Create a complete interactive webpage using HTML, CSS, and JavaScript"),
            ("js-046-swap-two-numbers.html", "Swap Two Numbers", "Write a JavaScript program to swap two numbers"),
            ("js-047-gcd-two-numbers.html", "GCD of Two Numbers", "Write a program to find the greatest common divisor (GCD) of two numbers"),
            ("js-048-lcm-two-numbers.html", "LCM of Two Numbers", "Write a program to find the least common multiple (LCM) of two numbers"),
            ("js-049-armstrong-number.html", "Armstrong Number Checker", "Write a program to check whether a number is an Armstrong number"),
            ("js-050-perfect-number.html", "Perfect Number Checker", "Write a program to check whether a number is a perfect number"),
            ("js-051-multiplication-table.html", "Multiplication Table Generator", "Write a program to generate the multiplication table of a given number"),
            ("js-052-power-of-number.html", "Power of a Number", "Write a program to calculate the power of a number"),
            ("js-053-count-digits.html", "Count Digits in a Number", "Write a program to count the number of digits in a number"),
            ("js-054-second-largest-array.html", "Second-Largest Element in Array", "Write a program to find the second-largest element in an array"),
            ("js-055-remove-array-duplicates.html", "Remove Duplicate Elements from Array", "Write a program to remove duplicate elements from an array"),
            ("js-056-merge-two-arrays.html", "Merge Two Arrays", "Write a program to merge two arrays"),
            ("js-057-array-element-frequency.html", "Frequency of Array Elements", "Write a program to find the frequency of each element in an array"),
            ("js-058-common-elements-arrays.html", "Common Elements in Two Arrays", "Write a program to find common elements in two arrays"),
            ("js-059-reverse-string.html", "Reverse a String", "Write a program to reverse a string"),
            ("js-060-palindrome-string.html", "Palindrome String Checker", "Write a program to check whether a string is a palindrome"),
            ("js-061-count-vowels-consonants.html", "Count Vowels and Consonants", "Write a program to count vowels and consonants in a string"),
            ("js-062-count-words-string.html", "Count Number of Words in a String", "Write a program to count the number of words in a string"),
            ("js-063-character-frequency-string.html", "Frequency of Characters in String", "Write a program to find the frequency of characters in a string"),
            ("js-064-regular-expressions-demo.html", "Regular Expressions in JavaScript", "Write a program to demonstrate regular expressions in JavaScript"),
            ("js-065-validate-email-regex.html", "Validate Email using Regex", "Write a program to validate an email address using a regular expression")
        ]
    }
]

# Generate JavaScript index.html with distinct category blocks
blocks_html = ""
tab_buttons = "<button class='tab-btn active' onclick='filterTab(\"all\")'>All Categories (122)</button>"

total_js_count = sum(len(c["items"]) for c in categories)

for cat in categories:
    cat_id = cat['id']
    cat_title = cat['title']
    cat_count = len(cat['items'])
    tab_buttons += f"<button class='tab-btn' onclick='filterTab(\"{cat_id}\")'>{cat_title} ({cat_count})</button>"
    
    ol_items = ""
    for idx, (fn, name, desc) in enumerate(cat["items"], 1):
        ol_items += f"""
        <li class="prog-ol-item" data-cat="{cat_id}">
            <a href="{fn}" class="prog-ol-link">
                <span class="link-title">{name}</span>
                <span class="link-desc">{desc}</span>
            </a>
        </li>"""
        
    blocks_html += f"""
    <div class="category-block" id="block-{cat_id}">
        <div class="category-header">
            <h2 class="category-title">{cat_title}</h2>
            <span class="category-badge">{cat['badge']}</span>
        </div>
        <p class="category-desc">{cat['desc']}</p>
        <ol class="prog-ol-list">
            {ol_items}
        </ol>
    </div>"""

JS_INDEX_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Programs - Practical Assignment</title>
    <link rel="stylesheet" href="../assets/css/style.css">
    <style>
        .category-tabs {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.6rem;
            margin-bottom: 2rem;
        }}
        .tab-btn {{
            padding: 0.55rem 1.1rem;
            background: #ffffff;
            color: var(--text-main);
            border: 1px solid var(--border);
            border-radius: 9999px;
            font-weight: 600;
            font-size: 0.875rem;
            cursor: pointer;
            transition: all 0.25s ease;
            box-shadow: var(--shadow-sm);
        }}
        .tab-btn:hover, .tab-btn.active {{
            background: var(--primary-gradient);
            color: #ffffff;
            border-color: transparent;
            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
        }}
        .category-block {{
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(8px);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 2rem;
            margin-bottom: 2.5rem;
            box-shadow: var(--shadow-md);
        }}
        .category-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #f1f5f9;
            padding-bottom: 0.75rem;
            margin-bottom: 0.5rem;
        }}
        .category-title {{
            font-size: 1.5rem;
            font-weight: 800;
            color: var(--primary);
        }}
        .category-badge {{
            font-size: 0.85rem;
            font-weight: 700;
            background: #e0e7ff;
            color: var(--primary);
            padding: 0.3rem 0.8rem;
            border-radius: 9999px;
        }}
        .category-desc {{
            color: var(--text-muted);
            font-size: 0.95rem;
            margin-bottom: 1.2rem;
        }}
        .prog-ol-list {{
            list-style-position: inside;
            padding: 0;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
            gap: 1.2rem;
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
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--primary);
        }}
        .link-title:hover {{
            text-decoration: underline;
        }}
        .link-desc {{
            font-size: 0.85rem;
            color: var(--text-muted);
        }}
    </style>
</head>
<body>
    <header class="app-header">
        <h1>JavaScript Programs</h1>
        <p>Categorized Collection of {total_js_count} JavaScript Practical Experiments</p>
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
        <input type="text" id="searchBox" class="search-box" placeholder="🔍 Search JavaScript programs by title or keyword..." onkeyup="filterProgs()">
        
        <!-- Category Filter Tabs -->
        <div class="category-tabs">
            {tab_buttons}
        </div>

        <!-- Categorized Blocks -->
        <div id="blocksContainer">
            {blocks_html}
        </div>
    </main>

    <footer class="page-footer">
        <div class="footer-nav">
            <a href="../index.html" class="btn-secondary">Home</a>
            <a href="index.html" class="btn-secondary">Back to Programs</a>
        </div>
        <p>&copy; 2026 Practical Assignment Submission | Student: Gandikota Shaavanth (250200412)</p>
    </footer>

    <script>
        function filterTab(catId) {{
            const btns = document.querySelectorAll('.tab-btn');
            btns.forEach(b => b.classList.remove('active'));
            event.target.classList.add('active');

            const blocks = document.querySelectorAll('.category-block');
            blocks.forEach(block => {{
                if (catId === 'all') {{
                    block.style.display = 'block';
                }} else {{
                    block.style.display = (block.id === 'block-' + catId) ? 'block' : 'none';
                }}
            }});
        }}

        function filterProgs() {{
            const q = document.getElementById('searchBox').value.toLowerCase();
            const items = document.querySelectorAll('.prog-ol-item');
            const blocks = document.querySelectorAll('.category-block');

            items.forEach(item => {{
                const txt = item.innerText.toLowerCase();
                item.style.display = txt.includes(q) ? 'list-item' : 'none';
            }});

            // Hide empty category blocks when searching
            blocks.forEach(block => {{
                if (q === '') {{
                    block.style.display = 'block';
                }} else {{
                    const visibleItems = block.querySelectorAll('.prog-ol-item[style*="display: list-item"], .prog-ol-item:not([style*="display: none"])');
                    block.style.display = visibleItems.length > 0 ? 'block' : 'none';
                }}
            }});
        }}
    </script>
</body>
</html>"""

with open(os.path.join(JS_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(JS_INDEX_HTML)

print("Updated javascript/index.html with visually separated category blocks and tabs!")
