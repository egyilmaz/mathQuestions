from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random

class Question15(BaseQuestion):

    def __init__(self):
        self.type = Types.quad_formula
        self.complexity = Complexity.Moderate
        a = random.sample([ 2, 3, 4, 5],1)[0]
        b = random.sample([-6, -5, -4, -3 -2, 2, 3, 4, 5, 6],1)[0]
        c = random.sample([-8, -6, -4, -2, 2, 4, 6, 8],1)[0]

        four_ac = -4*a*c
        if four_ac > 0:
            four_ac = f"+{four_ac}"
        num = f"{-b} \pm \sqrt{{{b**2} {four_ac}}}"
        denum = f"{2*a}"
        self.q = f"If we substitute a, b, c of $a{{x}}^2 + bx + c$ into quadratic formula, we get $\\frac{{{num}}}{{{denum}}}$, Find a,b,c"
        self.res = f"a={a}, b={b}, c={c} the quadratic eqn: ${a}{{x}}^2 + {b}x + {c}$"

    def question(self):
        return " "

    def graphic(self):
        return self.encode_graphics(self.q, 12)

    def answer(self):
        return "Answer: "

    def answer_graphic(self):
        return self.encode_graphics(self.res)


