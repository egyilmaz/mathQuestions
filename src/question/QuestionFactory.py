from src.question.Types import Output


class QuestionFactory:

    def __init__(self, otype):
        self.sheet_number = 0
        self.output_type = otype

    def ask(self, nof_questions):
        if self.output_type == Output.PRINTED:
            self.ask_printed(nof_questions)
        if self.output_type == Output.ONLINE:
            self.ask_interactive(nof_questions)

    def ask_printed(self, nof_questions):
        self.sheet_number = self.sheet_number + 1
        postfix = str(self.sheet_number) + '.txt'
        with open('answers_' + postfix, 'w') as file_a, open('questions_' + postfix, 'w') as file_q:
            for i in range(0, nof_questions):
                q = self.__get_question__(i % 5)
                file_q.write(str(i+1) + ') ' + q.question())
                file_q.write('\n\n\n\n\n')
                file_a.write(str(i+1) + ') ' + ', '.join("{}: {}".format(k, str(v)) for k, v in q.result().items()))
                file_a.write('\n')

    def ask_interactive(self, nof_questions):
        for i in range(0, nof_questions):
            q = self.__get_question__(i % 5)
            if q.ask_user():
                print("\nWell done.")
            else:
                print("\nCheck my answer : " + q.answer())
            print('\n')

    @staticmethod
    def __get_question__(qtype):
        if qtype == 0:
            from src.question.Question1 import Question1
            return Question1()
        if qtype == 1:
            from src.question.Question2 import Question2
            return Question2()
        if qtype == 2:
            from src.question.Question3 import Question3
            return Question3()
        if qtype == 3:
            from src.question.Question4 import Question4
            return Question4()
        if qtype == 4:
            from src.question.Question5 import Question5
            return Question5()
        if qtype == 5:
            from src.question.Question6 import Question6
            return Question6()
        if qtype == 6:
            from src.question.Question7 import Question7
            return Question7()
        if qtype == 7:
            from src.question.Question8 import Question8
            return Question8()
        if qtype == 8:
            from src.question.Question9 import Question9
            return Question9()
        if qtype == 9:
            from src.question.Question12 import Question10
            return Question10()
