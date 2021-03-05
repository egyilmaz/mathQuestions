from questions.src.question.BaseQuestion import BaseQuestion
import random
from questions.src.question.year6.Types import Types, Complexity


class Question80(BaseQuestion):
    def __init__(self):
        self.type = Types.Fraction_compare
        self.complexity = Complexity.Moderate
        self.seq = random.choice([[0.1,0.2,0.3,0.4,0.5],
                                [0.02,0.04,0.06,0.08,0.1],
                                [0.002,0.008,0.014,0.020,0.026],
                                [0.1,0.4,0.7,1.0,1.3],
                                [0.01,0.04,0.09,0.16,0.25],
                                [0.3,0.6,0.9,1,2,1.5],
                                [0.001, 0.002, 0.003, 0.004,0.005],
                                [1.1,2.2,3.3,4.4,5.5],
                                [1.03,1.05,1.07,1.09,1.11],
                                [101.101,102.103,103.105,104.107,105.109],
                                [10.01,12.02,14.03,16.04,18.05],
                                [1.0,0.1,0.01,0.001,0.0001],
                                [1.0,0.9,0.8,0.7,0.6]])

        self.index=random.choice(range(0,5))
        self.seq = [ str(i) for i in self.seq ]
        self.res = self.seq[self.index]
        self.seq[self.index] = 'X'

    def question(self):
        return "Given the sequence ["+' , '.join(self.seq)+"] find the value of X"

    def answer(self):
        return "X is {0}".format(self.res)