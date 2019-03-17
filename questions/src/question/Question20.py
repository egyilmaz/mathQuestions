import random
from fractions import Fraction
from .Types import Types
from ..utils.Utility import ask_interactive_1arg


# Question type is simplify A/B
class Question20:
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.num = random.choice(range(2, 10)) * random.choice(range(1, 10))
        self.denum = random.choice(range(2, 7)) * random.choice(range(1, 5)) * random.choice(range(2, 6))
        self.res = Fraction(self.num, self.denum)
        self.body = "Simplify {num}/{denum}".format(num=self.num, denum=self.denum)

    def question(self):
        return self.body

    def ask_user(self):
        return self.val == ask_interactive_1arg(self.question())

    def result(self):
        return {self.res: str(self.res)}

    def answer(self):
        return "{res}".format(res=self.res)
