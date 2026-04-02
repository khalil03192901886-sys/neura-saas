import sqlite3

conn = sqlite3.connect("saas.db", check_same_thread=False)
cursor = conn.cursor()

# USERS TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

# CHAT TABLE (USER BASED)
cursor.execute("""
CREATE TABLE IF NOT EXISTS chats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    message TEXT,
    response TEXT
)
""")

conn.commit()


# =====================
# USERS FUNCTIONS
# =====================

def create_user(username, password):
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       (username, password))
        conn.commit()
        return True
    except:
        return False


def verify_user(username, password):
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?",
                   (username, password))
    return cursor.fetchone()


# =====================
# CHAT SAVE
# =====================

def save_chat(username, message, response):
    cursor.execute("INSERT INTO chats (username, message, response) VALUES (?, ?, ?)",
                   (username, message, response))
    conn.commit()
