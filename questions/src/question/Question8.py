import random
from .BaseQuestion import BaseQuestion
from .Types import Types
from ..resources.Resource import slow_vehicles, slow_speeds, duration
from ..utils.Utility import ask_interactive_1arg


class Question8(BaseQuestion):
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.vehicle = random.choice(slow_vehicles)
        self.speed = random.choice(slow_speeds)
        self.duration = random.choice(duration)
        self.distance = self.speed * self.duration
        self.body = "How long does it take to travel {dist} miles for a {veh} with a speed of {spd}mph"\
            .format(veh=self.vehicle, dist=self.distance, spd=self.speed)

    def question(self):
        return self.body

    def ask_user(self):
        return self.duration == ask_interactive_1arg(self.question())

    def result(self):
        return {self.vehicle: self.duration}

    def answer(self):
        return "It takes {dur} hours".format(dur=self.duration)
