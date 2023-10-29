from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random
import sympy as sp

class Question58(BaseQuestion):

    def __init__(self):
        self.type = Types.probability
        self.complexity = Complexity.Complex
        [b1,b2]=random.sample(['red','green','blue','white','black'],2)
        (a,b,c,d)=random.sample([(2,3,2,5),(3,5,1,2),(2,3,1,2)],1)[0]
        x = sp.symbols('x')
        t = a+b
        eqn = (a/t)*(a*x-1)/(t*x-1) + (b/t)*(b*x-1)/(t*x-1) -(c/d)

        sol = sp.solve(eqn,x)
        self.q = f"Inside a drawer, there are {b1} and {b2} balls with a ratio of {b1}:{b2} as {a}:{b}. If we draw two balls at random, the probability of both balls being same color is {c}/{d}. Find number of {b1} and {b2} balls"
        self.res = f'Number of {b1} balls {a*sol[0]}, {b2} balls {b*sol[0]}'

    def question(self):
        return f"{self.q}"

    def answer(self):
        return f"{self.res}"

