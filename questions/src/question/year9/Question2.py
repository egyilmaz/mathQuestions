from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_unsorted_n_distinct, get_two_distinct
from questions.src.question.year9.Types import Types, Complexity
from itertools import chain
import random
from sympy import Eq, solve
from sympy.abc import x, y

def add_plus_sign(arr):
    res=[]
    for i in arr[0:]:
        res.append(str(i) if i < 0 else f"+{i}")
    return res

class Question2(BaseQuestion):
    # ax + by = c
    # dx + ey = f
    #(a,b,c,d,e,f)
    coeff = [[5,6,3,2,-3,12], [2,3,12,4,3,18],[-2,1,0,1,1,6],[1,1,78,1,-1,38],[-3,1,1,4,2,8]]
    result = [(3, -2),(3, 2),(2, 4),(58, 20),(3, 10)]

    def __init__(self):
        self.type = Types.simultan_eqn
        self.complexity = Complexity.Moderate
        index = random.randint(0, len(Question2.coeff)-1)
        mul = random.randint(2, 4)
        arr = [ mul*x for x in Question2.coeff[index]]
        
        sol = solve([ Eq(arr[0]*x + arr[1]*y, arr[2]),
                      Eq(arr[3]*x + arr[4]*y, arr[5])])
        sol_alt = { s:sol[s].evalf() for s in sol }
        cr = add_plus_sign([arr[1],arr[4]])
        # adding + for positive values for representation, keeping them separate from their actual value above.
        # note we are using first coefficient as is, regardless of its sign, only the positives are marked with + after first one
        self.q = r'${c1}x {c2}y = {c3}$'.format(c1=arr[0], c2=cr[0], c3=arr[2])
        self.q += "\n"
        self.q += r'${c1}x {c2}y = {c3}$'.format(c1=arr[3], c2=cr[1], c3=arr[5])
        self.res = r'{r1}, {r2}'.format(r1=sol, r2=sol_alt)

    def question(self):
        return "Solve the given simultaneous eqn "

    def graphic(self):
        return self.encode_graphics(self.q)

    def answer(self):
        return "{res}".format(res=self.res)

