from .BaseQuestion import BaseQuestion
from fractions import Fraction
from .utils.Utility import get_two_distinct
from .Types import Types, Complexity
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from matplotlib.ticker import MaxNLocator
from collections import namedtuple

class Question76(BaseQuestion):
    def __init__(self):
        self.type = Types.Fraction_decimal
        self.complexity = Complexity.Advanced
        self.pool = [Fraction(8,125),Fraction(1,8),Fraction(3,8),Fraction(7,8),Fraction(4,250),Fraction(1,500), Fraction(7,2),Fraction(48,25),Fraction(123,125),Fraction(45,25),Fraction(123,5)]
        self.first, self.second = get_two_distinct( self.pool )
        self.res = "{0}, {1}".format(float(self.first), float(self.second))
        self.body = "Represent  "

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)

    def graphic(self):
        n_groups = 5

        means_men = (20, 35, 30, 35, 27)
        std_men = (2, 3, 4, 1, 2)

        means_women = (25, 32, 34, 20, 25)
        std_women = (3, 5, 2, 3, 3)

        fig, ax = plt.subplots()

        index = np.arange(n_groups)
        bar_width = 0.35

        opacity = 0.4
        error_config = {'ecolor': '0.3'}

        rects1 = ax.bar(index, means_men, bar_width,
                        alpha=opacity, color='b',
                        yerr=std_men, error_kw=error_config,
                        label='Men')

        rects2 = ax.bar(index + bar_width, means_women, bar_width,
                        alpha=opacity, color='r',
                        yerr=std_women, error_kw=error_config,
                        label='Women')

        ax.set_xlabel('Group')
        ax.set_ylabel('Scores')
        ax.set_title('Scores by group and gender')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(('A', 'B', 'C', 'D', 'E'))
        ax.legend()

        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )

