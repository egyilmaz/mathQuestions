from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random
import sympy as sym

class Question3(BaseQuestion):
    vals = [[2,10,1,80,1,18],[1, 100,2, 18,3,27],[2,3,3,2,3,8],[1,48,1,24,1,49],[1,25,1,16,2,9]]

    def __init__(self):
        self.type = Types.surds
        self.complexity = Complexity.Moderate
        index = random.randint(0, len(Question3.vals)-1)
        mul = random.randint(1, 3)
        val = Question3.vals[index]
        val = [mul*x for x in val]
        sol = val[0]*sym.sqrt(val[1]) * val[2]*sym.sqrt(val[3]) * val[4]*sym.sqrt(val[5])
        # remove 1's in coefficients
        coeff = [val[0], val[2], val[4]]
        coeff = [ x if x > 1 else ' ' for x in coeff]
        self.q = r'${c1}\sqrt{{{c2}}}x{c3}\sqrt{{{c4}}}x{c5}\sqrt{{{c6}}}$'.format(c1=coeff[0], c2=val[1], c3=coeff[1], c4=val[3], c5=coeff[2], c6=val[5])
        self.res = r'{r1} or {r2}'.format(r1=sol, r2=sol.evalf())

    def question(self):
        return "Work out  "

    def graphic(self):
        return self.encode_graphics(self.q)

    def answer(self):
        return "{res}".format(res=self.res)

