from question_model import Question

class QuizBrain:
    def __init__(self, question_list: list[Question]) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question: Question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answer(user_answer, question.answer)

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_answer: str, question_answer) -> bool:
        if str(user_answer).lower() == question_answer.lower():
            self.score += 1
            print("You got in right!")
        else:
            print("Thet's wrong.")
        print(f"The correct answer was: {question_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
