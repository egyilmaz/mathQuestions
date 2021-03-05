from questions.src.question.utils.Utility import get_two_distinct
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.Types import Types, Complexity

class Question51(BaseQuestion):
    def __init__(self):
        self.type = Types.Equation_Second_order_two_unknown
        self.complexity = Complexity.Basic
        self.var1,self.var2 = get_two_distinct(['x','y','z'])
        self.num1,self.num2 = get_two_distinct([2,3,4,5,6,7,8,9,10])
        self.res = self.num1*self.num1 + +2*self.num1*self.num2 + self.num2*self.num2

    def question(self):
        return "Given {var1}={num1}, {var2}={num2}. What is "\
                .format(var1=self.var1,num1=self.num1,var2=self.var2,num2=self.num2)

    def graphic(self):
        a = r'${var1}^2$ + 2{var1}{var2} + ${var2}^2$ ?'.format(var1=self.var1,var2=self.var2)
        return self.encode_graphics(a)

    def answer(self):
        return "{res}".format(res=self.res)
