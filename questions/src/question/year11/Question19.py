from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_unsorted_n_distinct, get_two_distinct
from questions.src.question.year11.Types import Types, Complexity
from sympy import solve, Eq
from sympy.abc import a, b
import random

class Question19(BaseQuestion):

    def __init__(self):
        self.type = Types.line_equation_paralel
        self.complexity = Complexity.Moderate
        cand=[(2, -1, 1, 8),(3, 2, 1, 1),(5, -4, 2, 9),(3, -7, 4, 15),(4, 0, -1, 3),(-2, 5, -3, 0),(-0.5, 1, 3, 0),(-1, 10, 4, 0),(6,3,10,5)]
        vals = random.sample(cand, 1)[0]

        grad = vals[0]
        const = vals[1]
        x1 = vals[2]
        y1 = vals[3]
        
        if const > 0:
            const = f"+{const}"

        self.q = f"Write the equation of a line which is parallel to $ y = {grad}x {const}$ and passing throught ({x1},{y1})"      

        n = y1 - grad*x1
        if n > 0:
            n = f"+{n}"
        self.res = f"y = {grad}x {n}"

    def question(self):
        return ""
    
    def graphic(self):
        return self.encode_graphics(self.q, 12)

    def answer(self):
        return "Answer: "

    def answer_graphic(self):
        return self.encode_graphics(self.res)


