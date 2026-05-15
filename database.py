import sqlite3
from datetime import datetime
import pytz

DB_NAME = "quiz.db"

# ---------------- INIT DB ----------------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        score INTEGER,
        total INTEGER,
        date_time TEXT
    )
    """)

    conn.commit()
    conn.close()


# ---------------- INSERT RESULT ----------------
def insert_result(email, score, total):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # IST Time
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute("""
    INSERT INTO results (email, score, total, date_time)
    VALUES (?, ?, ?, ?)
    """, (email, score, total, current_time))

    conn.commit()
    conn.close()


# ---------------- GET RESULTS ----------------
def get_results(email):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, email, score, total, date_time
    FROM results
    WHERE email = ?
    ORDER BY id DESC
    """, (email,))

    data = cursor.fetchall()
    conn.close()

    return data


# ---------------- GET ATTEMPT COUNT ----------------
def get_attempt_count(email):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*) FROM results WHERE email = ?
    """, (email,))

    count = cursor.fetchone()[0]
    conn.close()

    return count