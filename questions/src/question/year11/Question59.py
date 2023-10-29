from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random
import sympy as sp

class Question59(BaseQuestion):

    def __init__(self):
        self.type = Types.probability
        self.complexity = Complexity.Moderate
        [b1,b2]=random.sample(['red','green','blue','white','black'],2)
        (a,b)=random.sample([(5,10),(10,15),(6,7),(4,5),(10,12),(8,10)],1)[0]
        t = a+b
        eqn1 = sp.nsimplify((a/t)*(a-1)/(t-1))
        eqn2 = sp.nsimplify((b/t)*(b-1)/(t-1))

        self.q = f"Inside a drawer, there are {a} {b1} and {b} {b2} balls. If we draw two balls at random, What is the probability of both balls being {b1} and {b2}?"
        self.res = f'Probability of both balls being {b1} is {eqn1}, and both balls being {b2} is {eqn2}'

    def question(self):
        return f"{self.q}"

    def answer(self):
        return f"{self.res}"

