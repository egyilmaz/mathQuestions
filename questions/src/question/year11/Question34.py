from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_unsorted_n_distinct, get_two_distinct
from questions.src.question.year11.Types import Types, Complexity
import sympy as sp
from sympy.abc import x, y
import random

class Question34(BaseQuestion):

    def __init__(self):
        self.type = Types.factorise
        self.complexity = Complexity.Moderate
         # Define the variable
        x = sp.symbols('x')
        a = random.sample([6,7,8,9],1)[0]
        b = random.sample([2,3,4],1)[0]
        eqn = b*(a**2 - x**2)
        self.q = f"${b*a**2} - {b}x^2$"
        # Simplify the expression
        simplified_expr = sp.factor(eqn)
        self.res = f'${simplified_expr}$'

    def question(self):
        return "Factorise  "

    def graphic(self):
        return self.encode_graphics(self.q)

    def answer(self):
        return "Answer: "

    def answer_graphic(self):
        return self.encode_graphics(self.res)

