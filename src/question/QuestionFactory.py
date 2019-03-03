from src.utils.Utility import ask_interactive_1arg, ask_interactive_2arg
from src.question.Types import Types
from src.question.Types import Output


class QuestionFactory:

    def __init__(self, otype):
        self.sheet_number = 0
        self.output_type = otype

    def ask(self):
        if self.output_type == Output.PRINTED:
            self.ask_printed()
        if self.output_type == Output.ONLINE:
            for i in range(1, 6):
                self.ask_interactive(i)

    def ask_printed(self):
        self.sheet_number = self.sheet_number + 1
        postfix = str(self.sheet_number) + '.txt'
        with open('answers_' + postfix, 'a') as file_a, open('questions_' + postfix, 'a') as file_q:
            for i in range(1, 6):
                q = self.__get_question__(i)
                file_q.write(str(i) + ') ' + str(q) + ' ' + q.question_text)
                file_q.write('\n\n\n\n\n')
                file_a.write(str(i) + ') ' + ', '.join("{}: {}".format(k, str(v)) for k, v in q.result().items()))
                file_a.write('\n')

    def ask_interactive(self, qtype):
        q = self.__get_question__(int(qtype))
        print("\n" + str(q))
        if q.type == Types.FIRST_ORDER_2_UNKNOWN:
            first,second = ask_interactive_2arg(q.question_text, q.subj1, q.subj2)

        if q.type == Types.FIRST_ORDER_1_UNKNOWN:
            result = ask_interactive_1arg(q.question_text, q.subj1)

        if result:
            print("\nWell done.")
        else:
            print("\nCheck my answer : " + q.answer())

    @staticmethod
    def __get_question__(qtype):
        if qtype == 1:
            from src.question.Question1 import Question1
            return Question1()
        if qtype == 2:
            from src.question.Question2 import Question2
            return Question2()
        if qtype == 3:
            from src.question.Question3 import Question3
            return Question3()
        if qtype == 4:
            from src.question.Question4 import Question4
            return Question4()
        if qtype == 5:
            from src.question.Question5 import Question5
            return Question5()
