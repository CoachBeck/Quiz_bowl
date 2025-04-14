# Quiz Bowl Application

This is a Python-based Quiz Bowl application developed as part of a Business Information Technology course at Tennessee Tech University. 
It features a student quiz interface and an admin dashboard with full control over the quiz database.

Quiz Mode (for Students
- Choose from 5 course subjects
- Take multiple-choice quizzes
- See instant feedback (correct/incorrect)
- Score is shown at the end of the quiz

Admin Mode (Password Protected)
- Add new questions with 4 multiple-choice options
- Select the correct answer using A/B/C/D
- View all questions in a table
- Edit or delete any existing question
- Subject selection built-in to match course categories

SQLite Database
- Uses a single `quiz_data.db` file
- Questions table includes:
  - `question`, `option_a`, `option_b`, `option_c`, `option_d`
  - `correct_answer` (A/B/C/D)
  - `subject`

Subjects Included

- Quality and Productivity Systems  
- Business Strategy  
- Business Applications Development  
- Management Information Systems  
- Business Intelligence and Analytics  

Each subject includes 10 preloaded questions (total: 50).

How to Run the Application

1. Clone the repository or download the files.
2. Ensure you have Python 3 installed.
3. Run the `main.py` file:

```bash
python main.py
