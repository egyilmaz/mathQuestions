import random
from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity


class Question119(BaseQuestion):
    def __init__(self):
        self.type = [Types.Problem_solving, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        running = random.choice([10,20,30,40])
        cycling = random.choice([2,3,4,5])
        swim_index = random.choice([1,2,3])
        wording={}
        wording[1]="quarter"
        wording[2]="half"
        wording[3]="three quarters"
        self.body = "A triathlon consists of running, cycling, swimming. Running part is {0}km, cycling takes {1} " \
                    "times the length of running and swimming is {2} of cycling. What will be the individual " \
                    "challenge's percentage in this race"\
            .format(running, cycling, wording[swim_index])
        total = running + cycling*running + cycling*running*swim_index*0.25
        res1 = 100*running/total
        res2 = 100*cycling*running/total
        res3 = 100*cycling*running*swim_index*0.25/total
        self.res = "Running is {0}% Cycling is {1}% Swimming is {2}%".format(round(res1),round(res2),round(res3))

    def question(self):
        return self.body

    def answer(self):
        return self.res
