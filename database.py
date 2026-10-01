import sqlite3

def connect():
    return sqlite3.connect("college.db")

def create_tables():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        is_admin INTEGER DEFAULT 0
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS chat_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_msg TEXT,
        bot_msg TEXT
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS courses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT,
        duration TEXT,
        fees TEXT
    )
    """)
    conn.commit()
    conn.close()
    preload_data()

def preload_data():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username='admin'")
    if not cur.fetchone():
        cur.execute("INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)", ("admin", "admin123", 1))
    cur.execute("SELECT * FROM courses")
    if not cur.fetchone():
        courses = [
            ("B.Sc Computer Science", "3 Years", "₹1,20,000"),
            ("B.A English", "3 Years", "₹90,000"),
            ("MCA", "2 Years", "₹1,50,000"),
            ("B.Com", "3 Years", "₹80,000")
        ]
        cur.executemany("INSERT INTO courses (course_name, duration, fees) VALUES (?, ?, ?)", courses)
    conn.commit()
    conn.close()

def log_chat(user_msg, bot_msg):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO chat_history (user_msg, bot_msg) VALUES (?, ?)", (user_msg, bot_msg))
    conn.commit()
    conn.close()

def add_user(username, password, is_admin=0):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, password, is_admin) VALUES (?, ?, ?)", (username, password, is_admin))
    conn.commit()
    conn.close()

def check_user(username, password):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cur.fetchone()
    conn.close()
    return user

def get_courses():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id, course_name, duration, fees FROM courses")
    courses = cur.fetchall()
    conn.close()
    return courses

def add_course(course_name, duration, fees):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO courses (course_name, duration, fees) VALUES (?, ?, ?)", (course_name, duration, fees))
    conn.commit()
    conn.close()

def delete_course(course_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM courses WHERE id=?", (course_id,))
    conn.commit()
    conn.close()

def get_users():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id, username, is_admin FROM users")
    users = cur.fetchall()
    conn.close()
    return users

def get_chat_history():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id, user_msg, bot_msg FROM chat_history ORDER BY id DESC")
    chats = cur.fetchall()
    conn.close()
    return chats

create_tables()