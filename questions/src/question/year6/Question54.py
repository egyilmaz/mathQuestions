import random
import matplotlib.pyplot as plt
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.year6.Types import Types, Complexity
from django.template import Template

class Question54(BaseQuestion):
    def __init__(self):
        self.type = Types.Geometry_circle_perimeter
        self.complexity = Complexity.Moderate
        self.radius = random.choice(range(3,10))
        self.res = 2 * 3.0 * self.radius

    def question(self):
        return "Given the circle below, What is its perimeter?  "

    def draw_graphic(self):
        a = r'(P = $2 \pi r$, where $\pi$ is 3.0)'
        return self.encode_graphics(a)

    def draw_circle(self):
        circle = plt.Circle((0.5, 0.5), radius=0.5, fill=False, fc='w', lw=1, edgecolor='black')
        plt.plot([0.5,1.0],[0.5,0.5],color='black')
        rad_str = "r={0}\"".format(self.radius)
        plt.text(0.5,0.6,rad_str,size=8)
        plt.gcf().set_size_inches(1,1)
        return self.draw_shape( circle )

    def answer(self):
        return "Perimeter is {0}".format(self.res)

    def context(self):
        question=self.question()
        circle = self.draw_circle()
        graphic = self.draw_graphic()
        answer = self.answer()
        meta = self.meta()
        return {'text':question,'circle':circle,'graphic':graphic,'answer':answer,'meta':meta}

    def template(self):
        return Template("{{text}}<div class=\"qi\"><img src=\"data:image/png;base64,{{graphic}}\"></div>"\
                            "<br><div class=\"qi\"><img src=\"data:image/png;base64,{{circle}}\"></div>"\
                        + self.std_input_answer_template_str())