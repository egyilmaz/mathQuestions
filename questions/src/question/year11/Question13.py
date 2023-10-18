from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
from sympy import solve, Eq
from sympy.abc import x
import random

class Question13(BaseQuestion):

    def __init__(self):
        self.type = Types.parabola
        self.complexity = Complexity.Moderate
        cand = [-6,-5,-4,-3,-2,2,3,4,5,6]
        b = random.sample(cand,1)[0]
        d = random.sample(cand,1)[0]
        mid = d+b
        if mid > 0:
            mid = f"+{mid}"
        last = d*b
        if last > 0:
            last = f"+{last}"
        if mid == 0:
            self.q = f'$x^2 {last}$'
        else:
            self.q = f'$x^2 {mid}x {last}$'

        roots =  solve([Eq((x + b)*(x+d), 0)])
        tp_x = -(d+b)/2
        tp_y = (tp_x + b)*(tp_x+d)
        self.res = f"roots={roots}, y-intercept={last}, turning-point={tp_x,tp_y}"

    def question(self):
        return "Find the y-intercept, x-intercept and turning point for the given parabola "

    def graphic(self):
        return self.encode_graphics(self.q)

    def answer(self):
        return "Answer: "

    def answer_graphic(self):
        return self.encode_graphics(self.res)


