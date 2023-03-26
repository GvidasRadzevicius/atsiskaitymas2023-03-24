import sqlite3

def create_database():
    
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY, 
                    name TEXT NOT NULL, 
                    email TEXT NOT NULL UNIQUE, 
                    password TEXT NOT NULL)''')
        c.execute('''CREATE TABLE IF NOT EXISTS groups
                    (id INTEGER PRIMARY KEY, 
                    name TEXT NOT NULL)''')
        c.execute('''CREATE TABLE IF NOT EXISTS bills
                    (id INTEGER PRIMARY KEY, 
                    description TEXT NOT NULL, 
                    amount REAL NOT NULL, 
                    group_id INTEGER NOT NULL, 
                    payer_id INTEGER NOT NULL, 
                    FOREIGN KEY(group_id) REFERENCES groups(id), 
                    FOREIGN KEY(payer_id) REFERENCES users(id))''')
        conn.commit()
        conn.close()
        print("Database created successfully")
    except sqlite3.Error as e:
        print("Error creating database:", e)

