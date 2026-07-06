import sqlite3

conn = sqlite3.connect("tickets.db")

cursor = conn.cursor()

try:
    cursor.execute("""
    ALTER TABLE tickets
    ADD COLUMN response TEXT
    """)
    
    conn.commit()
    print("Response column added successfully.")

except Exception as e:
    print(e)

conn.close()