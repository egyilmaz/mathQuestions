import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.Types import Types, Complexity


class Question109(BaseQuestion):
    def __init__(self):
        self.type = [Types.Ratio, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        onMap = random.choice([12, 15, 25, 50, 55, 125])
        result = random.choice([13,14,15,16,17,18,19])
        realDist = result * onMap
        self.body = "Each inch on a map corresponds to {0} miles in real life. If the distance" \
                    " between two mountain peeks is {1} miles, How many inches does that make on the map?"\
            .format(onMap,realDist)

        self.res="{0}".format(result)

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
