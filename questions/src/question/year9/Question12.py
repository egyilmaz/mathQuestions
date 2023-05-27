from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_unsorted_n_distinct, get_two_distinct
from questions.src.question.year9.Types import Types, Complexity
from sympy import solve, Eq
from sympy.abc import x, y
import random

class Question12(BaseQuestion):

    def __init__(self):
        self.type = Types.find_roots
        self.complexity = Complexity.Moderate
        cand = [-7,-6,-5,-4,-3,-2,2,3,4,5,6,7]
        b = random.sample(cand,1)[0]
        d = random.sample(cand,1)[0]

        mid = d+b
        if mid > 0:
            mid = f"+{mid}"
        last = d*b
        if last > 0:
            last = f"+{last}"        

        if mid == 0:
            self.q = f'$x^2 {last}=0$'
        else:
            self.q = f'$x^2 {mid}x {last}=0$'

        self.res =  solve([Eq((x + b)*(x + d), 0)])

    def question(self):
        return "Find the roots of  the given quadratic equation "

    def graphic(self):
        return self.encode_graphics(self.q)

    def answer(self):
        return "Answer: "

    def answer_graphic(self):
        return self.encode_graphics(self.res)


