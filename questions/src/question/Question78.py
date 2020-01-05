from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity
from fractions import Fraction
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from .utils.Utility import get_n_distinct


class Question78(BaseQuestion):
    def __init__(self):
        self.type = Types.Chart
        self.complexity = Complexity.Moderate
        scores = [20, 25, 30, 35, 40, 45, 50, 55, 60, 70, 80, 90, 100]
        self.scores_boys = get_n_distinct(scores, 4)
        self.scores_girls = get_n_distinct(scores, 4)
        self.courses=('Maths', 'Science', 'Reading', 'Writing')
        self.body = "Looking at the given chart of scores per courses, what is the ratio of total scores of girls over boys?"
        self.res = Fraction(sum(self.scores_girls), sum(self.scores_boys))

    def question(self):
        return self.body

    def answer_graphic(self):
        a = r'$\dfrac{{{0}}}{{{1}}}$ '.format(self.res.numerator,self.res.denominator)
        return self.encode_graphics(a)

    def graphic(self):
        fig, ax = plt.subplots()
        plt.gcf().set_size_inches(4, 4)
        index = np.arange(4)
        bar_width = 0.3
        opacity = 0.4
        ax.bar(index, self.scores_boys, bar_width,
                        alpha=opacity, color='b',
                        label='Boys')
        ax.bar(index + bar_width, self.scores_girls, bar_width,
                        alpha=opacity, color='r',
                        label='Girls')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(self.courses)
        ax.legend()
        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )

