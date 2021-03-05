import random
from questions.src.question.BaseQuestion import BaseQuestion
from questions.src.question.resources.Resource import slow_vehicles, slow_speeds, duration
from questions.src.question.year6.Types import Types, Complexity


class Question8(BaseQuestion):
    def __init__(self):
        self.type = Types.Vehicle_speed_time_distance
        self.complexity = Complexity.Moderate
        self.vehicle = random.choice(slow_vehicles)
        self.speed = random.choice(slow_speeds)
        self.duration = random.choice(duration)
        self.distance = self.speed * self.duration
        self.body = "How long does it take to travel {dist} miles for a {veh} with a speed of {spd}mph"\
            .format(veh=self.vehicle, dist=self.distance, spd=self.speed)

    def question(self):
        return self.body

    def answer(self):
        return "It takes {dur} hours".format(dur=self.duration)
