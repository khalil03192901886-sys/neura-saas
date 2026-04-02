import sqlite3

conn = sqlite3.connect("chat.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS chats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT,
    response TEXT
)
""")

conn.commit()

def save_chat(msg, res):
    cursor.execute("INSERT INTO chats (message, response) VALUES (?, ?)", (msg, res))
    conn.commit()
