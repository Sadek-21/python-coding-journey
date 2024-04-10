// Define variables
let currentQuestionIndex = 0;
let score = 0;
const quizContainer = document.querySelector('.quiz-container');
const questionElement = document.getElementById('question');
const optionsContainer = document.getElementById('options');
const nextButton = document.getElementById('next-btn');
const submitButton = document.getElementById('submit-btn');

// Fetch questions from JSON file
fetch('questions.json')
    .then(response => response.json())
    .then(data => {
        const questions = data.questions;
        displayQuestion(questions[currentQuestionIndex]);
    })
    .catch(error => console.error('Error fetching questions:', error));

// Function to display question and options
function displayQuestion(question) {
    questionElement.textContent = question.question;
    optionsContainer.innerHTML = '';

    question.options.forEach((option, index) => {
        const optionElement = document.createElement('div');
        optionElement.classList.add('option');
        optionElement.textContent = `${index + 1}. ${option}`;
        optionElement.setAttribute('data-index', index);
        optionElement.addEventListener('click', selectOption);
        optionsContainer.appendChild(optionElement);
    });
}

// Function to handle option selection
function selectOption(event) {
    const selectedOptionIndex = parseInt(event.target.getAttribute('data-index'));
    const correctOptionIndex = questions[currentQuestionIndex].correctIndex;

    if (selectedOptionIndex === correctOptionIndex) {
        score++;
    }
}

// Event listener for next button
nextButton.addEventListener('click', () => {
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.length) {
        displayQuestion(questions[currentQuestionIndex]);
    } else {
        endQuiz();
    }
});

// Function to end the quiz
function endQuiz() {
    // Display final score or perform any other action
}

// Event listener for submit button
submitButton.addEventListener('click', () => {
    endQuiz();
});
