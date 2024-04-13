import tkinter as tk
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
        for i in range(len(self.questions[0]['options'])):
            btn = tk.Button(self.master, text="", width=30, bg='SystemButtonFace',
                            command=lambda idx=i: self.select_option(idx))
            btn.pack(pady=5)
            self.option_buttons.append(btn)
        
        self.load_question()
    
    def load_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.question_label.config(text=question['question'])
            for i, option in enumerate(question['options']):
                self.option_buttons[i].config(text=option, bg='SystemButtonFace', state='normal')
        else:
            tk.messagebox.showinfo("Quiz Finished", "You have completed the quiz!")  # If you want to use this, add `from tkinter import messagebox`
            self.master.destroy()

    def select_option(self, option_index):
        question = self.questions[self.current_question_index]
        correct_index = question['answer_index']
        for btn in self.option_buttons:
            btn.config(state='disabled')  # Disable all buttons after selection
        if option_index == correct_index:
            self.option_buttons[option_index].config(bg='green')
        else:
            self.option_buttons[option_index].config(bg='red')
            self.option_buttons[correct_index].config(bg='green')

        self.current_question_index += 1
        self.master.after(1500, self.load_next_question)  # Wait 1500 ms before next question

    def load_next_question(self):
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