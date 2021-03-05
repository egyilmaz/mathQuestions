from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_n_distinct
from questions.src.question.year6.Types import Types, Complexity


class Question93(BaseQuestion):
    def __init__(self):
        self.type = Types.Percentage
        self.complexity = Complexity.Advanced
        self.male,self.female = get_n_distinct([30,40,50,60,70,80,90],2)
        self.body = "In a school, there are {0} female and {1} male students. What percentage of school pupils are male and female.".format(self.female,self.male)
        total = self.male + self.female
        self.resm,self.resf = (self.male*100.0)/total, (self.female*100.0)/total

    def question(self):
        return self.body

    def answer(self):
        return "Female {0} Male {1}".format(self.resf,self.resm)