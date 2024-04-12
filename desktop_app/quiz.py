import tkinter as tk
from tkinter import messagebox
import json
import random
import os
import sys

class QuizApp:
    def __init__(self, master, questions):
        self.master = master
        self.questions = questions
        self.current_question_index = 0
        
        self.master.title("Quiz App")
        
        self.question_label = tk.Label(self.master, text="", wraplength=400)
        self.question_label.pack(pady=10)
        
        self.option_buttons = []
        for i in range(len(self.questions[0]['options'])):  # Ensures correct number of options
            button = tk.Button(self.master, text="", width=30, command=lambda idx=i: self.select_option(idx))
            button.pack(pady=5)
            self.option_buttons.append(button)
        
        self.load_question()
    
    def load_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.question_label.config(text=question['question'])
            for i, option in enumerate(question['options']):
                self.option_buttons[i].config(text=option)
        else:
            messagebox.showinfo("Quiz Finished", "You have completed the quiz!")
            self.master.destroy()

    def select_option(self, option_index):
        question = self.questions[self.current_question_index]
        if option_index == question['answer_index']:
            messagebox.showinfo("Result", "Correct!")
        else:
            correct_option = question['options'][question['answer_index']]
            messagebox.showinfo("Result", f"Incorrect. The correct answer is: {correct_option}")
        
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.load_question()
        else:
            self.master.destroy()

def load_questions(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['questions']

def main():
    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))

    file_path = os.path.join(application_path, 'questions.json')
    questions = load_questions(file_path)
    random.shuffle(questions)
    
    root = tk.Tk()
    app = QuizApp(root, questions)
    root.mainloop()

if __name__ == "__main__":
    main()
