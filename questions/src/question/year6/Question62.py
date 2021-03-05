import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.Types import Types, Complexity
from questions.src.question.resources.Resource import girls


class Question62(BaseQuestion):
    def __init__(self):
        self.type = Types.Percentage
        self.complexity = Complexity.Advanced
        self.subj = random.choice(girls)
        self.tax = random.choice([5,10,15])
        self.room = random.choice([130,140,150,160,170,180])
        self.bill = self.room*(1+self.tax/100.0)
        self.body = "{subj} and her family stayed at a hotel and got a bill of {bill}pounds, which includes {tax}% tax "\
                     "What was the room's rate, before tax?".format(subj=self.subj, bill = self.bill, tax=self.tax)

    def question(self):
        return self.body

    def answer(self):
        return "Room rate before tax was {0}".format(self.room)
