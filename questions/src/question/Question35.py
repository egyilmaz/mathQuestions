from .BaseQuestion import BaseQuestion
from .resources.Resource import boys
import random

class Question35(BaseQuestion):
    def __init__(self):
        self.subj = random.choice(boys)
        self.tax = random.choice([10,20,25])
        self.salary = random.choice([200,400,600,800])
        self.body = "{0} is earning {1} pounds from his part time job. He needs to pay {2}% tax. How much money is he left with after tax?".format(self.subj, self.salary, self.tax)
        net_income = self.salary *(1 - self.tax/100)
        self.res = "Net income is {0}".format(net_income)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
