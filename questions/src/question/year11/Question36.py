from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random
from sympy import nsimplify

class Question36(BaseQuestion):

    def __init__(self):
        self.type = Types.tap_tank
        self.complexity = Complexity.Moderate
        arr = [2,3,4,5,6]
        random.shuffle(arr)
        taps = arr[0]
        tanks = arr[1]
        hours = arr[2]
        qtaps = arr[4]
        self.q=f"If its taking {hours} hours for {taps} taps to fill {tanks} tanks. How long will it take to fill in {tanks} tanks with {qtaps} taps? Assuming tanks and taps are all of same capacity"
        self.res = f"It will take {(taps*hours/qtaps)}hours"

    def question(self):
        return ""

    def graphic(self):
        return self.encode_graphics(self.q, 10)

    def answer(self):
        return ""

    def answer_graphic(self):
        return self.encode_graphics(self.res, 15)
