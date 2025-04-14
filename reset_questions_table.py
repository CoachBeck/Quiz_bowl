import sqlite3

conn = sqlite3.connect("quiz_data.db")
cursor = conn.cursor()

# DANGER: This will delete all previous questions in the table
cursor.execute("DROP TABLE IF EXISTS questions")

# Create new table with multiple choice support
cursor.execute('''
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL,
    subject TEXT NOT NULL
)
''')

conn.commit()
conn.close()
print("✅ New 'questions' table created with multiple choice support.")