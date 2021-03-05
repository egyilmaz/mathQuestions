from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_two_distinct
from questions.src.question.year6.Types import Types, Complexity


class Question30(BaseQuestion):
    def __init__(self):
        self.type = Types.Percentage
        self.complexity = Complexity.Moderate
        self.first, self.second = get_two_distinct([1,2,3,4,5,10,20,25,30,40,50,60,75,90,100])
        self.res = "{0}%,{1}%".format(str(self.first), str(self.second))
        self.body = "Represent {0} and {1} as percentages".format(float(self.first/100), float(self.second/100))

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)
