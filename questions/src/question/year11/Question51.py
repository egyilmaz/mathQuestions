from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random
from sympy import symbols, reduce_inequalities

class Question51(BaseQuestion):

    def __init__(self):
        self.type = Types.inequality
        self.complexity = Complexity.Moderate
        x = symbols('x')
        a = random.sample([3,4,5,6,7],1)[0]
        b = random.sample([4,5,6,7,8],1)[0]
        c = random.sample([-2-1,1,2],1)[0]
        d = random.sample([2,3,4],1)[0]
        ineq1 = x**2 < a**2
        ineq2 = (b-x)/d < (x + c)
        ineq1_str = f"$x^2 < {{{a**2}}}$"
        ineq2_str = f"$({{{b}}}-x)/{{{d}}} < (x + {{{c}}})$"
        self.q = f"If x is an integer, given the inequalities {ineq1_str} and {ineq2_str}, what is x ?"
        sol1 = reduce_inequalities([ineq1, ineq2], x)
        self.res= f"{sol1}"

    def question(self):
        return ""

    def graphic(self):
        return self.encode_graphics(self.q,  14)

    def answer(self):
        return ""

    def answer_graphic(self):
        return self.encode_graphics(self.res, 15)
