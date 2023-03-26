from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        password2 = request.form['password2']

        if password != password2:
            return 'Passwords do not match'
        
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        try:
            c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        except sqlite3.IntegrityError:
            return 'This email is already in use'

        conn.commit()
        conn.close()

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = c.fetchone()

        conn.close()

        if user and user[3] == password:
            return redirect(url_for('groups'))
        else:
            return 'Invalid login'

    return render_template('login.html')

@app.route('/groups')
def groups():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT * FROM groups")
    groups = c.fetchall()

    conn.close()

    return render_template('groups.html', groups=groups)

@app.route('/bills/<int:group_id>')
def bills(group_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT * FROM bills WHERE group_id = ?", (group_id,))
    bills = c.fetchall()

    conn.close()

    return render_template('bills.html', bills=bills)

if __name__ == '__main__':
    app.run(debug=True)
