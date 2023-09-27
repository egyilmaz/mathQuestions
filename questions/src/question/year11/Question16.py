from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_unsorted_n_distinct, get_two_distinct
from questions.src.question.year11.Types import Types, Complexity
from sympy import solve, Eq
from sympy.abc import x, y
import random

class Question16(BaseQuestion):

    def __init__(self):
        self.type = Types.quad_challenge
        self.complexity = Complexity.Moderate
        a = random.sample([ 2, 3, 4],1)[0]
        b = random.sample([5, 6, 8, 10],1)[0]

        nsec = random.sample([2, 3, 4, 5],1)[0]

        self.q = f"$h = {a*b}t - {a}{{t}}^2$. What will be the height after {nsec} seconds. " \
        "When will the ball be hitting the ground, i.e h = 0"
        
        ball_after_n_sec = a*b*nsec - a*nsec*nsec
        ball_on_gnd =  solve([Eq((a*b*x - a*x*x), 0)])
        
        self.res = f"After {nsec} seconds height is {ball_after_n_sec} meter. The time when the ball hits the ground h=0 is {ball_on_gnd}"

    def question(self):
        return "A cannon fires a ball with an angle. The height of the flying ball is defined as a quadratic function as "

    def graphic(self):
        return self.encode_graphics(self.q, 12)

    def answer(self):
        return "Answer: "

    def answer_graphic(self):
        return self.encode_graphics(self.res)


