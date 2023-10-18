from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random

class Question5(BaseQuestion):

    def __init__(self):
        self.type = Types.expand
        self.complexity = Complexity.Moderate
        cand = [-6,-5,-4,-3,-2,2,3,4,5,6]
        a = random.sample(cand,1)[0]
        b = random.sample(cand,1)[0]
        c = random.sample(cand,1)[0]
        d = random.sample(cand,1)[0]

        first = b
        if first > 0:
            first = f"+{first}"

        second = d
        if second > 0:
            second = f"+{second}"        

        self.q = f'$({a}x {first})({c}x {second})$'
        self.res = f'${a*c}x^2+{a*d+b*c}x+{b*d}$'

    def question(self):
        return "Expand then simplfy  "

    def graphic(self):
        return self.encode_graphics(self.q)

    def answer(self):
        return "Answer: "

    def answer_graphic(self):
        return self.encode_graphics(self.res)


