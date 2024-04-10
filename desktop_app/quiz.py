import json
import random

def load_questions(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['questions']

def randomize_questions(questions):
    random.shuffle(questions)
    return questions

def main():
    file_path = 'questions.json'
    questions = load_questions(file_path)
    randomized_questions = randomize_questions(questions)
    
    for question in randomized_questions:
        print(f"{question['id']}. {question['question']}")
        for i, option in enumerate(question['options']):
            print(f"{chr(97+i)}: {option}")
        
        user_answer = input("Your answer (a, b, c, d, e): ").lower()
        if user_answer == question['answer']:
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", question['answer'])

if __name__ == "__main__":
    main()
