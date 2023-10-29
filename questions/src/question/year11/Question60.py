from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year11.Types import Types, Complexity
import random
import sympy as sp

class Question60(BaseQuestion):

    def __init__(self):
        self.type = Types.probability
        self.complexity = Complexity.Moderate
        who=random.sample(['Aila','Roger','Frederick','Constantin','Mikey'],1)[0]
        what=random.sample(['hoodie', 'coat', 'pant', 'bag'],1)[0]
        amount=random.sample([1,2,3,4],1)[0]
        price= random.sample([10, 12, 15, 20, 25],1)[0]
        inflation = random.sample([12,23,34,5,16,7, 11, 21],1)[0]
        inflated = round(price*(inflation+100)/100,2)
        plural_what = what
        if amount > 1:
            plural_what = what+"s"
        self.q = f"Last month, {who} bought {amount} {plural_what} for a total of {round(price*amount,2)}. This month, a single {what} costed {inflated} calculate the inflation rate on {what} to 1dp?"
        self.res = f'inflation rate is {round(inflation,1)}'

    def question(self):
        return f"{self.q}"

    def answer(self):
        return f"{self.res}"

