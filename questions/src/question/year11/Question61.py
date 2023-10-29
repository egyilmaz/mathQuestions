from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random
import math

class Question61(BaseQuestion):

    def __init__(self):
        self.type = Types.surds
        self.complexity = Complexity.Basic
        a = random.uniform(4.1, 6.0)
        b = random.uniform(-4.0, 0)
        c = random.uniform(0.1, 6.0)
        a = round(a,1)
        b = round(b,2)
        c = round(c,3)
        eqn = math.sqrt((a+b)/c)

        self.q = f"Using a calculator, given a={a}, b={b}, c={c}, calculate the value $\\sqrt{{\\frac{{a + b}}{{c}}}}$ and round the result to 2dp."
        self.res = f'Raw result {eqn}, rounded {round(eqn,2)} '

    def graphic(self):
        return self.encode_graphics(self.q,  14)

    def answer_graphic(self):
        return self.encode_graphics(self.res, 15)

    def question(self):
        return f""

    def answer(self):
        return f""

