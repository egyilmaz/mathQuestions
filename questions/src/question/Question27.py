import random
from .BaseQuestion import BaseQuestion
from fractions import Fraction
from decimal import Decimal
from .Types import Types
from ..resources.Resource import random_fractions
from ..utils.Utility import ask_interactive_1arg, get_two_distinct, descending

class Question27(BaseQuestion):
    def __init__(self):
        self.pool = [Fraction(1,2),Fraction(1/4),Fraction(3/4), Fraction(1,10),Fraction(2,5),Fraction(3,5),Fraction(4,5),Fraction(5,5)]
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.first, self.second = get_two_distinct( self.pool )
        self.res = [str(self.first*100)+"%", str(self.second*100)+"%"] 
        self.body = "Represent  "

    def question(self):
        return self.body

    def graphic(self):
        a = r'$\dfrac{{{0}}}{{{1}}}$  and  $\dfrac{{{2}}}{{{3}}}$ as percentages'.format(self.first.numerator,self.first.denominator,self.second.numerator,self.second.denominator)
        return self.encode_graphics(a)


    def ask_user(self):
        return self.val == ask_interactive_1arg(self.question())

    def result(self):
        return {self.res: str(self.res)}

    def answer(self):
        return "{res}".format(res=self.res)
