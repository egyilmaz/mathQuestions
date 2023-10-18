from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random

class Question37(BaseQuestion):

    def __init__(self):
        self.type = Types.tap_tank
        self.complexity = Complexity.Complex
        arr = [2,3,4,5,6]
        random.shuffle(arr)
        taps = arr[0]
        tanks = arr[1]
        hours = arr[2]
        qtanks = arr[3]
        qtaps = arr[4]
        self.q=f"Assuming tanks and taps are all of same capacity, If its taking {hours} hours for {taps} taps to fill {tanks} tanks. How long will it take to fill in {qtanks} tanks with {qtaps} taps?"
        self.res = f"It will take {(qtanks/tanks)*(taps*hours/qtaps)}hours"

    def question(self):
        return ""

    def graphic(self):
        return self.encode_graphics(self.q, 10)

    def answer(self):
        return ""

    def answer_graphic(self):
        return self.encode_graphics(self.res, 15)
