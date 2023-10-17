from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random
import sympy as sp

class Question44(BaseQuestion):

    def __init__(self):
        self.type = Types.sphere
        self.complexity = Complexity.Basic
        theList = [1,2,3,4,5,6]
        r_a = random.sample(theList,1)[0]
        v_a = sp.nsimplify((4/3)*r_a**3)
        s_a = 4*r_a**2
        self.q = f"Given the radius of a sphere A, $r_A={{{r_a}}}$, Find the surface area and volume of it. Give your answers in $\pi$"

        self.res= f"Surface Area = $4 \pi r^2 =$ {sp.nsimplify(s_a)}$\pi$ Volume = $\\frac{{4}}{{3}} \pi r^3$ = {sp.nsimplify(v_a)}$\pi$"

    def question(self):
        return ""

    def graphic(self):
        return self.encode_graphics(self.q,  14)

    def answer(self):
        return ""

    def answer_graphic(self):
        return self.encode_graphics(self.res, 15)
