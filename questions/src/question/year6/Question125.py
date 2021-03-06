from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year6.Types import Types, Complexity
import random
import matplotlib.pyplot as plt
from io import BytesIO


class Question125(BaseQuestion):
    def __init__(self):
        self.type = [Types.Geometry_translation, Types.sat_reasoning]
        self.complexity = Complexity.Moderate
        self.x=random.choice([1,2,3,4])
        self.y=random.choice([2,3,4,5])
        trans_x= random.choice([4,5,6])
        trans_y= random.choice([6,7,8])
        self.body = "Given a coordinate, A({0},{1}), What will be the new coordinates after translating this point " \
                    "by {2} units to the right and {3} units upwards?".format(self.x,self.y,trans_x, trans_y)

        self.resx,self.resy=self.x+trans_x, self.y+trans_y
    def question(self):
        return self.body

    def answer(self):
        return "New coordinate will be A({0},{1})".format(self.resx, self.resy)


    def graphic(self):
        plt.axis('equal')
        plt.gcf().set_size_inches(4, 4)
        lim = max(self.x,self.y)
        plt.xlim(0,2*lim)
        plt.ylim(0,2*lim)
        plt.xticks(range(1,2*lim))
        plt.yticks(range(1,2*lim))
        plt.grid(True)
        label = "A({0},{1})".format(self.x,self.y)
        plt.text(0.9*self.x, 0.8*self.y, label)
        plt.scatter([self.x], [self.y], s=[15])
        buf = BytesIO()
        plt.savefig(buf, format='PNG')
        return self.toBuffer( buf )

