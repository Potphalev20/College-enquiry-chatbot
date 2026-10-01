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
    CREATE TABLE IF NOT EXISTS courses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT,
        duration TEXT,
        fees TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS chat_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_msg TEXT,
        bot_msg TEXT
    )
    """)

    conn.commit()
    conn.close()

    preload_data()

def preload_data():
    conn = connect()
    cur = conn.cursor()

    # Admin user
    cur.execute("SELECT * FROM users WHERE username='admin'")
    if not cur.fetchone():
        cur.execute("INSERT INTO users VALUES (NULL,?,?,?)", ("admin","admin123",1))

    # Courses
    cur.execute("SELECT * FROM courses")
    if not cur.fetchone():
        cur.executemany("INSERT INTO courses(course_name,duration,fees) VALUES (?,?,?)", [
            ("BCA","3 Years","₹1,00,000"),
            ("MCA","2 Years","₹1,50,000")
        ])

    conn.commit()
    conn.close()

# FUNCTIONS
def check_user(u,p):
    conn=connect();cur=conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=? AND password=?", (u,p))
    user=cur.fetchone()
    conn.close()
    return user

def get_courses():
    conn=connect();cur=conn.cursor()
    cur.execute("SELECT * FROM courses")
    data=cur.fetchall()
    conn.close()
    return data
def get_users():
    conn=connect();cur=conn.cursor()
    cur.execute("SELECT id,username,is_admin FROM users")
    data=cur.fetchall()
    conn.close()
    return data

def get_chat_history():
    conn=connect();cur=conn.cursor()
    cur.execute("SELECT * FROM chat_history")
    data=cur.fetchall()
    conn.close()
    return data

def add_course(n,d,f):
    conn=connect();cur=conn.cursor()
    cur.execute("INSERT INTO courses(course_name,duration,fees) VALUES (?,?,?)",(n,d,f))
    conn.commit();conn.close()

def delete_course(i):
    conn=connect();cur=conn.cursor()
    cur.execute("DELETE FROM courses WHERE id=?",(i,))
    conn.commit();conn.close()

create_tables()
