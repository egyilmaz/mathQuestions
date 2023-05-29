from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_unsorted_n_distinct, get_two_distinct
from questions.src.question.year9.Types import Types, Complexity
from sympy import solve, Eq
from sympy.abc import x, y
import random

class Question17(BaseQuestion):

    def __init__(self):
        self.type = Types.line_equation
        self.complexity = Complexity.Moderate
        cand = [(1,4,3,10),(0,0,3,12),(5,-2, 9, 14),(-8,6,0,-2),(-5, -9,1,3),(-7, -2, 1, -4),(-2, 1, 8, -7),(-2,9,4,7),(-4.5,3,6,-7.5)]
        cand += [(2,5,4,11),(-4,2,1,7),(-5,-8,-4,-4),(-1, -2, -6, 3),(-6,-4,-3,2),(3,5,4,1),(-5,4,5,2),(1,6,5,4),(-10,-5,-7,4)]
        (x1,y1,x2,y2) = random.sample(cand, 1)[0]

        if (x2-x1)==0:
            x2 += 1
        grad = (y2-y1)/(x2-x1)
        const = y1 - grad*x1
        self.q = f"Find the line equation that passes through ({x1},{y1}) and ({x2},{y2})"      
        self.res = f"$ y = {grad}x + {const}$"

    def question(self):
        return " "
    
    def graphic(self):
        return self.encode_graphics(self.q, 12)

    def answer(self):
        return "Answer: "

    def answer_graphic(self):
        return self.encode_graphics(self.res)


