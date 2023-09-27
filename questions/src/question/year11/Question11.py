from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_unsorted_n_distinct, get_two_distinct
from questions.src.question.year11.Types import Types, Complexity
from sympy import solve, Eq
from sympy.abc import x, y
import random

class Question11(BaseQuestion):

    def __init__(self):
        self.type = Types.quad_formula
        self.complexity = Complexity.Moderate
        cand = [(3, 8, 2), (1, 5, -12), (1, -7, 3), (2,3,-7), (2, 9, -3), (7, 8, 1), (3, -1, -1), (1, -7, 4)]
        a,b,c = random.sample(cand,1)[0]
        #the form is a*x^2+bx+c       
        self.res =  solve([Eq(a*x**2 + b*x +c, 0)])
        if a == 1:
            a = ""
        if b == 1:
            b = ""
        self.q = f'${a}x^2 + {b}x + {c}=0$'

    def question(self):
        return "Solve the equation and give your answer correct to 3 significant figures "

    def graphic(self):
        return self.encode_graphics(self.q)

    def answer(self):
        return "Answer: "

    def answer_graphic(self):
        return self.encode_graphics(self.res)


