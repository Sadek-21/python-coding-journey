from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def index():
    return 'Welcome to the Quiz App!'

# Define a route for displaying the quiz page
@app.route('/quiz')
def quiz():
    return 'This is the Quiz Page'

# Define a route for handling AJAX requests to fetch questions
@app.route('/get_questions')
def get_questions():
    # Here you would fetch questions from your JSON file or database
    # For now, let's return a dummy list of questions
    questions = [
        {'id': 1, 'question': 'What is the capital of France?', 'options': ['Paris', 'London', 'Berlin', 'Rome'], 'answer': 'Paris'},
        {'id': 2, 'question': 'Who wrote "Romeo and Juliet"?', 'options': ['Shakespeare', 'Hemingway', 'Tolkien', 'Austen'], 'answer': 'Shakespeare'}
    ]
    return {'questions': questions}

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
