from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_unsorted_n_distinct, get_two_distinct
from questions.src.question.year9.Types import Types, Complexity
from sympy import expand,symbols
from sympy.abc import x, y
import random

class Question9(BaseQuestion):

    def __init__(self):
        self.type = Types.expand_triple
        self.complexity = Complexity.Moderate
        cand = [10, 100, 1000]
        a = random.sample(cand,1)[0]
        b = random.sample([-1,1],1)[0]
        c = random.sample([2,3,4],1)[0]
        self.q = r'${{{v1}}}^\dfrac{{{v2}}}{{{v3}}}$'.format(v1=a,v2=b, v3=c)
        self.res = " "

    def question(self):
        return "Expand then simplfy  "

    def graphic(self):
        return self.encode_graphics(self.q)

    def answer(self):
        return f"Answer: "

    def answer_graphic(self):
        return self.encode_graphics(self.res)


