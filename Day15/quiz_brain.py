class QuizBrain :
    def __init__(self, question_list, question_num = 0 ) -> None:
        self.question_num = question_num
        self.question_list = question_list
        self.score = 0

    def still_has_question(self) :
        if self.question_num < len(self.question_list) :
            return True
        else :
            
            return False

    def next_question(self) :
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num } : {current_question.text} (True/False) : ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer) :
        if user_answer.lower() == correct_answer.lower() :
            print("You got it right !")
            self.score += 1
            print(f"Your current score is : {self.score} / {self.question_num}")
        else :
            print("That's Wrong. ")
        print(f"The corrrect answer was : {correct_answer}")
        print(f"Your current score is : {self.score} / {self.question_num}")
        print("\n")
        
        if self.question_num == 12 :
            print("You've completed the quiz")
            print(f"Your final score is {self.score} / {self.question_num}")


    
