import random

from Question import Question
from data import results

quiz_questions = []
for question in results:
    quiz_question = Question(question['question'], question['correct_answer'])
    quiz_questions.append(quiz_question)

score = 0
counter = 0
random.shuffle(quiz_questions)
for question in quiz_questions:
    counter+=1
    score = question.quiz(score, counter)
    print(f"{score}/{counter}\n")