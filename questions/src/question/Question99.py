import random
from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity


class Question99(BaseQuestion):
    def __init__(self):
        self.type = [Types.Arithmetic,Types.sat_arithmetic]
        self.complexity = Complexity.Basic
        self.first = random.choice([177423, 188099, 988203, 199199, 234567, 100020, 200001])
        self.second = random.choice([19999, 18888, 13456, 10001, 63999, 12345, 56789, 99999])
        self.body = "{0} + {1} and {0} - {1} = ".format(self.first,self.second)
        self.res="{0} and {1}".format(self.first+self.second, self.first-self.second)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
