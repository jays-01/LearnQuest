import question_model
from data import question_data
from brain import QuizBrain
from ui import QuizInterface

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_ans = question["correct_answer"]
    new_question = question_model.Question(question_text,question_ans)
    question_bank.append(new_question)



quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_question():
#     quiz.next_question()
#     quiz.check_answer()


print(f"You've completed your quiz and your final score is : {quiz.score}/{quiz.question_number}")

