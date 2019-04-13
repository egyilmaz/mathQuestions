import random
from .BaseQuestion import BaseQuestion
from fractions import Fraction

# Question type is simplify A/B
class Question20(BaseQuestion):
    def __init__(self):
        self.num = random.choice(range(2, 10)) * random.choice(range(1, 10))
        self.denum = random.choice(range(2, 7)) * random.choice(range(1, 5)) * random.choice(range(2, 6))
        self.res = Fraction(self.num, self.denum)
        self.body = "Simplify {num}/{denum}".format(num=self.num, denum=self.denum)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
