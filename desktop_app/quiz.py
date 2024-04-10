import tkinter as tk
from tkinter import messagebox
import json
import random

class QuizApp:
    def __init__(self, master, questions):
        self.master = master
        self.questions = questions
        self.current_question_index = 0
        
        self.master.title("Quiz App")
        
        self.question_label = tk.Label(self.master, text="", wraplength=400)
        self.question_label.pack(pady=10)
        
        self.option_buttons = []
        for i in range(5):
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
        selected_option = chr(97 + option_index)
        if selected_option == question['answer']:
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is: {question['answer']}")
        
        self.current_question_index += 1
        self.load_question()

def load_questions(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['questions']

def main():
    file_path = r'.\questions.json'
    questions = load_questions(file_path)
    random.shuffle(questions)
    
    root = tk.Tk()
    app = QuizApp(root, questions)
    root.mainloop()


if __name__ == "__main__":
    main()
