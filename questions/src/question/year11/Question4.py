from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_unsorted_n_distinct, get_two_distinct
from questions.src.question.year11.Types import Types, Complexity
from itertools import chain
import random
import sympy as sym
import matplotlib.pyplot as plt
import matplotlib

class Question4(BaseQuestion):

    def __init__(self):
        self.type = Types.simplfy_decimals
        self.complexity = Complexity.Moderate
        a = random.sample([1.8, 1.2, 1.0, -2.0, -2.4, -1.2],1)[0]
        b = random.sample([2, 3, -1, -2, -3],1)[0]
        c = random.sample([2, 3, 4, 5],1)[0]
        d = random.sample([2, 3, -1, -2, -3],1)[0]
        num=f"{a} x 10^{{{b}}}"
        denum=f"{c} x 10^{{{d}}}"
        sol = (a*(10**b)) / (c*(10**d)) 
        self.q = f"$\\frac{{{num}}}{{{denum}}}$"
        self.res = r'{r1}'.format(r1=sol)

    def question(self):
        return "Work out  "

    def graphic(self):
        return self.encode_graphics(self.q, 20)

    def answer(self):
        return "{res}".format(res=self.res)

