from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_unsorted_n_distinct, get_two_distinct
from questions.src.question.year11.Types import Types, Complexity
import sympy as sp
from sympy.abc import x, y
import random

class Question33(BaseQuestion):

    def __init__(self):
        self.type = Types.factorise
        self.complexity = Complexity.Moderate
         # Define the variable
        x = sp.symbols('x')
        eqns=[("(x+1)*(x+2) / (2*(x+1)**2)","$\dfrac{(x+1)(x+2)}{2(x+1)^2}$"),
              ("(x-1)*(x+1) / (2*(x-1)**2)","$\dfrac{(x-1)(x+1)}{2(x-1)^2}$"),
              ("(x**2-1) / ((x-1)**2)","$\dfrac{x^2-1}{(x-1)^2}$"),
              ]
        # Define the expression
        expr, self.q = random.sample(eqns, 1)[0]

        # Simplify the expression
        simplified_expr = sp.simplify(expr)
        self.res = f'${simplified_expr}$'

    def question(self):
        return "Simplify  "

    def graphic(self):
        return self.encode_graphics(self.q)

    def answer(self):
        return "Answer: "

    def answer_graphic(self):
        return self.encode_graphics(self.res)


