import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.utils.Utility import get_n_distinct
from questions.src.question.year6.Types import Types, Complexity


class Question88(BaseQuestion):
    def __init__(self):
        self.type = Types.Percentage
        self.complexity = Complexity.Moderate
        self.percentages = get_n_distinct([2.5,3.5,4.5,5.5,6.5,10.5,15.5,24.5,32.5,45.5],3)
        self.languages = get_n_distinct(["German","Turkish","Mandarin","Spanish","Arabic","Urdu","Hindu"],3)
        self.population = random.choice([200,400,600,800,1000])
        self.spoken = [(self.population/100)*per for per in self.percentages]
        self.body = "In a school with {pop} students".format(pop=self.population)
        c=0
        for p in self.spoken:
            self.body += ", {many} speaks {lang}".format(many=p, lang=self.languages[c])
            c += 1
        self.body += ". What are the percentages of these students speaking these languages?"

    def question(self):
        return self.body

    def answer(self):
        return "{0}".format(self.percentages)
