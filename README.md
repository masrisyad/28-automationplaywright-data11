# 🧪 Dropdown Interaction Automation (Playwright Python)

A lightweight UI automation script built with **Python** and **Playwright**. This project demonstrates how to programmatically interact with standard HTML dropdown menus (`<select>` elements) using different selection strategies.

---

## 📌 Overview

This script serves as a Proof of Concept (PoC) for dropdown manipulation. It targets the widely used practice site, [The Internet (Herokuapp)](https://the-internet.herokuapp.com/dropdown).

**Key Interactions Demonstrated:**

| Selection Method | Playwright Syntax | Best Use Case |
| --- | --- | --- |
| **By Value** | `page.select_option(selector, "value")` | When the underlying HTML `value` attribute is stable and unique. |
| **By Label** | `page.select_option(selector, label="Text")` | When you want to mimic a real user by targeting the visible text rendered on the screen. |

---

## 🛠️ Prerequisites

Before executing this script, ensure your system meets the following baseline requirements:

* **Python:** Version 3.8 or higher.
* **pip:** Python's package installer.

---

## ⚙️ Installation & Setup

Follow these steps to configure your local execution environment properly:

**1. Clone or Create the Script**
Save the provided Python code into a file named `main.py` in your project directory.

**2. Establish a Virtual Environment (Highly Recommended)**
Using a virtual environment isolates your project dependencies from the global system.

```bash
# Create the virtual environment
python -m venv venv

# Activate on macOS/Linux:
source venv/bin/activate

# Activate on Windows (Command Prompt):
venv\Scripts\activate

```

**3. Install Playwright**
Install the Playwright Python library via pip:

```bash
pip install playwright

```

**4. Install Browser Binaries**
Playwright requires its own specific browser engines to interact with web pages. Install the Chromium binary by running:

```bash
playwright install chromium

```

---

## 🚀 Execution Guide

Run the script directly from your terminal:

```bash
python main.py

```

### What to Expect:

Because the script uses `headless=False`, you will visually see a Chromium browser launch. It will navigate to the target URL, swiftly select **"Option 1"**, immediately change the selection to **"Option 2"**, and then close.

Check your terminal for the successful execution log:

```text
Dropdown berhasil dimanipulasi.

```

---

## 🏗️ Best Practice

While this script beautifully demonstrates action-based automation, scaling it into a robust test suite requires adding verification steps. Here is how a Senior QE would improve this code for a production environment:

1. **Implement Assertions:** Automation should verify state, not just perform actions. After making a selection, use Playwright's `expect` module to assert that the value actually changed in the DOM.
```python
from playwright.sync_api import expect

# After selecting Option 1:
expect(page.locator("select#dropdown")).to_have_value("1")

```


2. **Handle Dynamic Waits:** If the dropdown relies on an API call to populate its options, you should implement a wait strategy (e.g., waiting for the `<option>` elements to be visible) before attempting to select them to prevent flakiness.
3. **Headless Execution:** For CI/CD environments (e.g., GitHub Actions, GitLab CI), change the browser launch argument to `headless=True` to run the test silently without a graphical interface, which saves system resources and time.
