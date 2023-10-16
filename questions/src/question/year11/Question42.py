from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random
import sympy as sp

class Question42(BaseQuestion):

    def __init__(self):
        self.type = Types.surd_denum
        self.complexity = Complexity.Complex
        a = random.sample([2,3,4],1)[0]
        b = random.sample([2,3],1)[0]
        c = random.sample([2,3,5],1)[0]
        d = random.sample([-3,-2,-1,1,2,3],1)[0]
        num = f"(\sqrt{{{b*a**2}}} - \sqrt{{{b}}})^2"
        if d > 0:
            denum = f"\sqrt{{{c}}}+{{{d}}}"
        else:
            denum = f"\sqrt{{{c}}} {{{d}}}"
        self.q = f'Simplify $\\frac{{{num}}}{{{denum}}}$'

        x,y,t,k = sp.symbols('x y t k', real=True, positive=True)
        expression = ((x - y)**2)/(t+k)
        subs = {x:sp.sqrt(b*a**2), y:sp.sqrt(c), t: sp.sqrt(c), k:d}
        result = expression.subs(subs)
        self.res= f"${{{sp.simplify(result)}}}$"

    def question(self):
        return ""

    def graphic(self):
        return self.encode_graphics(self.q,  14)

    def answer(self):
        return ""

    def answer_graphic(self):
        return self.encode_graphics(self.res, 15)
