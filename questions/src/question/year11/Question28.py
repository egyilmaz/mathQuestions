from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
from sympy import nsimplify
import random

class Question28(BaseQuestion):

    def __init__(self):
        self.type = Types.ratio
        self.complexity = Complexity.Moderate
        names = random.sample(["Joe","Henry","George", "Mary", "Anabel", "Alina", "Aya", "Susan"],3)
        cand = [(3, 4, 5, 6), (2, 3, 4, 5), (3, 4, 5, 7), (4 ,5, 6, 8), (2, 3, 8, 6), (2, 4, 3, 5), (3, 4, 6, 7), (4, 5, 8, 6)]
        a,b,c,d = random.sample(cand,1)[0]
        self.q = f"The ratio of wages for {names[0]} to {names[1]} is {a} : {b}, the ratio of wages for {names[1]} to {names[2]} is {c} : {d}. What will be the wage ratio for {names[2]} to {names[0]}"
        sol =  nsimplify(((d*b) / (c*a)),rational=True)
        self.r = f"The ratio of {names[2]} to {names[0]} is {sol}"

    def question(self):
        return f"{self.q}"

    def answer(self):
        return "Answer: "

    def answer_graphic(self):
        return self.encode_graphics(self.r)


