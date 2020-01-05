import random
from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity
import numpy as np


class Question116(BaseQuestion):
    def __init__(self):
        self.type = [Types.General_Problem, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        arr = np.random.randint(10, size=random.choice([5,6,7,8]))
        wording = random.choice(['mean','average'])
        self.body = "Find the {0} of {1}?".format(wording, arr)

        self.res = "Answer is {0}".format(np.mean(arr))

    def question(self):
        return self.body

    def answer(self):
        return self.res
