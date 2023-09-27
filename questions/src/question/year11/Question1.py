from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_unsorted_n_distinct, get_two_distinct
from questions.src.question.year11.Types import Types, Complexity
from itertools import chain
from sympy import Eq, solve
from sympy.abc import x, y

def add_plus_sign(arr):
    res=[arr[0]]
    for i in arr[1:]:
        res.append(str(i) if i < 0 else f"+{i}")
    return res

class Question1(BaseQuestion):

    coeff = [i for i in range(-12, 13) if i != 0 or i !=1]

    def __init__(self):
        self.type = Types.simultan_eqn
        self.complexity = Complexity.Advanced
        self.var1, self.var2 = get_two_distinct(['x', 'y', 'z', 't', 'a', 'b', 'c'])
        rc = get_unsorted_n_distinct(Question1.coeff, 6)

        sol = solve([ Eq(rc[0]*x + rc[1]*y, rc[2]),
                      Eq(rc[3]*x + rc[4]*y, rc[5])])
        sol_alt = { s:sol[s].evalf() for s in sol }

        cr = add_plus_sign(rc)
        # adding + for positive values for representation, keeping them separate from their actual value above.
        # note we are using first coefficient as is, regardless of its sign, only the positives are marked with + after first one
        self.q = r'${c1}{v1} {c2}{v2} = {c3}$'.format(c1=cr[0], v1=self.var1, c2=cr[1], v2=self.var2, c3=cr[2])
        self.q += "\n"
        self.q += r'${c1}{v1} {c2}{v2} = {c3}$'.format(c1=cr[3], v1=self.var1, c2=cr[4], v2=self.var2, c3=cr[5])
        self.res = r'{r1}, {r2}'.format(r1=sol, r2=sol_alt)

    def question(self):
        return "Solve the given simultaneous eqn "

    def graphic(self):
        return self.encode_graphics(self.q)

    def answer(self):
        return "{res}".format(res=self.res)

