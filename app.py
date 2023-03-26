import sqlite3
from sqlite3 import Error
from flask import Flask, request, flash, redirect, url_for, render_template, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

def create_database():
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL UNIQUE, password TEXT NOT NULL)''')
        c.execute('''CREATE TABLE IF NOT EXISTS groups (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, creator_id INTEGER NOT NULL, FOREIGN KEY (creator_id) REFERENCES users(id))''')
        c.execute('''CREATE TABLE IF NOT EXISTS bills (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, amount REAL NOT NULL, group_id INTEGER NOT NULL, FOREIGN KEY (group_id) REFERENCES groups(id))''')
        c.execute('''CREATE TABLE IF NOT EXISTS group_members (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER NOT NULL, group_id INTEGER NOT NULL, FOREIGN KEY (user_id) REFERENCES users(id), FOREIGN KEY (group_id) REFERENCES groups(id))''')
        conn.commit()
        print("Database created successfully")
        conn.close()
    except Error as e:
        print(e)

@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('show_login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if not name or not email or not password or not confirm_password:
            flash("All fields are required.")
            return redirect(url_for('show_register'))

        if password != confirm_password:
            flash("Passwords do not match.")
            return redirect(url_for('show_register'))

        try:
            conn = sqlite3.connect('database.db')
            c = conn.cursor()

            c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))

            conn.commit()
            flash("You have successfully registered!")
            return redirect(url_for('show_login'))

        except Error as e:
            flash("This email is already registered.")
            return redirect(url_for('show_register'))

    return render_template('register.html')

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
            session['user_id'] = user[0]
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid login.")
            return redirect(url_for('show_login'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('show_login'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user_id = session['user_id']

        conn = sqlite3.connect
        
        



app = Flask(__name__)

