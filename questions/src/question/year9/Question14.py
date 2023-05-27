from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_unsorted_n_distinct, get_two_distinct
from questions.src.question.year9.Types import Types, Complexity
from sympy import solve, Eq
from sympy.abc import x, y
import random

class Question14(BaseQuestion):

    def __init__(self):
        self.type = Types.quad_trans
        self.complexity = Complexity.Moderate
        b = random.sample([-6, -4, -2, 2, 4, 6],1)[0]
        d = 2*random.sample([-8, -6, -4, -2, 2, 4, 6, 8],1)[0]
        mid = d+b
        if mid > 0:
            mid = f"+{mid}"
        last = d*b
        if last > 0:
            last = f"+{last}"
        if mid == 0:
            asked = f'$x^2 {last}$'
        else:
            asked = f'$x^2 {mid}x {last}$'

        roots =  solve([Eq((x + b)*(x+d), 0)])
        p = (d+b)/2
        q = -(p*p - d*b)
        self.res = f"$(x + {p})^2 {q}$ and p={p}, q={q}"
        self.q = f" {asked} in $(x+p)^2 + q$ form"

    def question(self):
        return "Rewrite "

    def graphic(self):
        return self.encode_graphics(self.q)

    def answer(self):
        return "Answer: "

    def answer_graphic(self):
        return self.encode_graphics(self.res)


