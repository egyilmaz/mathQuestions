import random
from fractions import Fraction
from src.question.Types import Types
from src.utils.Utility import ask_interactive_1arg


# Question type percentage of
class Question21:
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.num = 10*random.choice(range(1, 10))
        self.per = 10*random.choice(range(1, 10))
        self.res = self.num*self.per/100
        self.body = "Find {per}% of {num}".format(num=self.num, per=self.per)

    def question(self):
        return self.body

    def ask_user(self):
        return self.val == ask_interactive_1arg(self.question())

    def result(self):
        return {self.res: str(self.res)}

    def answer(self):
        return "{res}".format(res=self.res)
