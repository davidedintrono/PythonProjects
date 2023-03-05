from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for elem in question_data:
    text = elem["question"]
    answer = elem["correct_answer"]
    new_obj = Question(text, answer)
    question_bank.append(new_obj)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score  was {quiz.score}/{quiz.question_number}")