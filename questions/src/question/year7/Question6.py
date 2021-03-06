from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_unsorted_n_distinct
from questions.src.question.year7.Types import Types, Complexity
import random


class Question6(BaseQuestion):

    coeff = [i for i in range(-21, -2)]

    def __init__(self):
        self.type = Types.algebra_negative_numbers
        self.complexity = Complexity.Basic
        self.var = random.sample(['x', 'y', 'z', 't', 'a', 'b', 'c'], 1)[0]
        rc = get_unsorted_n_distinct(Question6.coeff, 3)
        self.q = r'${c1} - ({c2} - {v}) = {c3}$ '.format(c1=rc[0], v =self.var, c2=rc[1], c3=rc[2])
        self.res = r'{r1}'.format(r1=(rc[2]-rc[0]+rc[1]))

    def question(self):
        return f"Find the value of {self.var}, given "

    def graphic(self):
        return self.encode_graphics(self.q)

    def answer(self):
        return f"{self.res}"

