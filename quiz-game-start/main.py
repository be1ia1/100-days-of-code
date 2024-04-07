from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for item in question_data:
    question = Question(text=item['text'], answer=item['answer'])
    question_bank.append(question)

quiz = QuizBrain(question_list=question_bank)


while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")
