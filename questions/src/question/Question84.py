import random
from .BaseQuestion import BaseQuestion
from .utils.Utility import get_two_distinct
from .Types import Types, Complexity


class Question84(BaseQuestion):
    def __init__(self):
        self.type = Types.General_Problem
        self.complexity = Complexity.Advanced
        self.source, self.target = get_two_distinct(['GBP', 'USD', 'Euro', 'TL', 'Rupee', 'Yuan', 'Won'])
        self.perkm = random.choice([2.3, 3.5, 4.2, 1.8, 0.9, 1.3])
        self.exrate = random.choice([1.2, 1.3, 1.4, 2.3, 2.4, 3.3, 3.4])
        self.km = random.choice([4,5,6,7,8,9,10,13,14,15,16,17,18,20,30,40])
        self.res = self.perkm*self.km*self.exrate

    def question(self):
        return "Taxi is charging {0}{1} per km. If it takes {2} km from home to work. How much does it cost in {3}, " \
               "where exchange rate is 1{1}={4}{3}?"\
            .format(self.perkm,self.source,self.km,self.target,self.exrate)

    def answer(self):
        return "It costs {0}".format(self.res)