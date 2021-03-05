from questions.src.question.utils.Utility import get_two_distinct
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.Types import Types, Complexity

class Question50(BaseQuestion):
    def __init__(self):
        self.type = Types.Equation_First_order_two_unknown
        self.complexity = Complexity.Basic
        self.var1,self.var2 = get_two_distinct(['x','y','z'])
        self.coef1,self.coef2 = get_two_distinct([2,3,4,5])
        self.num1,self.num2 = get_two_distinct([2,3,4,5,6,7,8,9,10])
        self.res = self.coef1*self.num1 + self.coef2*self.num2

    def question(self):
        return "Given {var1}={num1}, {var2}={num2}. What is {coef1}{var1} + {coef2}{var2}?"\
                .format(var1=self.var1,num1=self.num1,var2=self.var2,num2=self.num2,coef1=self.coef1,coef2=self.coef2)

    def answer(self):
        return "{res}".format(res=self.res)
