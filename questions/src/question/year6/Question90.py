from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.Types import Types, Complexity
from questions.src.question.utils.Utility import get_n_distinct

def angle_identifier( angle ):
    if angle < 90: return "Acute"
    elif angle==90: return "Right"
    elif angle<180: return "Obtuse"
    elif angle==180: return "Straight"
    elif angle<360: return "Reflex"
    else: return "Full"


class Question90(BaseQuestion):
    def __init__(self):
        self.type = Types.Geometry_angle
        self.complexity = Complexity.Basic
        pool = [1, 10, 20, 25, 30, 35, 40, 45, 50, 55, 60, 70, 80, 90, 100, 110, 115, 120, 125, 130, 145, 175, 179, 180,
                200, 250, 270, 300, 330, 360]
        angles = get_n_distinct(pool, 4)
        self.body = "Identify the angle types {0} (acute, right, obtuse, straight, reflex, full)?".format(angles)
        self.res = [angle_identifier(a) for a in angles]

    def question(self):
        return self.body

    def answer(self):
        return ", ".join(self.res)
