from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random

class Question45(BaseQuestion):

    def __init__(self):
        self.type = Types.function
        self.complexity = Complexity.Moderate
        f=random.sample(['f','t','p'],1)[0]
        g=random.sample(['g','k','q'],1)[0]
        a=random.sample([2,3,4],1)[0]
        b=random.sample([-2,-1,1,2],1)[0]
        c=random.sample([2,3,4],1)[0]
        d=random.sample([-2,-1,1,2],1)[0]
        x =random.sample([-2,-1,0,1,2,3,4],1)[0]
        e = (c*(a*x+b) + d)**2
        first = (a**2)*(c**2)
        second = 2*c*a*(c*b+d)
        third = (c*b+d)**2
        if second > 0:
            second = '+'+str(second)
        if b > 0:
            b = '+'+str(b)
        if d > 0:
            d = '+'+str(d)
        self.q = f"If {g}(x) = {a}x{b} and {f}(x) = $({{{c}}}x {{{d}}})^2$, write down {f}{g}(x) and then find the x when {f}{g}(x) = {e}"
        self.res= f"{f}{g}(x) = ${{{first}}}x^2$ {second}x + {third}  if {f}{g}(x)={e} then x={x}"

    def question(self):
        return ""

    def graphic(self):
        return self.encode_graphics(self.q,  14)

    def answer(self):
        return ""

    def answer_graphic(self):
        return self.encode_graphics(self.res, 15)
