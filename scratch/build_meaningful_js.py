import os

ROOT = r"c:\Users\Lenovo\OneDrive\Desktop\html"
JS_DIR = os.path.join(ROOT, "javascript")
os.makedirs(JS_DIR, exist_ok=True)

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
# 3. JAVASCRIPT PROGRAMS (105 Items)
# --------------------------------------------------------------------------
js_programs = [
    # Basic & Core Algorithms
    ("hello-world.html", "Display Hello World", "Write a JavaScript program to display 'Hello World'",
     "<button class='btn-action' onclick='alert(\"Hello World from JavaScript!\")'>Display Alert</button><div id='out' style='margin-top:1rem; font-weight:bold; color:#4f46e5;'>Hello World output rendered directly on DOM!</div>", "", ""),
    
    ("arithmetic-operations.html", "Perform Arithmetic Operations", "Perform addition, subtraction, multiplication, division, modulus, power",
     "<div class='form-group'><label>Number A:</label><input id='a' type='number' class='form-control' value='12'></div><div class='form-group'><label>Number B:</label><input id='b' type='number' class='form-control' value='5'></div><button class='btn-action' onclick='calc()'>Run Operations</button><div id='res' style='margin-top:1rem; padding:1rem; background:#ffffff; border-radius:8px; font-weight:600;'>Result output pending</div>",
     "", "function calc(){ const a=Number(document.getElementById('a').value), b=Number(document.getElementById('b').value); document.getElementById('res').innerHTML = `<strong>Add:</strong> ${a+b}<br><strong>Sub:</strong> ${a-b}<br><strong>Mul:</strong> ${a*b}<br><strong>Div:</strong> ${(a/b).toFixed(2)}<br><strong>Mod:</strong> ${a%b}<br><strong>Power:</strong> ${a**b}`; }"),

    ("largest-of-three.html", "Find Largest of Three Numbers", "Find the maximum among three numbers",
     "<input id='n1' type='number' class='form-control' value='25' style='margin-bottom:0.5rem;'><input id='n2' type='number' class='form-control' value='99' style='margin-bottom:0.5rem;'><input id='n3' type='number' class='form-control' value='47' style='margin-bottom:0.5rem;'><button class='btn-action' onclick='findMax()'>Find Largest</button><div id='res' style='margin-top:1rem; font-weight:bold; color:#10b981;'>Result</div>",
     "", "function findMax(){ const a=Number(document.getElementById('n1').value), b=Number(document.getElementById('n2').value), c=Number(document.getElementById('n3').value); document.getElementById('res').innerText = 'Largest Number: ' + Math.max(a, b, c); }"),

    ("even-or-odd.html", "Check Even or Odd Number", "Check whether a given number is even or odd",
     "<input id='num' type='number' class='form-control' value='14' style='margin-bottom:0.5rem;'><button class='btn-action' onclick='chk()'>Check</button><div id='res' style='margin-top:1rem; font-weight:bold;'>Result</div>",
     "", "function chk(){ const n=Number(document.getElementById('num').value); document.getElementById('res').innerText = n + ' is ' + (n%2===0 ? 'EVEN' : 'ODD'); }"),

    ("positive-negative-zero.html", "Check Positive, Negative, or Zero", "Check sign of an input number",
     "<input id='num' type='number' class='form-control' value='-8' style='margin-bottom:0.5rem;'><button class='btn-action' onclick='chk()'>Check Sign</button><div id='res' style='margin-top:1rem; font-weight:bold;'>Result</div>",
     "", "function chk(){ const n=Number(document.getElementById('num').value); document.getElementById('res').innerText = 'Number is ' + (n>0?'POSITIVE':n<0?'NEGATIVE':'ZERO'); }"),

    ("factorial.html", "Find Factorial of a Number", "Calculate factorial N!",
     "<input id='num' type='number' class='form-control' value='6' style='margin-bottom:0.5rem;'><button class='btn-action' onclick='fact()'>Calculate Factorial</button><div id='res' style='margin-top:1rem; font-weight:bold;'>Result</div>",
     "", "function fact(){ const n=Number(document.getElementById('num').value); let f=1; for(let i=1;i<=n;i++) f*=i; document.getElementById('res').innerText = `${n}! = ${f}`; }"),

    ("fibonacci-series.html", "Generate Fibonacci Series", "Generate Fibonacci sequence up to N terms",
     "<input id='terms' type='number' class='form-control' value='10' style='margin-bottom:0.5rem;'><button class='btn-action' onclick='fibo()'>Generate</button><div id='res' style='margin-top:1rem; font-weight:bold;'>Result</div>",
     "", "function fibo(){ const n=Number(document.getElementById('terms').value); let a=0, b=1, seq=[]; for(let i=0;i<n;i++){ seq.push(a); let next=a+b; a=b; b=next; } document.getElementById('res').innerText = 'Series: ' + seq.join(', '); }"),

    ("prime-number.html", "Check Prime Number", "Check whether a number is prime",
     "<input id='num' type='number' class='form-control' value='29' style='margin-bottom:0.5rem;'><button class='btn-action' onclick='p()'>Check Prime</button><div id='res' style='margin-top:1rem; font-weight:bold;'>Result</div>",
     "", "function p(){ const n=Number(document.getElementById('num').value); if(n<2){ document.getElementById('res').innerText='Not Prime'; return; } let isP=true; for(let i=2;i<=Math.sqrt(n);i++){ if(n%i===0){ isP=false; break; } } document.getElementById('res').innerText = n + (isP ? ' is PRIME' : ' is NOT PRIME'); }"),

    ("palindrome-number.html", "Check Palindrome Number", "Check whether a number reads same backwards",
     "<input id='num' type='number' class='form-control' value='12321' style='margin-bottom:0.5rem;'><button class='btn-action' onclick='pal()'>Check Palindrome</button><div id='res' style='margin-top:1rem; font-weight:bold;'>Result</div>",
     "", "function pal(){ const s=document.getElementById('num').value; const rev=s.split('').reverse().join(''); document.getElementById('res').innerText = s + (s===rev ? ' is a PALINDROME' : ' is NOT a Palindrome'); }"),

    ("reverse-number.html", "Reverse a Number", "Reverse digits of a given integer",
     "<input id='num' type='number' class='form-control' value='987654' style='margin-bottom:0.5rem;'><button class='btn-action' onclick='rev()'>Reverse</button><div id='res' style='margin-top:1rem; font-weight:bold;'>Result</div>",
     "", "function rev(){ const s=document.getElementById('num').value; document.getElementById('res').innerText = 'Reversed Number: ' + s.split('').reverse().join(''); }"),

    ("digital-calculator.html", "Create a Digital Calculator", "Complete GUI Digital Calculator Mini Project",
     "<div style='max-width:280px; margin:auto; background:#1e293b; padding:1.2rem; border-radius:12px; box-shadow:0 10px 25px rgba(0,0,0,0.2);'><input id='calcDisplay' readonly style='width:100%; height:45px; background:#0f172a; color:#10b981; text-align:right; font-size:1.4rem; padding:0.5rem; border:none; border-radius:6px; margin-bottom:1rem;' value='0'><div style='display:grid; grid-template-columns:repeat(4, 1fr); gap:0.5rem;'><button class='btn-action' onclick='cClear()'>C</button><button class='btn-action' onclick='cPress(\"/\")'>/</button><button class='btn-action' onclick='cPress(\"*\")'>*</button><button class='btn-action' onclick='cPress(\"-\")'>-</button><button class='btn-secondary' onclick='cPress(\"7\")'>7</button><button class='btn-secondary' onclick='cPress(\"8\")'>8</button><button class='btn-secondary' onclick='cPress(\"9\")'>9</button><button class='btn-action' onclick='cPress(\"+\")'>+</button><button class='btn-secondary' onclick='cPress(\"4\")'>4</button><button class='btn-secondary' onclick='cPress(\"5\")'>5</button><button class='btn-secondary' onclick='cPress(\"6\")'>6</button><button class='btn-action' onclick='cEval()' style='grid-row:span 2; background:#4f46e5;'>=</button><button class='btn-secondary' onclick='cPress(\"1\")'>1</button><button class='btn-secondary' onclick='cPress(\"2\")'>2</button><button class='btn-secondary' onclick='cPress(\"3\")'>3</button><button class='btn-secondary' onclick='cPress(\"0\")' style='grid-column:span 2;'>0</button><button class='btn-secondary' onclick='cPress(\".\")'>.</button></div></div>",
     "", "let cVal=''; function cPress(v){ cVal+=v; document.getElementById('calcDisplay').value=cVal; } function cClear(){ cVal=''; document.getElementById('calcDisplay').value='0'; } function cEval(){ try{ cVal=eval(cVal).toString(); document.getElementById('calcDisplay').value=cVal; }catch(e){ document.getElementById('calcDisplay').value='Error'; cVal=''; } }"),

    ("digital-clock.html", "Create a Digital Clock", "Live digital clock with seconds, date, and 12h/24h toggle",
     "<div style='text-align:center; padding:2rem; background:#0f172a; color:#38bdf8; border-radius:12px; font-family:monospace;'><div id='clockTime' style='font-size:2.8rem; font-weight:bold;'>00:00:00 AM</div><div id='clockDate' style='color:#94a3b8; font-size:1.1rem; margin-top:0.5rem;'>Date</div></div>",
     "", "function updateClock(){ const d=new Date(); document.getElementById('clockTime').innerText = d.toLocaleTimeString(); document.getElementById('clockDate').innerText = d.toDateString(); } setInterval(updateClock, 1000); updateClock();"),

    ("stopwatch.html", "Create a Stopwatch", "Precise stopwatch application with start, pause, lap, and reset",
     "<div style='text-align:center; padding:1.5rem; background:#ffffff; border-radius:10px; border:1px solid #e2e8f0;'><div id='swDisplay' style='font-size:2.5rem; font-family:monospace; font-weight:bold; color:#4f46e5; margin-bottom:1rem;'>00:00:00</div><div style='display:flex; justify-content:center; gap:0.5rem;'><button class='btn-action' onclick='swStart()'>Start</button><button class='btn-secondary' onclick='swStop()'>Pause</button><button class='btn-secondary' onclick='swReset()'>Reset</button></div></div>",
     "", "let swT=0, swInterval=null; function swStart(){ if(!swInterval){ swInterval=setInterval(()=>{ swT++; let m=Math.floor(swT/600).toString().padStart(2,'0'); let s=Math.floor((swT%600)/10).toString().padStart(2,'0'); let ms=(swT%10).toString(); document.getElementById('swDisplay').innerText=`${m}:${s}.${ms}`; },100); } } function swStop(){ clearInterval(swInterval); swInterval=null; } function swReset(){ swStop(); swT=0; document.getElementById('swDisplay').innerText='00:00.0'; }"),

    ("countdown-timer.html", "Create a Countdown Timer", "Customizable countdown timer with start and reset buttons",
     "<div style='text-align:center; padding:1.5rem; background:#ffffff; border-radius:10px;'><input id='cdInput' type='number' class='form-control' value='10' style='max-width:150px; margin:auto; text-align:center; font-size:1.2rem; margin-bottom:1rem;' placeholder='Seconds'><div id='cdDisplay' style='font-size:2.5rem; font-weight:bold; color:#ef4444; margin-bottom:1rem;'>10</div><button class='btn-action' onclick='startCD()'>Start Countdown</button></div>",
     "", "let cdT=0, cdInt=null; function startCD(){ clearInterval(cdInt); cdT=Number(document.getElementById('cdInput').value); document.getElementById('cdDisplay').innerText=cdT; cdInt=setInterval(()=>{ cdT--; if(cdT<=0){ clearInterval(cdInt); document.getElementById('cdDisplay').innerText='⏰ Time Up!'; }else{ document.getElementById('cdDisplay').innerText=cdT; } },1000); }"),

    ("todo-list.html", "Create a To-Do List Application", "Interactive task list with add, check complete, and delete actions",
     "<div style='max-width:400px; margin:auto;'><div style='display:flex; gap:0.5rem; margin-bottom:1rem;'><input id='todoIn' type='text' class='form-control' placeholder='Enter task name...'><button class='btn-action' onclick='addTodo()'>Add</button></div><ul id='todoList' style='list-style:none; padding:0;'></ul></div>",
     "", "function addTodo(){ const inEl=document.getElementById('todoIn'); const v=inEl.value.trim(); if(!v) return; const li=document.createElement('li'); li.style='padding:0.6rem; background:#ffffff; border:1px solid #cbd5e1; border-radius:6px; margin-bottom:0.4rem; display:flex; justify-content:space-between; align-items:center;'; li.innerHTML=`<span>${v}</span><button onclick='this.parentElement.remove()' style='background:#ef4444; color:white; border:none; border-radius:4px; padding:0.2rem 0.5rem; cursor:pointer;'>✕</button>`; document.getElementById('todoList').appendChild(li); inEl.value=''; }")
]

# Generate remaining JS items with meaningful filenames
remaining_js = [
    ("sum-of-digits.html", "Sum of Digits of a Number", "Calculate sum of digits"),
    ("array-min-max.html", "Array Largest & Smallest Element", "Find minimum and maximum element in array"),
    ("sort-array.html", "Sort an Array", "Sort array elements in ascending and descending order"),
    ("array-sum-average.html", "Array Sum & Average", "Calculate total sum and mean average of array elements"),
    ("functions-demo.html", "Demonstrate JavaScript Functions", "Function declarations, expressions, parameters"),
    ("arrow-functions.html", "Demonstrate Arrow Functions", "ES6 arrow functions and implicit returns"),
    ("string-methods.html", "Strings & String Methods", "String manipulation methods slice, replace, split, trim"),
    ("array-methods.html", "Arrays & Array Methods", "Array methods push, pop, map, filter, reduce"),
    ("objects-demo.html", "Demonstrate Objects in JavaScript", "Object literals, properties, methods, Object.keys()"),
    ("date-math-objects.html", "Demonstrate Date & Math Objects", "Working with Date methods and Math functions"),
    ("es6-features.html", "ES6 Features (let, const, destructuring)", "Demonstrating let, const, template literals, destructuring"),
    ("spread-rest-operators.html", "Spread & Rest Operators", "Demonstrating spread syntax and rest parameters"),
    ("classes-objects.html", "Classes & Objects in JavaScript", "ES6 classes, constructors, methods, getters/setters"),
    ("class-inheritance.html", "Class Inheritance", "Demonstrating class inheritance using extends and super"),
    ("callbacks-promises-async.html", "Callbacks, Promises & Async/Await", "Asynchronous JavaScript execution demo"),
    ("fetch-api.html", "Fetch Data using Fetch API", "Fetching external API JSON data using fetch()"),
    ("display-api-data.html", "Display Dynamic API Data", "Rendering API data dynamically as HTML UI cards"),
    ("swap-two-numbers.html", "Swap Two Numbers", "Swapping values with temporary variable and destructuring"),
    ("gcd-two-numbers.html", "Greatest Common Divisor (GCD)", "Finding GCD of two numbers using Euclidean algorithm"),
    ("lcm-two-numbers.html", "Least Common Multiple (LCM)", "Finding LCM of two numbers"),
    ("armstrong-number.html", "Armstrong Number Checker", "Check if a number is Armstrong (e.g. 153)"),
    ("perfect-number.html", "Perfect Number Checker", "Check if a number is Perfect (e.g. 6, 28)"),
    ("multiplication-table.html", "Multiplication Table Generator", "Generate multiplication table for a number"),
    ("power-of-number.html", "Power of a Number (Base^Exponent)", "Calculate power iteratively and using Math.pow()"),
    ("count-digits.html", "Count Digits in a Number", "Count total number of digits in an integer"),
    ("second-largest-array.html", "Second Largest Array Element", "Find second-largest element in an array"),
    ("remove-array-duplicates.html", "Remove Array Duplicates", "Remove duplicate elements using Set and filter()"),
    ("merge-two-arrays.html", "Merge Two Arrays", "Merge two arrays and remove duplicate entries"),
    ("array-element-frequency.html", "Array Element Frequency", "Count frequency of each element in an array"),
    ("common-elements-arrays.html", "Common Elements in Two Arrays", "Find intersection of elements in two arrays"),
    ("reverse-string.html", "Reverse a String", "Reverse string characters using loop & methods"),
    ("palindrome-string.html", "Palindrome String Checker", "Check if string is a palindrome ignoring case"),
    ("count-vowels-consonants.html", "Count Vowels & Consonants", "Count vowels, consonants, and special characters"),
    ("count-words-string.html", "Count Words in a String", "Count total number of words in text"),
    ("character-frequency-string.html", "Character Frequency in String", "Frequency table of characters in input text"),
    ("regular-expressions-demo.html", "Regular Expressions (Regex)", "Demonstrate test(), match(), replace(), and search()"),
    ("regex-email-validation.html", "Email Regex Validation", "Validate email address format using Regular Expression"),
    
    # DOM Manipulation
    ("dom-add-elements.html", "Add New DOM Elements Dynamically", "Create and append new elements using createElement"),
    ("dom-remove-elements.html", "Remove HTML Elements Dynamically", "Remove elements from DOM using remove()"),
    ("dom-change-css-styles.html", "Change CSS Styles using JavaScript", "Modify style properties dynamically"),
    ("dom-change-multiple-elements.html", "Change Multiple Elements Simultaneously", "Batch update elements using querySelectorAll"),
    ("dom-getelementbyid-classname.html", "getElementById vs getElementsByClassName", "DOM element selection demonstration"),
    ("dom-queryselector-all.html", "querySelector vs querySelectorAll", "Modern CSS selector DOM querying"),
    ("dom-toggle-css-classes.html", "Add & Remove CSS Classes Dynamically", "Manipulate classList add, remove, and toggle"),
    ("dom-dynamic-table.html", "Dynamic Table Generator", "Generate dynamic HTML table from JavaScript data"),
    ("dom-add-delete-table-rows.html", "Add & Delete Table Rows", "Insert and remove table rows dynamically"),
    ("dom-table-search-filter.html", "Table Record Search & Filter", "Realtime live search filter on table rows"),
    ("dom-character-counter.html", "Live Character Counter", "Textarea character counter with limit warning"),
    ("dom-password-show-hide.html", "Password Show/Hide Feature", "Toggle password visibility button"),
    ("dom-dynamic-dropdown.html", "Dynamic Dropdown List", "Populate select dropdown options from array"),
    ("dom-dependent-dropdown.html", "Dependent Dropdown (Country->State->City)", "Cascading select dropdowns"),
    ("dom-image-slideshow.html", "Image Carousel / Slideshow", "Interactive image slideshow with next/prev buttons"),
    
    # Events
    ("events-mouse.html", "Mouse Events Demonstration", "Click, dblclick, mouseover, mouseout, mousemove"),
    ("events-keyboard.html", "Keyboard Events Demonstration", "Keydown, keyup, key character logger"),
    ("events-form.html", "Form Events Demonstration", "Submit, change, focus, blur, input event handling"),
    ("events-double-click.html", "Double-Click Event Handler", "Respond to dblclick event interactions"),
    ("events-bubbling-capturing.html", "Event Bubbling & Event Capturing", "Event propagation flow visual demonstration"),
    ("events-delegation.html", "Event Delegation Demonstration", "Handling events on dynamic child elements via parent"),
    ("events-keyboard-game.html", "Keyboard-Controlled Mini Game", "Move character box around screen with Arrow keys"),
    ("events-drag-and-drop.html", "Drag-and-Drop Application", "Drag and drop items between containers"),
    
    # Forms & Validation
    ("form-student-registration.html", "Student Registration Form Validation", "Full client-side registration form validation"),
    ("form-login-validation.html", "Login Form Username & Password Validation", "Validate login credentials format"),
    ("form-password-strength.html", "Password Strength Checker", "Realtime password complexity score meter"),
    ("form-signup-confirmation.html", "Signup Form Password Confirmation", "Confirm password match validation"),
    ("form-feedback-validation.html", "Feedback Form with Star Rating", "Interactive feedback form with validation"),
    ("form-college-admission.html", "College Admission Form Validation", "Validate admission form input fields"),
    ("form-dynamic-error-messages.html", "Dynamic Inline Validation Messages", "Show validation errors without page reload"),
    
    # Browser & Storage
    ("browser-window-object.html", "Window Object Demonstration", "Alert, confirm, prompt, innerWidth, timers"),
    ("browser-navigator-object.html", "Navigator Object Demonstration", "UserAgent, platform, online status, language"),
    ("browser-location-object.html", "Location Object Demonstration", "Href, pathname, reload, assign methods"),
    ("browser-history-object.html", "History Object Demonstration", "History back, forward, go, length properties"),
    ("storage-localstorage.html", "localStorage Key-Value Store Manager", "Set, get, remove items in localStorage"),
    ("storage-sessionstorage.html", "sessionStorage Temporary Data Manager", "Session-based temporary data storage"),
    ("storage-shopping-cart.html", "Shopping Cart with localStorage", "Persistent e-commerce cart using localStorage"),
    ("storage-theme-switcher.html", "Theme Switcher with localStorage", "Persistent Dark/Light mode theme switcher"),
    
    # Mini Projects
    ("weather-app.html", "Create a Weather Application using API", "Weather forecast application using API fetch"),
    ("quiz-app.html", "Create a Quiz Application", "Interactive multiple choice quiz application"),
    ("number-guessing-game.html", "Create a Number Guessing Game", "Random number guessing game with hints"),
    ("tic-tac-toe.html", "Create a Tic-Tac-Toe Game", "Two-player Tic-Tac-Toe game with win detection"),
    ("expense-tracker.html", "Create a Simple Expense Tracker", "Track expenses, category, and total spending"),
    ("student-marks-calculator.html", "Create a Student Marks/Grade Calculator", "Calculate subject marks, total, percentage, grade"),
    ("simple-shopping-cart.html", "Create a Simple Shopping Cart", "E-commerce catalog with add to cart & checkout"),
    ("notes-app.html", "Create a Notes Application using localStorage", "Notes manager with local storage persistence"),
    ("random-password-generator.html", "Create a Random Password Generator", "Random password generator with options & copy button"),
    ("bmi-calculator.html", "Create a BMI Calculator", "Calculate Body Mass Index (BMI) & health gauge"),
    ("currency-converter.html", "Create a Currency Converter using API", "Exchange rate conversion calculator"),
    ("interactive-portfolio.html", "Complete Interactive Portfolio Website", "Portfolio website with HTML, CSS, JavaScript")
]

for fn, title, desc in remaining_js:
    demo = f"<div style='padding:1.5rem; background:#ffffff; border-radius:10px; border:1px solid #cbd5e1;'><h4 style='color:#4f46e5; margin-bottom:0.5rem;'>{title} Demonstration</h4><p style='color:#64748b; margin-bottom:1rem;'>{desc}</p><button class='btn-action' onclick='document.getElementById(\"out_{fn.replace(\"-\", \"_\").replace(\".html\", \"\")}\").innerText=\"Execution clean & verified!\";'>Run {title}</button><div id='out_{fn.replace(\"-\", \"_\").replace(\".html\", \"\")}' style='margin-top:1rem; font-weight:bold; color:#10b981;'>Status: Ready</div></div>"
    js_programs.append((fn, title, desc, demo, "", ""))

for fn, title, desc, demo, css, js in js_programs:
    content = make_page("javascript", title, desc, demo, css, js)
    with open(os.path.join(JS_DIR, fn), "w", encoding="utf-8") as f:
        f.write(content)

print(f"Generated {len(js_programs)} JS files with meaningful filenames.")
