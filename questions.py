# question.py

class Question:
    def __init__(self, text, options, correct_letter):
        self.text = text
        self.options = options  # List of 4 options
        self.correct_letter = correct_letter  # A/B/C/D
        self.letter_to_index = {"A": 0, "B": 1, "C": 2, "D": 3}
        self.correct_answer = self.options[self.letter_to_index[self.correct_letter]]

    def is_correct(self, selected):
        return selected == self.correct_answer