import sqlite3

DB_NAME = "quiz_data.db"

CATEGORIES = [
    "Quality and Productivity Systems",
    "Business Strategy",
    "Business Applications Development",
    "Management Information Systems",
    "Business Intelligence and Analytics"
]

def connect():
    return sqlite3.connect(DB_NAME)

def create_table():
    with connect() as conn:
        c = conn.cursor()
        c.execute('''
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


def add_question(subject, question, option1, option2, option3, option4, correct_answer_text):
    # Convert answer text to A/B/C/D
    letter_map = {
        option1: "A",
        option2: "B",
        option3: "C",
        option4: "D"
    }
    correct_letter = letter_map.get(correct_answer_text, "A")  # Default to A

    with connect() as conn:
        c = conn.cursor()
        c.execute('''
            INSERT INTO questions (question, option_a, option_b, option_c, option_d, correct_answer, subject)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (question, option1, option2, option3, option4, correct_letter, subject))
        conn.commit()

def get_questions(subject):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT question, option_a, option_b, option_c, option_d, correct_answer
        FROM questions
        WHERE subject = ?
    ''', (subject,))
    questions = cursor.fetchall()
    conn.close()
    return questions