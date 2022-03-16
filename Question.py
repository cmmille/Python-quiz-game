class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return f'Q: {self.question}\nA: {self.answer}'

    def check_answer(self):
        """Get answer from user and check if it is correct. Returns true if correct"""
        user_input = input("What is the answer? (true/false)\t").capitalize()
        if user_input == self.answer:
            print("Correct!")
            return True
        else:
            print(f"Sorry, the correct answer was {self.answer}.")
            return False

    def display_question(self, question_number):
        q = (f"Q{question_number}: ")
        print("True or False?")
        print(q + self.question)

    def quiz(self, score, question_number):
        self.display_question(question_number)
        if self.check_answer():
            score+=1
        return score