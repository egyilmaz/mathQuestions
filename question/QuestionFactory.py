class QuestionFactory:

    def ask(self, qtype):
        q = self.__getQuestion__(int(qtype))
        print("\n" + str(q))
        if q.ask():
            print("\nWell done.")
        else:
            print("\nCheck my answer : " + q.answer())

    def get(self,qtype):
        return self.__getQuestion__(qtype)

    @staticmethod
    def __getQuestion__(qtype):
        if qtype == 1:
            from question.Question1 import Question1
            return Question1()
        if qtype == 2:
            from question.Question2 import Question2
            return Question2()
        if qtype == 3:
            from question.Question3 import Question3
            return Question3()
        if qtype == 4:
            from question.Question4 import Question4
            return Question4()
        if qtype == 5:
            from question.Question5 import Question5
            return Question5()
