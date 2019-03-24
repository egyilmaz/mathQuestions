import random
from .BaseQuestion import BaseQuestion
from .Types import Types
from ..resources.Resource import boys, items, simple_fractions
from ..utils.Utility import ask_interactive_1arg, get_two_distinct
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (5,1)
from io import BytesIO
import base64


class Question22(BaseQuestion):
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.subject = random.choice(boys)
        self.ratio1, self.ratio2 = get_two_distinct(simple_fractions)
        self.int1, self.int2 = get_two_distinct(range(1,7))
        self.res = self.ratio1 + self.ratio2

    def question(self):
        return ""

    def graphic(self):
        plt.axis('off')
        a = r'What is  ${0} \dfrac{{{1}}}{{{2}}} + {3}\dfrac{{{4}}}{{{5}}}$ = ?'.format(self.int1,self.ratio1.numerator,self.ratio1.denominator,self.int2,self.ratio2.numerator,self.ratio2.denominator)
        plt.text(-1, 1, a, fontsize=12)
        buf = BytesIO()
        plt.savefig(buf, format='PNG', bbox_inches='tight', pad_inches=0)
        graphic = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n','')
        plt.clf()
        buf.close()
        return graphic

    def ask_user(self):
        return self.res == ask_interactive_1arg(self.question())

    def result(self):
        return {self.subject: self.res}

    def answer(self):
        return "{res}".format(res=self.res)
