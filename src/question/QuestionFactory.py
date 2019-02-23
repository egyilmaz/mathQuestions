from src.resources.Resource import get_user_input
from src.resources.Resource import get_user_input_2arg


class QuestionFactory:

    def ask(self, qtype):
        q = self.__get_question__(int(qtype))
        print("\n" + str(q))
        if q.ask():
            print("\nWell done.")
        else:
            print("\nCheck my answer : " + q.answer())

    def get(self, qtype):
        return self.__get_question__(qtype)

    @staticmethod
    def __get_question__(qtype):
        if qtype == 1:
            from src.question.Question1 import Question1
            return Question1(get_user_input_2arg)
        if qtype == 2:
            from src.question.Question2 import Question2
            return Question2(get_user_input_2arg)
        if qtype == 3:
            from src.question.Question3 import Question3
            return Question3(get_user_input_2arg)
        if qtype == 4:
            from src.question.Question4 import Question4
            return Question4(get_user_input)
        if qtype == 5:
            from src.question.Question5 import Question5
            return Question5(get_user_input)
