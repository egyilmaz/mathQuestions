import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_two_distinct
from questions.src.question.Types import Types, Complexity


class Question82(BaseQuestion):
    def __init__(self):
        self.type = [Types.Money_exchange_rate, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        self.source, self.target = get_two_distinct(['GBP','USD','Euro','TL','Rupee','Yuan','Won'])
        self.money = random.choice([20,40,50,100,200,1000,2000])
        self.exrate = random.choice([7.8,2.4,4.5,6.7])
        self.res = self.money*self.exrate

    def question(self):
        return "Exchange rate is given as, 1{0} = {2}{1}. If we have {3} {0}, How much does it make in {1} "\
            .format(self.source,self.target,self.exrate,self.money)

    def answer(self):
        return "We will have {0}{1}".format(self.res,self.target)