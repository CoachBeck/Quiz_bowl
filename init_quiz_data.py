import sqlite3

conn = sqlite3.connect("quiz_data.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        answer TEXT NOT NULL,
        subject TEXT NOT NULL
    )
''')

conn.commit()
conn.close()
print("✅ 'questions' table created successfully in quiz_data.db!")