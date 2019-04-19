import random
from .utils.Utility import get_two_distinct
from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity
from django.template import Template

class Question54(BaseQuestion):
    def __init__(self):
        self.type = Types.Equation_Second_order_one_unknown
        self.complexity = Complexity.Advanced
        self.coef1,self.coef2 = get_two_distinct([2,3,4,5])
        self.var1 = random.choice(['x','y','z'])
        self.num1 = random.choice([2,3,4,5])
        self.asked = self.coef1*self.num1*self.num1 + self.coef2*self.num1*self.num1

    def question(self):
        return "Given "

    def graphic(self):
        a = r'{coef1}${var1}^2$ + {coef2}${var1}^2$ = {asked}, What is {var1} ?'\
            .format(var1=self.var1,asked=self.asked,coef1=self.coef1,coef2=self.coef2)
        return self.encode_graphics(a)

    def answer(self):
        return "{res}".format(res=self.num1)

    def template(self):
        return Template("{{ text }}<div class=\"qi\"><img src=\"data:image/png;base64,{{graphic}}\"></div>")