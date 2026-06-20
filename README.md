# SQL Injection Prevention Shield 🛡️

An interactive Cyber Security web application built with Python (Flask) and SQLite to demonstrate how SQL Injection attacks work and how to prevent them using Parameterized Queries.

---

## 🚀 Features
* **Dual Execution Modes:** 
  * **UNSAFE Mode:** Demonstrates how raw string concatenation allows attackers to bypass authentication.
  * **SECURE Mode:** Demonstrates how Parameterized Queries (Prepared Statements) completely block the attack.
* **Live Query Inspection:** Displays the exact SQL statement executed on the backend in real-time.
* **Modern UI/UX:** Clean, dark-themed responsive dashboard.

---

## 🛠️ Tech Stack
* **Backend:** Python 3.14, Flask
* **Database:** SQLite
* **Frontend:** HTML5, CSS3 (Tailwind-styled Custom CSS), JavaScript

---

## 💻 Local Setup Instructions

1. Clone the Repository:
   git clone <your-repository-url>
   cd CodeAlpha_SQL_Injection_Prevention

2. Set Up a Virtual Environment (Optional but Recommended):
   python -m venv .venv
   # Activate on Windows:
   .venv\Scripts\activate
   # Activate on macOS/Linux:
   source .venv/bin/activate

3. Install Dependencies:
   pip install flask

4. Run the Application:
   python app.py
   
   Open http://127.0.0.1:5000 or http://localhost:5000 in your web browser.

---

## 🧪 How to Test (Live Demonstration)

### 1. The Vulnerable Test (Unsafe Mode)
* Username / Payload: admin' OR '1'='1
* Password: Any random password (e.g., 123)
* Action: Click "Run Vulnerable Query"
* Result: Login Successful! The application is fooled because '1'='1' is always true, altering the query logic.

### 2. The Secure Test (Prevention Mode)
* Username / Payload: admin' OR '1'='1
* Password: Any random password (e.g., 123)
* Action: Click "Run Secure Query"
* Result: Login Failed. The backend uses parameterized inputs, treating the payload as a literal string value rather than executable SQL code.

---

## 🛡️ Prevention Logic

Instead of concatenating user inputs like this (Vulnerable):
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

The secure shield implements proper placeholders (Secure):
query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))
