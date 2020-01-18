import random
from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity
import numpy as np


class Question136(BaseQuestion):
    def __init__(self):
        self.type = [Types.General_Problem, Types.sat_reasoning]
        self.complexity = Complexity.Advanced
        total = random.choice([60, 90, 120, 180])
        subset = random.sample([8, 10, 11, 12, 13, 15, 20], 3)
        last = total - np.sum(subset)
        subset.append(last)
        self.body = "Given {0} as the number of 4 cake types sold in a week. When drawn as a pie chart, what will be" \
                    " the degrees representing each sales figure on the chart".format(subset)
        percents = [round(360.0/total,2)*i for i in subset]
        self.res="Results in degrees {0}".format(percents)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
