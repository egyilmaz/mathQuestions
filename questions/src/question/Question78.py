from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from .utils.Utility import get_n_distinct


class Question78(BaseQuestion):
    def __init__(self):
        self.type = Types.chart
        self.complexity = Complexity.Moderate
        scores = [20, 25, 30, 35, 40, 45, 50, 55]
        self.scores_boys = get_n_distinct(scores, 4)
        self.scores_girls = get_n_distinct(scores, 4)
        self.courses=('Maths', 'Science', 'Reading', 'Writing')
        self.body = "Looking at the given chart of scores per courses, what is the ratio of girls over boys for Science and Writing?"

    def question(self):
        return self.body

    def answer_graphic(self):
        a = r'$\dfrac{{{0}}}{{{1}}}$  and  $\dfrac{{{2}}}{{{3}}}$ '.format(self.scores_girls[1],
                                                                                  self.scores_boys[1],
                                                                                  self.scores_girls[3],
                                                                                  self.scores_boys[3])
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

