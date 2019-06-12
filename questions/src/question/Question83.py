import random
from .utils.Utility import get_two_distinct
from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity


class Question83(BaseQuestion):
    def __init__(self):
        self.type = Types.General_Problem
        self.complexity = Complexity.Basic
        self.source, self.forex = get_two_distinct(['GBP','USD','Euro','TL','Rupee','Yuan','Won'])
        self.perkm = random.choice([2.3, 3.5, 4.2, 1.8, 0.9, 1.3])
        self.km = random.choice([4,5,6,7,8,9,10,13,14,15,16,17,18,20,30,40])
        self.res = self.perkm*self.km

    def question(self):
        return "Taxi is charging {0} {1} per km. If it takes {2} km from home to work. How much does it cost?"\
            .format(self.perkm,self.forex,self.km)

    def answer(self):
        return "It costs {0}".format(self.res)