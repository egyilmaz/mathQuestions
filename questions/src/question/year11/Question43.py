from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random
import sympy as sp

class Question43(BaseQuestion):

    def __init__(self):
        self.type = Types.sphere
        self.complexity = Complexity.Moderate
        theList = [1,2,3,4,5,6]
        r_a = random.sample(theList,1)[0]
        r_b = random.sample(theList,1)[0]
        r_c = random.sample(theList,1)[0]
        v_a = sp.nsimplify((4/3)*r_a**3)
        v_b = sp.nsimplify((4/3)*r_b**3)
        self.q = f"Volume of the sphere A, $V_A$=$({{{v_a}}})\pi$ $cm^3$, volume of the sphere B, $V_B$=${{{v_b}}}\pi$ $cm^3$."\
                 f"The ratio of the radius of the sphere B to the sphere C is {r_b}:{r_c}, Find the ratio of surface area A to C"

        s_a = 4*r_a**2
        s_b = 4*r_b**2
        self.res= f"{sp.nsimplify(s_a/s_b)}"

    def question(self):
        return ""

    def graphic(self):
        return self.encode_graphics(self.q,  14)

    def answer(self):
        return ""

    def answer_graphic(self):
        return self.encode_graphics(self.res, 15)
