import sqlite3

conn = sqlite3.connect("tickets.db")

cursor = conn.cursor()

try:
    cursor.execute("""
    ALTER TABLE tickets
    ADD COLUMN created_at TEXT
    """)
    conn.commit()
    print("Column added successfully.")
except Exception as e:
    print(e)

conn.close()