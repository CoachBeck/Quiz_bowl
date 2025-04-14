from tkinter import *
from tkinter import ttk, messagebox
from admin_add_questions import show_add_question
import sqlite3

DB_NAME = "quiz_data.db"

def show_admin_dashboard():
    dashboard = Tk()
    dashboard.title("Admin Dashboard")
    dashboard.geometry("300x250")

    Label(dashboard, text="Admin Panel", font=("Arial", 16)).pack(pady=15)

    Button(dashboard, text="Add Question", width=20, command=lambda: go_to_add(dashboard)).pack(pady=5)
    Button(dashboard, text="Manage Questions", width=20, command=lambda: go_to_manage(dashboard)).pack(pady=5)
    Button(dashboard, text="Back to Main Menu", width=20, command=lambda: go_back(dashboard)).pack(pady=10)

def go_to_add(current_window):
    current_window.destroy()
    show_add_question()

def go_back(current_window):
    current_window.destroy()
    from main import main
    main()

def go_to_manage(current_window):
    current_window.destroy()
    manage_win = Tk()
    manage_win.title("Manage Questions")
    manage_win.geometry("800x600")

    selected_id = None

    # Entry fields
    Label(manage_win, text="Question:").pack()
    question_entry = Entry(manage_win, width=80)
    question_entry.pack()

    Label(manage_win, text="Option A:").pack()
    option_a_entry = Entry(manage_win, width=80)
    option_a_entry.pack()

    Label(manage_win, text="Option B:").pack()
    option_b_entry = Entry(manage_win, width=80)
    option_b_entry.pack()

    Label(manage_win, text="Option C:").pack()
    option_c_entry = Entry(manage_win, width=80)
    option_c_entry.pack()

    Label(manage_win, text="Option D:").pack()
    option_d_entry = Entry(manage_win, width=80)
    option_d_entry.pack()

    Label(manage_win, text="Correct Answer (A/B/C/D):").pack()
    correct_answer_var = StringVar()
    correct_entry = Entry(manage_win, textvariable=correct_answer_var, width=10)
    correct_entry.pack()

    Label(manage_win, text="Subject:").pack()
    subject_var = StringVar()
    subject_dropdown = ttk.Combobox(manage_win, textvariable=subject_var, width=77)
    subject_dropdown['values'] = (
        "Quality and Productivity Systems",
        "Business Strategy",
        "Business Applications Development",
        "Management Information Systems",
        "Business Intelligence and Analytics"
    )
    subject_dropdown.pack()

    # Treeview to list questions
    tree = ttk.Treeview(manage_win, columns=("ID", "Question", "Correct", "Subject"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Question", text="Question")
    tree.heading("Correct", text="Correct Answer")
    tree.heading("Subject", text="Subject")
    tree.pack(fill="both", expand=True, pady=10)

    def load_questions():
        for row in tree.get_children():
            tree.delete(row)
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id, question, correct_answer, subject FROM questions")
        for row in cursor.fetchall():
            tree.insert('', 'end', values=row)
        conn.close()

    def select_row(event):
        nonlocal selected_id
        selected = tree.focus()
        values = tree.item(selected, 'values')
        if values:
            selected_id = values[0]
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute("SELECT question, option_a, option_b, option_c, option_d, correct_answer, subject FROM questions WHERE id = ?", (selected_id,))
            data = cursor.fetchone()
            conn.close()
            question_entry.delete(0, END)
            question_entry.insert(0, data[0])
            option_a_entry.delete(0, END)
            option_a_entry.insert(0, data[1])
            option_b_entry.delete(0, END)
            option_b_entry.insert(0, data[2])
            option_c_entry.delete(0, END)
            option_c_entry.insert(0, data[3])
            option_d_entry.delete(0, END)
            option_d_entry.insert(0, data[4])
            correct_answer_var.set(data[5])
            subject_var.set(data[6])

    def update_question():
        if not selected_id:
            messagebox.showwarning("Select", "Please select a question to update.")
            return
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE questions
            SET question=?, option_a=?, option_b=?, option_c=?, option_d=?, correct_answer=?, subject=?
            WHERE id=?
        ''', (
            question_entry.get(), option_a_entry.get(), option_b_entry.get(), option_c_entry.get(),
            option_d_entry.get(), correct_answer_var.get(), subject_var.get(), selected_id
        ))
        conn.commit()
        conn.close()
        load_questions()
        clear_entries()

    def delete_question():
        if not selected_id:
            messagebox.showwarning("Select", "Please select a question.")
            return
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM questions WHERE id=?", (selected_id,))
        conn.commit()
        conn.close()
        load_questions()
        clear_entries()

    def clear_entries():
        nonlocal selected_id
        selected_id = None
        question_entry.delete(0, END)
        option_a_entry.delete(0, END)
        option_b_entry.delete(0, END)
        option_c_entry.delete(0, END)
        option_d_entry.delete(0, END)
        correct_answer_var.set("")
        subject_var.set("")

    Button(manage_win, text="Update", command=update_question).pack(pady=5)
    Button(manage_win, text="Delete", command=delete_question).pack(pady=5)

    tree.bind("<ButtonRelease-1>", select_row)
    load_questions()