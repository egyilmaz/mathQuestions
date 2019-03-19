from .Types import Output
from ..utils.Utility import get_n_distinct
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def plot():
    x=range(1,10)
    y=x
    plt.plot(x,y)
    buf = BytesIO()
    plt.savefig(buf, format='PNG', dpi=100)
    graphic = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n','')
    buf.close()
    return graphic


nof_registered_questions = 21

class QuestionFactory:

    def __init__(self, otype):
        self.sheet_number = 0
        self.output_type = otype

    def ask(self, nof_questions):
        if self.output_type == Output.PRINTED:
            self.ask_printed(nof_questions)
        if self.output_type == Output.ONLINE:
            return self.ask_question(nof_questions)
        if self.output_type == Output.INTERACTIVE:
            self.ask_interactive(nof_questions)

    def ask_question(self, nof_questions):
        if nof_questions > nof_registered_questions:
            nof_questions = nof_registered_questions
        bunch = get_n_distinct(range(0,nof_registered_questions),nof_questions)
        result = []
        for i in bunch:
            question = self.__get_question__(i)
            result.append((question.question(),question.graphic()))
        return result

    def ask_printed(self, nof_questions):
        self.sheet_number = self.sheet_number + 1
        postfix = str(self.sheet_number) + '.txt'
        with open('answers_' + postfix, 'w') as file_a, open('questions_' + postfix, 'w') as file_q:
            for i in range(0, nof_questions):
                q = self.__get_question__(i % nof_registered_questions)
                file_q.write(str(i+1) + ') ' + q.question())
                file_q.write('\n\n\n\n\n')
                file_a.write(str(i+1) + ') ' + ', '.join("{}: {}".format(k, str(v)) for k, v in q.result().items()))
                file_a.write('\n')

    def ask_interactive(self, nof_questions):
        for i in range(0, nof_questions):
            q = self.__get_question__(i % nof_registered_questions)
            if q.ask_user():
                print("\nWell done.")
            else:
                print("\nCheck my answer : " + q.answer())
            print('\n')

    @staticmethod
    def __get_question__(qtype):
        if qtype == 0:
            from .Question1 import Question1
            return Question1()
        if qtype == 1:
            from .Question2 import Question2
            return Question2()
        if qtype == 2:
            from .Question3 import Question3
            return Question3()
        if qtype == 3:
            from .Question4 import Question4
            return Question4()
        if qtype == 4:
            from .Question5 import Question5
            return Question5()
        if qtype == 5:
            from .Question6 import Question6
            return Question6()
        if qtype == 6:
            from .Question7 import Question7
            return Question7()
        if qtype == 7:
            from .Question8 import Question8
            return Question8()
        if qtype == 8:
            from .Question9 import Question9
            return Question9()
        if qtype == 9:
            from .Question10 import Question10
            return Question10()
        if qtype == 10:
            from .Question11 import Question11
            return Question11()
        if qtype == 11:
            from .Question12 import Question12
            return Question12()
        if qtype == 12:
            from .Question13 import Question13
            return Question13()
        if qtype == 13:
            from .Question14 import Question14
            return Question14()
        if qtype == 14:
            from .Question15 import Question15
            return Question15()
        if qtype == 15:
            from .Question16 import Question16
            return Question16()
        if qtype == 16:
            from .Question17 import Question17
            return Question17()
        if qtype == 17:
            from .Question18 import Question18
            return Question18()
        if qtype == 18:
            from .Question19 import Question19
            return Question19()
        if qtype == 19:
            from .Question20 import Question20
            return Question20()
        if qtype == 20:
            from .Question21 import Question21
            return Question21()
