from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random
import sympy as sp

class Question41(BaseQuestion):

    def __init__(self):
        self.type = Types.surd_denum
        self.complexity = Complexity.Moderate
        theList = [(2,3,3,1),(2,2,2,2),(2,2,2,3),(2,3,3,3),(2,3,3,-3),
                   (3,2,2,-1),(3,3,3,-2),(3,3,3,2),(3,3,3,3),
                   (4,2,2,-2),(4,2,2,2),(4,3,3,-2),(4,2,2,1),(4,3,3,-1)]
        a,b,c,d = random.sample(theList,1)[0]
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

