import random
from .BaseQuestion import BaseQuestion


class Question21(BaseQuestion):
    def __init__(self):
        self.num = 10*random.choice(range(1, 10))
        self.per = 10*random.choice(range(1, 10))
        self.res = self.num*self.per/100
        self.body = "Find {per}% of {num}".format(num=self.num, per=self.per)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
