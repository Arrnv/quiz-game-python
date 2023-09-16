class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        item = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no}: {item.text}(True/False)")
        self.check_answer(user_answer, item.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got the answer right.")
            self.score += 1
        else:
            print("You got it wrong.")
        print(f"Correct answer is: {correct_answer}")
        print(f"Your score is: {self.score}/{self.question_no}")
        print("\n")
