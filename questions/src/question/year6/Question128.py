import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year6.Types import Types, Complexity


class Question128(BaseQuestion):
    def __init__(self):
        self.type = [Types.Problem_solving, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        times=random.choice([2,3,4,5])
        add=random.choice([3,5,7,10])
        start=random.choice([10,15,20,25])
        seq=[]
        current=start
        for i in range(1,5):
            seq.append(current)
            current = current*times + add

        res1,res2 = seq[0],seq[3]
        seq[0]="?"
        seq[3]="?"
        self.body = "Given the rule ' Multiply by {0}, then add {1}', what is the missing " \
                    "numbers in {2}?".format(times,add,seq)
        self.res="{0} and {1}".format(res1,res2)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
