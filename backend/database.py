import sqlite3
from datetime import datetime
# Create database connection
import pandas as pd

def export_tickets():

    conn = sqlite3.connect("tickets.db")

    df = pd.read_sql_query(
        "SELECT * FROM tickets",
        conn
    )

    conn.close()
    print(df.tail())
    df.to_csv(
        "ticket_report.csv",
        index=False
    )

    return "ticket_report.csv"

    columns = [
        "id",
        "ticket",
        "category",
        "sentiment",
        "retrieved_document",
        "created_at",
        "response"
    ]

    df = pd.DataFrame(
        rows,
        columns=columns
    )

    df.to_csv(
        "ticket_report.csv",
        index=False
    )

    return "ticket_report.csv"
conn = sqlite3.connect(
    "tickets.db",
    check_same_thread=False
)

cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket TEXT,
    category TEXT,
    sentiment TEXT,
    retrieved_document TEXT,
    created_at TEXT
)
""")

conn.commit()



def save_ticket(
    ticket,
    category,
    sentiment,
    retrieved_document,
    response
):

    created_at = datetime.now().strftime(
        "%d-%m-%Y %I:%M %p"
    )

    cursor.execute(
    """
    INSERT INTO tickets (
        ticket,
        category,
        sentiment,
        retrieved_document,
        created_at,
        response
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        ticket,
        category,
        sentiment,
        retrieved_document,
        created_at,
        response
    )
)

    conn.commit()

    
def get_all_tickets():

    conn = sqlite3.connect("tickets.db")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM tickets
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows
def get_ticket_stats():

    conn = sqlite3.connect("tickets.db")

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM tickets")
    total = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM tickets WHERE category='Billing'"
    )
    billing = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM tickets WHERE category='Shipping'"
    )
    shipping = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM tickets WHERE category='Technical'"
    )
    technical = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM tickets WHERE sentiment='NEGATIVE'"
    )
    escalated = cursor.fetchone()[0]

    conn.close()

    return {
        "total": total,
        "billing": billing,
        "shipping": shipping,
        "technical": technical,
        "escalated": escalated
    }