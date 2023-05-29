from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_unsorted_n_distinct, get_two_distinct
from questions.src.question.year9.Types import Types, Complexity
from sympy import solve, Eq
from sympy.abc import a, b
import random

class Question18(BaseQuestion):

    def __init__(self):
        self.type = Types.line_equation
        self.complexity = Complexity.Moderate
        cand=[(5, -2, 8, a, 3),(-8,-9,-2,a,4),(3, -4, a, 10, 2),(-2, 5, 2, a, -0.5),(1, a, 5, 1, 0.75)]
        vals = random.sample(cand, 1)[0]

        grad = vals[4]
        const = vals[1] - grad*vals[0]
        
        sol = solve([ Eq( grad*vals[2] + const, vals[3])])
        self.q = f"A line is passing through ({vals[0]},{vals[1]}) and ({vals[2]},{vals[3]}) where its gradient is {grad}.  Find a"      
        self.res = f"{sol}"

    def question(self):
        return ""
    
    def graphic(self):
        return self.encode_graphics(self.q, 12)

    def answer(self):
        return "Answer: "

    def answer_graphic(self):
        return self.encode_graphics(self.res)


