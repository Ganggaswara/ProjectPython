from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

q_data = question_data

question_bank = []
for question in q_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
