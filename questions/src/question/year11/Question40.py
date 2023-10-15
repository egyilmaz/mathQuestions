from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random
import sympy as sp

class Question40(BaseQuestion):

    def __init__(self):
        self.type = Types.simplify_power
        self.complexity = Complexity.Complex
        a = random.sample([5,6,7],1)[0]
        b = random.sample([2,3,4],1)[0]
        c = random.sample([1,2,3],1)[0]
        d = random.sample([2,3,4],1)[0]
        num = f"{{{a}}}^{{{c}}}"
        denum = f"{{{a}}}\sqrt{{{a}}}"
        num2 = "x*y"
        self.q = f'${{{a}}}\sqrt{{{a**c}}} = {{{a}}}^{{{{{b}}}x}} $  and  $\\frac{{{num}}}{{{denum}}}  = {{{a}}}^{{(y{{{-b}}})}}$ calculate $\\frac{{{num2}}}{{{d}}}$ and leave the result as a fraction in simplest form'
        x = (1+c/2)/b
        y = (b+c-3/2)
        self.res = sp.nsimplify(x*y/d, rational=False)

    def question(self):
        return "Given  "

    def graphic(self):
        return self.encode_graphics(self.q,  12)

    def answer(self):
        return "{res}".format(res=self.res)

