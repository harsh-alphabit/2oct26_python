import subprocess
from pathlib import Path
import PyPDF2

MODULE_DIR = Path(r"c:\Users\chvha\Desktop\alphabit batchs\2-10-26 python core\python-fund\module- 5")
HTML_FILE = MODULE_DIR / "practice_tasks.html"
PDF_FILE = MODULE_DIR / "practice_tasks.pdf"

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Python Exception Handling — 25 Practice Tasks</title>
<style>
  @page {
    size: A4 portrait;
    margin: 12mm 14mm 14mm 14mm;
  }

  *, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: #1e293b;
    background-color: #ffffff;
    line-height: 1.45;
    font-size: 12.5px;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }

  /* Header Banner */
  .header-card {
    background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #312e81 100%);
    color: #ffffff;
    border-radius: 9px;
    padding: 16px 22px;
    margin-bottom: 12px;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.12);
  }

  .header-badge {
    display: inline-block;
    background: rgba(255, 255, 255, 0.18);
    backdrop-filter: blur(4px);
    border: 1px solid rgba(255, 255, 255, 0.25);
    color: #e2e8f0;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    padding: 3px 9px;
    border-radius: 20px;
    margin-bottom: 6px;
  }

  .header-title {
    font-size: 22px;
    font-weight: 800;
    letter-spacing: -0.4px;
    margin-bottom: 4px;
    color: #ffffff;
  }

  .header-subtitle {
    font-size: 12.5px;
    color: #cbd5e1;
    margin-bottom: 10px;
  }

  .header-meta-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    border-top: 1px solid rgba(255, 255, 255, 0.18);
    padding-top: 9px;
  }

  .meta-item {
    font-size: 11px;
  }

  .meta-label {
    color: #94a3b8;
    font-weight: 500;
    display: block;
    font-size: 9.5px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }

  .meta-val {
    color: #f8fafc;
    font-weight: 700;
    margin-top: 1px;
  }

  /* Difficulty Legend */
  .legend-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 7px;
    padding: 7px 14px;
    margin-bottom: 12px;
    font-size: 11px;
  }

  .legend-title {
    font-weight: 700;
    color: #475569;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-size: 10.5px;
  }

  .legend-items {
    display: flex;
    gap: 12px;
  }

  /* Difficulty Badges */
  .badge {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-size: 10.5px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 12px;
    line-height: 1;
    white-space: nowrap;
  }

  .badge-easy {
    background: #ecfdf5;
    color: #047857;
    border: 1px solid #a7f3d0;
  }

  .badge-medium {
    background: #fffbeb;
    color: #b45309;
    border: 1px solid #fde68a;
  }

  .badge-hard {
    background: #f5f3ff;
    color: #6d28d9;
    border: 1px solid #ddd6fe;
  }

  /* Topics Overview Grid */
  .topics-card {
    background: #f1f5f9;
    border: 1px solid #e2e8f0;
    border-radius: 7px;
    padding: 9px 14px;
    margin-bottom: 14px;
    break-inside: avoid;
    page-break-inside: avoid;
  }

  .topics-title {
    font-size: 10.5px;
    font-weight: 800;
    color: #334155;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 6px;
  }

  .topics-list {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 3px 14px;
    list-style: none;
    font-size: 11px;
    color: #475569;
  }

  .topics-list li {
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .topic-num {
    display: inline-block;
    width: 16px;
    height: 16px;
    background: #3b82f6;
    color: #ffffff;
    font-size: 9.5px;
    font-weight: 700;
    border-radius: 50%;
    text-align: center;
    line-height: 16px;
    flex-shrink: 0;
  }

  /* Section Header */
  .section-banner {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: #0f172a;
    color: #ffffff;
    padding: 7px 12px;
    border-radius: 6px;
    margin-top: 14px;
    margin-bottom: 9px;
    break-after: avoid;
    page-break-after: avoid;
  }

  .section-banner-title {
    font-size: 12.5px;
    font-weight: 800;
    letter-spacing: 0.3px;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .section-badge {
    background: #38bdf8;
    color: #0f172a;
    font-size: 9.5px;
    font-weight: 800;
    padding: 2px 7px;
    border-radius: 10px;
    letter-spacing: 0.4px;
  }

  .section-tasks-count {
    font-size: 10.5px;
    color: #94a3b8;
    font-weight: 600;
  }

  /* Task Card */
  .task-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-left: 4px solid #3b82f6;
    border-radius: 6px;
    padding: 10px 13px;
    margin-bottom: 9px;
    break-inside: avoid;
    page-break-inside: avoid;
    box-shadow: 0 1px 2px rgba(0,0,0,0.02);
  }

  .task-card.easy {
    border-left-color: #10b981;
  }

  .task-card.medium {
    border-left-color: #f59e0b;
  }

  .task-card.hard {
    border-left-color: #8b5cf6;
  }

  .task-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 6px;
    padding-bottom: 5px;
    border-bottom: 1px solid #f1f5f9;
  }

  .task-title-group {
    display: flex;
    align-items: center;
    gap: 7px;
  }

  .task-num {
    font-size: 11px;
    font-weight: 800;
    color: #0f172a;
    background: #f1f5f9;
    padding: 2px 6px;
    border-radius: 4px;
    border: 1px solid #e2e8f0;
  }

  .task-title {
    font-size: 12px;
    font-weight: 700;
    color: #0f172a;
  }

  .task-desc {
    color: #334155;
    font-size: 11.5px;
    line-height: 1.5;
  }

  .task-desc ul, .task-desc ol {
    margin-left: 16px;
    margin-top: 3px;
    margin-bottom: 4px;
  }

  .task-desc li {
    margin-bottom: 2px;
  }

  /* Code box */
  .code-block {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 6px 9px;
    font-family: "Cascadia Code", Consolas, "Courier New", monospace;
    font-size: 10.5px;
    color: #0f172a;
    white-space: pre-wrap;
    word-break: break-word;
    margin: 5px 0;
    line-height: 1.4;
  }

  .code-inline {
    background: #f1f5f9;
    border: 1px solid #e2e8f0;
    border-radius: 3px;
    padding: 1px 4px;
    font-family: "Cascadia Code", Consolas, "Courier New", monospace;
    font-size: 10.5px;
    color: #0f172a;
    font-weight: 600;
  }

  /* Callout bars */
  .info-bar {
    display: flex;
    align-items: flex-start;
    gap: 6px;
    font-size: 11px;
    padding: 5px 9px;
    border-radius: 5px;
    margin-top: 5px;
    line-height: 1.4;
  }

  .test-bar {
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
    color: #166534;
  }

  .test-bar strong {
    color: #14532d;
    font-weight: 700;
  }

  .hint-bar {
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    color: #1e40af;
  }

  .hint-bar strong {
    color: #1e3a8a;
    font-weight: 700;
  }

  .expected-bar {
    background: #faf5ff;
    border: 1px solid #e9d5ff;
    color: #581c87;
  }

  .expected-bar strong {
    color: #4c1d95;
    font-weight: 700;
  }

  .footer-note {
    text-align: center;
    font-size: 10px;
    color: #94a3b8;
    margin-top: 18px;
    padding-top: 8px;
    border-top: 1px solid #e2e8f0;
    break-inside: avoid;
    page-break-inside: avoid;
  }
</style>
</head>
<body>

  <!-- Header -->
  <div class="header-card">
    <div class="header-badge">Python Core &bull; Module 5</div>
    <h1 class="header-title">Exception Handling (try / except)</h1>
    <div class="header-subtitle">Comprehensive Practice Tasks &bull; 25 Hands-on Lab Exercises</div>
    
    <div class="header-meta-grid">
      <div class="meta-item">
        <span class="meta-label">Total Exercises</span>
        <div class="meta-val">25 Tasks Across 8 Sections</div>
      </div>
      <div class="meta-item">
        <span class="meta-label">Core Concepts</span>
        <div class="meta-val">try, except, else, finally, raise</div>
      </div>
      <div class="meta-item">
        <span class="meta-label">Real-World Labs</span>
        <div class="meta-val">ATM, Quiz, Cart, Marksheet</div>
      </div>
    </div>
  </div>

  <!-- Difficulty Legend -->
  <div class="legend-bar">
    <span class="legend-title">Difficulty Levels:</span>
    <div class="legend-items">
      <span class="badge badge-easy">⭐ Easy — Fundamentals</span>
      <span class="badge badge-medium">⭐⭐ Medium — Applied Logic</span>
      <span class="badge badge-hard">⭐⭐⭐ Hard — Complex & Real World</span>
    </div>
  </div>

  <!-- Topics Covered -->
  <div class="topics-card">
    <div class="topics-title">Topics Covered in this Practice Set</div>
    <ul class="topics-list">
      <li><span class="topic-num">1</span> Basic try / except syntax</li>
      <li><span class="topic-num">2</span> Catching specific exceptions (ValueError, ZeroDivisionError, etc.)</li>
      <li><span class="topic-num">3</span> Inspecting errors with <span class="code-inline">as e</span></li>
      <li><span class="topic-num">4</span> Multi-except hierarchies & general fallback</li>
      <li><span class="topic-num">5</span> The <span class="code-inline">else</span> clause for clean success execution</li>
      <li><span class="topic-num">6</span> The <span class="code-inline">finally</span> block for guaranteed cleanup</li>
      <li><span class="topic-num">7</span> Complete 4-part architecture (try / except / else / finally)</li>
      <li><span class="topic-num">8</span> Nested exception handling & loop validation workflows</li>
    </ul>
  </div>

  <!-- SECTION 1 -->
  <div class="section-banner">
    <div class="section-banner-title">
      <span class="section-badge">Section 1</span>
      <span>Basic try / except</span>
    </div>
    <span class="section-tasks-count">Tasks 1 – 3</span>
  </div>

  <!-- Task 1 -->
  <div class="task-card easy">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 01</span>
        <span class="task-title">Basic Integer Input Conversion</span>
      </div>
      <span class="badge badge-easy">⭐ Easy</span>
    </div>
    <div class="task-desc">
      Ask the user to enter a number and convert it to an integer using <span class="code-inline">int()</span>.<br>
      If the user inputs something non-numeric (e.g. <span class="code-inline">"hello"</span>), catch the error and print:
      <br><span class="code-inline">"Invalid input! Please enter a number."</span>
    </div>
    <div class="info-bar test-bar">
      <span>🧪 <strong>Test with:</strong> <span class="code-inline">"hello"</span>, <span class="code-inline">"abc"</span>, <span class="code-inline">"10"</span></span>
    </div>
  </div>

  <!-- Task 2 -->
  <div class="task-card easy">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 02</span>
        <span class="task-title">ZeroDivisionError Handling</span>
      </div>
      <span class="badge badge-easy">⭐ Easy</span>
    </div>
    <div class="task-desc">
      Ask the user for two numbers. Divide the first by the second.<br>
      If the second number is <span class="code-inline">0</span>, catch the <span class="code-inline">ZeroDivisionError</span> and print:
      <br><span class="code-inline">"Cannot divide by zero!"</span>
    </div>
    <div class="info-bar test-bar">
      <span>🧪 <strong>Test with:</strong> <span class="code-inline">10, 0</span> and <span class="code-inline">10, 2</span></span>
    </div>
  </div>

  <!-- Task 3 -->
  <div class="task-card easy">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 03</span>
        <span class="task-title">Safe List Index Access (IndexError)</span>
      </div>
      <span class="badge badge-easy">⭐ Easy</span>
    </div>
    <div class="task-desc">
      Create a list: <span class="code-inline">fruits = ["apple", "banana", "cherry"]</span>.<br>
      Ask the user to enter an index number and try to print <span class="code-inline">fruits[index]</span>.<br>
      If the index is out of range, catch <span class="code-inline">IndexError</span> and print:
      <br><span class="code-inline">"That index doesn't exist!"</span>
    </div>
    <div class="info-bar test-bar">
      <span>🧪 <strong>Test with:</strong> <span class="code-inline">0</span>, <span class="code-inline">5</span>, <span class="code-inline">-10</span></span>
    </div>
  </div>

  <!-- SECTION 2 -->
  <div class="section-banner">
    <div class="section-banner-title">
      <span class="section-badge">Section 2</span>
      <span>Specific Exceptions & "as e"</span>
    </div>
    <span class="section-tasks-count">Tasks 4 – 7</span>
  </div>

  <!-- Task 4 -->
  <div class="task-card easy">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 04</span>
        <span class="task-title">Dictionary Key Lookup (KeyError)</span>
      </div>
      <span class="badge badge-easy">⭐ Easy</span>
    </div>
    <div class="task-desc">
      Create a dictionary: <span class="code-inline">student = {"name": "Ravi", "age": 20}</span>.<br>
      Ask the user to enter a key name (like <span class="code-inline">"name"</span>, <span class="code-inline">"age"</span>, <span class="code-inline">"marks"</span>) and try to print the value.<br>
      If the key doesn't exist, catch <span class="code-inline">KeyError</span> and print:
      <br><span class="code-inline">"Key not found!"</span>
    </div>
    <div class="info-bar test-bar">
      <span>🧪 <strong>Test with:</strong> <span class="code-inline">"name"</span>, <span class="code-inline">"marks"</span></span>
    </div>
  </div>

  <!-- Task 5 -->
  <div class="task-card easy">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 05</span>
        <span class="task-title">Incompatible Types (TypeError)</span>
      </div>
      <span class="badge badge-easy">⭐ Easy</span>
    </div>
    <div class="task-desc">
      Ask the user for their name.<br>
      Try to do: <span class="code-inline">result = name + 10</span><br>
      Catch the <span class="code-inline">TypeError</span> and print:
      <br><span class="code-inline">"Cannot add text and number together!"</span>
    </div>
  </div>

  <!-- Task 6 -->
  <div class="task-card medium">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 06</span>
        <span class="task-title">Capturing Error Message Details with "as e"</span>
      </div>
      <span class="badge badge-medium">⭐⭐ Medium</span>
    </div>
    <div class="task-desc">
      Ask the user to enter a number and try to convert it to <span class="code-inline">int</span>.<br>
      If it fails, catch <span class="code-inline">ValueError as e</span> and print:
      <br><span class="code-inline">print(f"Error details: {e}")</span>
    </div>
    <div class="info-bar test-bar">
      <span>🧪 <strong>Test with:</strong> <span class="code-inline">"abc"</span> &rarr; should show the actual Python error message</span>
    </div>
  </div>

  <!-- Task 7 -->
  <div class="task-card medium">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 07</span>
        <span class="task-title">"as e" with IndexError</span>
      </div>
      <span class="badge badge-medium">⭐⭐ Medium</span>
    </div>
    <div class="task-desc">
      Create a list of 3 city names. Ask user for an index.<br>
      If <span class="code-inline">IndexError</span> occurs, print the actual error message using <span class="code-inline">as e</span>.<br>
      <strong>Format:</strong> <span class="code-inline">"Oops! {e}"</span>
    </div>
  </div>

  <!-- SECTION 3 -->
  <div class="section-banner">
    <div class="section-banner-title">
      <span class="section-badge">Section 3</span>
      <span>Multiple except Blocks</span>
    </div>
    <span class="section-tasks-count">Tasks 8 – 10</span>
  </div>

  <!-- Task 8 -->
  <div class="task-card medium">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 08</span>
        <span class="task-title">Two except Blocks</span>
      </div>
      <span class="badge badge-medium">⭐⭐ Medium</span>
    </div>
    <div class="task-desc">
      Ask the user for a number, convert to int. Then divide 100 by that number.<br>
      Handle BOTH:
      <ul>
        <li><span class="code-inline">ValueError</span> (if they type text)</li>
        <li><span class="code-inline">ZeroDivisionError</span> (if they type 0)</li>
      </ul>
      Print a different message for each.
    </div>
    <div class="info-bar test-bar">
      <span>🧪 <strong>Test with:</strong> <span class="code-inline">"abc"</span>, <span class="code-inline">0</span>, <span class="code-inline">5</span></span>
    </div>
  </div>

  <!-- Task 9 -->
  <div class="task-card medium">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 09</span>
        <span class="task-title">Three except Blocks with General Fallback</span>
      </div>
      <span class="badge badge-medium">⭐⭐ Medium</span>
    </div>
    <div class="task-desc">
      Create a list: <span class="code-inline">prices = ["100", "abc", "200"]</span>. Ask user for an index.<br>
      Try to:
      <ol>
        <li>Access <span class="code-inline">prices[index]</span></li>
        <li>Convert it to <span class="code-inline">int</span></li>
        <li>Print the value</li>
      </ol>
      Handle: <span class="code-inline">IndexError</span>, <span class="code-inline">ValueError</span>, and a general <span class="code-inline">Exception</span>.
    </div>
    <div class="info-bar test-bar">
      <span>🧪 <strong>Test with:</strong> <span class="code-inline">0</span>, <span class="code-inline">1</span>, <span class="code-inline">5</span></span>
    </div>
  </div>

  <!-- Task 10 -->
  <div class="task-card medium">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 10</span>
        <span class="task-title">Multiple Exceptions in a Calculator</span>
      </div>
      <span class="badge badge-medium">⭐⭐ Medium</span>
    </div>
    <div class="task-desc">
      Ask user for: <span class="code-inline">number1</span>, <span class="code-inline">operator</span> (+, -, *, /), <span class="code-inline">number2</span>.<br>
      Perform the calculation.<br>
      Handle:
      <ul>
        <li><span class="code-inline">ValueError</span> (non-numeric input)</li>
        <li><span class="code-inline">ZeroDivisionError</span> (dividing by 0)</li>
        <li><span class="code-inline">Exception</span> (anything else, like invalid operator)</li>
      </ul>
    </div>
    <div class="info-bar test-bar">
      <span>🧪 <strong>Test with:</strong> <span class="code-inline">10 / 0</span>, <span class="code-inline">"abc" + 5</span>, <span class="code-inline">10 / 2</span></span>
    </div>
  </div>

  <!-- SECTION 4 -->
  <div class="section-banner">
    <div class="section-banner-title">
      <span class="section-badge">Section 4</span>
      <span>The else Block</span>
    </div>
    <span class="section-tasks-count">Tasks 11 – 13</span>
  </div>

  <!-- Task 11 -->
  <div class="task-card medium">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 11</span>
        <span class="task-title">try / except / else Flow</span>
      </div>
      <span class="badge badge-medium">⭐⭐ Medium</span>
    </div>
    <div class="task-desc">
      Ask the user for their age (convert to int).
      <ul>
        <li>If conversion succeeds (no error): in the <span class="code-inline">else</span> block, print <span class="code-inline">"You are {age} years old!"</span></li>
        <li>If conversion fails: print <span class="code-inline">"That's not a valid age!"</span></li>
      </ul>
    </div>
    <div class="info-bar test-bar">
      <span>🧪 <strong>Test with:</strong> <span class="code-inline">25</span>, <span class="code-inline">"twenty"</span></span>
    </div>
  </div>

  <!-- Task 12 -->
  <div class="task-card medium">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 12</span>
        <span class="task-title">else with Division</span>
      </div>
      <span class="badge badge-medium">⭐⭐ Medium</span>
    </div>
    <div class="task-desc">
      Ask for two numbers.
      <ul>
        <li>In <span class="code-inline">try</span>: convert both to int and divide.</li>
        <li>In <span class="code-inline">except</span>: handle <span class="code-inline">ValueError</span> and <span class="code-inline">ZeroDivisionError</span>.</li>
        <li>In <span class="code-inline">else</span>: print <span class="code-inline">"Division successful! Result = {result}"</span></li>
      </ul>
      <em>(The else block should ONLY run when there is NO error.)</em>
    </div>
  </div>

  <!-- Task 13 -->
  <div class="task-card medium">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 13</span>
        <span class="task-title">else with List Access</span>
      </div>
      <span class="badge badge-medium">⭐⭐ Medium</span>
    </div>
    <div class="task-desc">
      Create a list: <span class="code-inline">colors = ["red", "green", "blue"]</span>. Ask user for an index.
      <ul>
        <li>In <span class="code-inline">try</span>: access <span class="code-inline">colors[index]</span>.</li>
        <li>In <span class="code-inline">except</span>: handle <span class="code-inline">IndexError</span>.</li>
        <li>In <span class="code-inline">else</span>: print <span class="code-inline">"You picked: {color}"</span> and also print <span class="code-inline">"This color has {len} letters"</span>.</li>
      </ul>
    </div>
    <div class="info-bar hint-bar">
      <span>💡 <strong>Best Practice:</strong> Extra processing in <span class="code-inline">else</span> keeps your <span class="code-inline">try</span> block compact and focused.</span>
    </div>
  </div>

  <!-- SECTION 5 -->
  <div class="section-banner">
    <div class="section-banner-title">
      <span class="section-badge">Section 5</span>
      <span>The finally Block</span>
    </div>
    <span class="section-tasks-count">Tasks 14 – 16</span>
  </div>

  <!-- Task 14 -->
  <div class="task-card medium">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 14</span>
        <span class="task-title">try / except / finally Execution</span>
      </div>
      <span class="badge badge-medium">⭐⭐ Medium</span>
    </div>
    <div class="task-desc">
      Ask the user for a number. Try to divide 100 by that number.<br>
      In <span class="code-inline">except</span>: handle <span class="code-inline">ZeroDivisionError</span> and <span class="code-inline">ValueError</span>.<br>
      In <span class="code-inline">finally</span>: print <span class="code-inline">"Calculation attempt finished."</span><br>
      <em>The finally message should appear whether there was an error or NOT.</em>
    </div>
    <div class="info-bar test-bar">
      <span>🧪 <strong>Test with:</strong> <span class="code-inline">0</span>, <span class="code-inline">5</span>, <span class="code-inline">"abc"</span></span>
    </div>
  </div>

  <!-- Task 15 -->
  <div class="task-card medium">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 15</span>
        <span class="task-title">finally as Cleanup Guarantee</span>
      </div>
      <span class="badge badge-medium">⭐⭐ Medium</span>
    </div>
    <div class="task-desc">
      Simulate opening a connection: <span class="code-inline">print("Opening database connection...")</span>.<br>
      In <span class="code-inline">try</span>: ask user for a number and divide 50 by it.<br>
      In <span class="code-inline">except</span>: handle errors.<br>
      In <span class="code-inline">finally</span>: print <span class="code-inline">"Closing database connection..."</span>.<br>
      <em>The connection must ALWAYS close &mdash; even if there's an error!</em>
    </div>
  </div>

  <!-- Task 16 -->
  <div class="task-card hard">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 16</span>
        <span class="task-title">Complete Pipeline: try / except / else / finally</span>
      </div>
      <span class="badge badge-hard">⭐⭐⭐ Hard</span>
    </div>
    <div class="task-desc">
      Ask the user for a password:
      <ul>
        <li>In <span class="code-inline">try</span>: check if <span class="code-inline">len(password) &gt;= 8</span> &mdash; if not, raise:
          <br><span class="code-inline">raise ValueError("Password must be at least 8 characters")</span></li>
        <li>In <span class="code-inline">except</span>: catch <span class="code-inline">ValueError as e</span>, print the error.</li>
        <li>In <span class="code-inline">else</span>: print <span class="code-inline">"Password accepted!"</span></li>
        <li>In <span class="code-inline">finally</span>: print <span class="code-inline">"Password check complete."</span></li>
      </ul>
    </div>
    <div class="info-bar test-bar">
      <span>🧪 <strong>Test with:</strong> <span class="code-inline">"abc"</span>, <span class="code-inline">"mypassword123"</span></span>
    </div>
  </div>

  <!-- SECTION 6 -->
  <div class="section-banner">
    <div class="section-banner-title">
      <span class="section-badge">Section 6</span>
      <span>Nested try / except</span>
    </div>
    <span class="section-tasks-count">Tasks 17 – 18</span>
  </div>

  <!-- Task 17 -->
  <div class="task-card hard">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 17</span>
        <span class="task-title">Nested: Processing a List of Heterogeneous Items</span>
      </div>
      <span class="badge badge-hard">⭐⭐⭐ Hard</span>
    </div>
    <div class="task-desc">
      Given this data:
      <div class="code-block">numbers = ["10", "abc", "20", "0", "30"]</div>
      Loop through each item:
      <ul>
        <li><strong>Inner try:</strong> convert to int, then divide 100 by it.</li>
        <li><strong>Inner except:</strong> handle <span class="code-inline">ValueError</span> and <span class="code-inline">ZeroDivisionError</span> separately.</li>
        <li><strong>Outer try:</strong> wraps the whole loop as a safety net.</li>
        <li>Print <span class="code-inline">✅</span> for success and <span class="code-inline">❌</span> for each error.</li>
      </ul>
    </div>
    <div class="info-bar expected-bar">
      <span>📋 <strong>Expected Output:</strong><br>
      ✅ 100/10 = 10.0<br>
      ❌ 'abc' is not a valid number<br>
      ✅ 100/20 = 5.0<br>
      ❌ Cannot divide by zero<br>
      ✅ 100/30 = 3.33</span>
    </div>
  </div>

  <!-- Task 18 -->
  <div class="task-card hard">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 18</span>
        <span class="task-title">Nested: Student Grades Calculation</span>
      </div>
      <span class="badge badge-hard">⭐⭐⭐ Hard</span>
    </div>
    <div class="task-desc">
      Given:
      <div class="code-block">students = [
    {"name": "Aman", "score": "85", "total": "100"},
    {"name": "Neha", "score": "xyz", "total": "100"},
    {"name": "Kiran", "score": "70", "total": "0"},
]</div>
      <ul>
        <li><strong>Outer try:</strong> process all students.</li>
        <li><strong>Inner try:</strong> convert <span class="code-inline">score</span> and <span class="code-inline">total</span> to int, calculate percentage.</li>
        <li><strong>Inner except:</strong> handle <span class="code-inline">ValueError</span> (bad score) and <span class="code-inline">ZeroDivisionError</span> (total=0).</li>
        <li>Print each student's result or error message clearly.</li>
      </ul>
    </div>
  </div>

  <!-- SECTION 7 -->
  <div class="section-banner">
    <div class="section-banner-title">
      <span class="section-badge">Section 7</span>
      <span>Loops + try/except (Input Validation)</span>
    </div>
    <span class="section-tasks-count">Tasks 19 – 21</span>
  </div>

  <!-- Task 19 -->
  <div class="task-card medium">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 19</span>
        <span class="task-title">Keep Asking Until Valid</span>
      </div>
      <span class="badge badge-medium">⭐⭐ Medium</span>
    </div>
    <div class="task-desc">
      Use a <span class="code-inline">while</span> loop to keep asking the user for a number.<br>
      If they enter something invalid, print an error and ask again.<br>
      Only break out of the loop when they enter a valid integer.<br>
      After the loop, print: <span class="code-inline">"You entered: {number}"</span>
    </div>
  </div>

  <!-- Task 20 -->
  <div class="task-card medium">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 20</span>
        <span class="task-title">Validate Age with Range Check</span>
      </div>
      <span class="badge badge-medium">⭐⭐ Medium</span>
    </div>
    <div class="task-desc">
      Keep asking for age until the user enters a valid integer that is ALSO between <span class="code-inline">1</span> and <span class="code-inline">120</span>.<br>
      Handle <span class="code-inline">ValueError</span> for non-numeric input.<br>
      Use <span class="code-inline">else</span> block to check the range &mdash; if out of range, continue the loop.<br>
      If valid, break and print: <span class="code-inline">"Your age: {age}"</span>
    </div>
  </div>

  <!-- Task 21 -->
  <div class="task-card hard">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 21</span>
        <span class="task-title">Collect 5 Valid Numbers</span>
      </div>
      <span class="badge badge-hard">⭐⭐⭐ Hard</span>
    </div>
    <div class="task-desc">
      Ask the user to enter 5 numbers one by one.<br>
      If they enter something invalid, show an error and DON'T count it.<br>
      Keep asking until you have exactly 5 valid numbers.<br>
      At the end, print all 5 numbers and their sum.
    </div>
    <div class="info-bar hint-bar">
      <span>💡 <strong>Hint:</strong> Use a list to store valid numbers, loop while <span class="code-inline">len(list) &lt; 5</span>.</span>
    </div>
  </div>

  <!-- SECTION 8 -->
  <div class="section-banner">
    <div class="section-banner-title">
      <span class="section-badge">Section 8</span>
      <span>Real-World Scenarios</span>
    </div>
    <span class="section-tasks-count">Tasks 22 – 25</span>
  </div>

  <!-- Task 22 -->
  <div class="task-card hard">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 22</span>
        <span class="task-title">ATM Withdrawal Simulator</span>
      </div>
      <span class="badge badge-hard">⭐⭐⭐ Hard</span>
    </div>
    <div class="task-desc">
      Starting balance = <span class="code-inline">10000</span>.<br>
      In a loop:
      <ul>
        <li>Ask user how much to withdraw (0 to exit).</li>
        <li>Handle <span class="code-inline">ValueError</span> if they type text.</li>
        <li>If <span class="code-inline">amount &gt; balance</span>: print <span class="code-inline">"Insufficient funds!"</span></li>
        <li>If <span class="code-inline">amount &lt;= 0</span> (but not exit): print <span class="code-inline">"Enter a positive amount!"</span></li>
        <li>If valid: subtract from balance, print remaining balance.</li>
      </ul>
      Use <span class="code-inline">finally</span> inside the loop to always print <span class="code-inline">"--- Transaction complete ---"</span>.
    </div>
  </div>

  <!-- Task 23 -->
  <div class="task-card hard">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 23</span>
        <span class="task-title">Shopping Cart Checkout System</span>
      </div>
      <span class="badge badge-hard">⭐⭐⭐ Hard</span>
    </div>
    <div class="task-desc">
      Given a product catalog:
      <div class="code-block">catalog = {"pen": 10, "notebook": 50, "bag": 500, "bottle": 150}</div>
      In a loop:
      <ul>
        <li>Ask the user for a product name and quantity.</li>
        <li>Handle <span class="code-inline">KeyError</span> if the product doesn't exist.</li>
        <li>Handle <span class="code-inline">ValueError</span> if quantity is not a number.</li>
        <li>If valid, add to a cart list and running total.</li>
        <li>Type <span class="code-inline">"done"</span> to finish.</li>
      </ul>
      At the end, print the receipt (all items + total).<br>
      Use <span class="code-inline">else</span> block to add item only when no error occurred.
    </div>
  </div>

  <!-- Task 24 -->
  <div class="task-card hard">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 24</span>
        <span class="task-title">Mark Sheet Processor with Custom Range Validation</span>
      </div>
      <span class="badge badge-hard">⭐⭐⭐ Hard</span>
    </div>
    <div class="task-desc">
      Given:
      <div class="code-block">raw_marks = [
    ("Ravi", "85"), ("Priya", "abc"), ("Amit", "92"),
    ("Sneha", "-10"), ("Kiran", "78"), ("Neha", "110"),
]</div>
      Process each student:
      <ul>
        <li>Convert marks to int (handle <span class="code-inline">ValueError</span>).</li>
        <li>Check if marks are between 0 and 100 &mdash; if not, raise:
          <br><span class="code-inline">raise ValueError("Marks out of range")</span></li>
        <li>Determine grade: <span class="code-inline">&gt;=90 A</span>, <span class="code-inline">&gt;=75 B</span>, <span class="code-inline">&gt;=60 C</span>, else <span class="code-inline">D</span></li>
      </ul>
      Use nested <span class="code-inline">try/except</span>. Print <span class="code-inline">✅</span> for valid entries, <span class="code-inline">❌</span> for errors.<br>
      At the end, print how many passed and how many had errors.
    </div>
  </div>

  <!-- Task 25 -->
  <div class="task-card hard">
    <div class="task-header">
      <div class="task-title-group">
        <span class="task-num">Task 25</span>
        <span class="task-title">Mini Quiz Game with Exception Handling</span>
      </div>
      <span class="badge badge-hard">⭐⭐⭐ Hard</span>
    </div>
    <div class="task-desc">
      Create a quiz with 5 questions (stored as a list of tuples):
      <div class="code-block">questions = [
    ("What is 5 + 3?", 8),
    ("What is 10 / 2?", 5),
    ("What is 7 * 6?", 42),
    ("What is 100 - 37?", 63),
    ("What is 2 ** 5?", 32),
]</div>
      For each question:
      <ul>
        <li>Ask the user for their answer.</li>
        <li>In <span class="code-inline">try</span>: convert answer to int.</li>
        <li>In <span class="code-inline">except</span>: print <span class="code-inline">"Invalid answer! Skipping..."</span> and move to next.</li>
        <li>In <span class="code-inline">else</span>: check if answer matches &rarr; update score.</li>
        <li>In <span class="code-inline">finally</span>: print <span class="code-inline">"Question {n} done."</span></li>
      </ul>
      At the end, print <span class="code-inline">"You scored {score}/5"</span>.<br>
      Wrap everything in an outer <span class="code-inline">try/except</span> for safety.
    </div>
  </div>

  <div class="footer-note">
    Python Core Curriculum &bull; Module 5: Exception Handling &bull; Practice Tasks Worksheet
  </div>

</body>
</html>
"""

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(html_content)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    chrome_path,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--no-pdf-header-footer",
    f"--print-to-pdf={PDF_FILE}",
    str(HTML_FILE.resolve())
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome stderr:", res.stderr.strip())

reader = PyPDF2.PdfReader(str(PDF_FILE))
print(f"Generated {PDF_FILE.name}: {len(reader.pages)} pages, {PDF_FILE.stat().st_size} bytes")
