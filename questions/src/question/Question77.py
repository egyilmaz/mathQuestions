from .BaseQuestion import BaseQuestion
from .Types import Types, Complexity
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from .utils.Utility import get_n_distinct


class Question77(BaseQuestion):
    def __init__(self):
        self.type = Types.chart
        self.complexity = Complexity.Moderate
        scores = [20, 40, 60, 80, 100, 120]
        self.scores_boys = get_n_distinct(scores, 4)
        self.scores_girls = get_n_distinct(scores, 4)
        self.body = "Looking at the given chart of scores per courses, what is the average of girls scores in all courses?"
        self.res = sum(self.scores_girls)/4.0

    def question(self):
        return self.body

    def answer(self):
        return "{res}".format(res=self.res)

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
        ax.set_xticklabels(('Maths', 'Science', 'Reading', 'Writing'))
        ax.legend()
        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )

