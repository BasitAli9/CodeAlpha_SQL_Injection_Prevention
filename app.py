from flask import Flask, render_template, request
import sqlite3
import re

app = Flask(__name__)

# Database Initialization with dummy data
def init_db():
    conn = sqlite3.connect('security_demo.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS users')
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    ''')
    # Dummy production credentials insert kar rahe hain
    cursor.execute("INSERT INTO users (username, password) VALUES ('Basit', '123')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('basitali', '2026')")
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    mode = request.form['mode']
    
    executed_query = ""
    status = ""
    result = ""

    conn = sqlite3.connect('security_demo.db')
    cursor = conn.cursor()

    if mode == 'unsafe':
        # ❌ VULNERABLE: Direct string concatenation allows SQL Injection
        executed_query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        try:
            cursor.execute(executed_query)
            user = cursor.fetchone()
            if user:
                status = "🔓 Authentication Bypassed! (SQL Injection Success)"
                result = f"Logged in user record: ID={user[0]}, Username='{user[1]}'"
            else:
                status = "❌ Login Failed"
                result = "No matching credentials found."
        except Exception as e:
            status = "💥 Database Error Triggered"
            result = str(e)
            
    else:
        #  SECURE: Parameterized queries or Input validation
        executed_query = "SELECT * FROM users WHERE username = ? AND password = ?"
        
        # Validation Check to explicitly block raw classic SQL statements
        if re.search(r"('|\b(OR|AND|UNION|SELECT|DROP)\b)", username, re.IGNORECASE):
            status = "🛡️ Malicious Input Blocked by FireWall Rule!"
            result = "The system intercepted dangerous characters before compiling sql structure."
        else:
            cursor.execute(executed_query, (username, password))
            user = cursor.fetchone()
            if user:
                status = "✅ Secure Authentication Successful"
                result = f"Logged in user: {user[1]}"
            else:
                status = "❌ Secure Login Failed"
                result = "Invalid production credentials."

    conn.close()
    return render_template('index.html', mode=mode, status=status, result=result, executed_query=executed_query)

if __name__ == '__main__':
    init_db()
    import os
    # Render cloud friendly configuration allocation
    cloud_port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=cloud_port, debug=False)