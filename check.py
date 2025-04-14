import sqlite3
import os

db_path = os.path.abspath("quiz_data.db")
print(f"Checking database at: {db_path}")

try:
    conn = sqlite3.connect("quiz_data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, question, answer, subject FROM questions")
    rows = cursor.fetchall()

    if rows:
        print(f"✅ {len(rows)} questions found in the database:")
        for row in rows:
            print(row)
    else:
        print("⚠️ No questions found in the database.")

    conn.close()
except Exception as e:
    print("❌ Error reading from database:", e)