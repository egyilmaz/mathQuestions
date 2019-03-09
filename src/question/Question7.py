import random
from question.Types import Types
from resources.Resource import slow_vehicles, slow_speeds, duration
from utils.Utility import ask_interactive_1arg


class Question7:
    def __init__(self):
        self.type = Types.FIRST_ORDER_1_UNKNOWN
        self.vehicle = random.choice(slow_vehicles)
        self.speed = random.choice(slow_speeds)
        self.duration = random.choice(duration)
        self.distance = self.speed * self.duration
        self.body = "It takes {dur} hours for a {veh} to travel a distance of {dist} miles."\
                    " What is the speed of this {veh}".format(veh=self.vehicle, dist=self.distance, dur=self.duration)

    def question(self):
        return self.body

    def ask_user(self):
        return self.speed == ask_interactive_1arg(self.question())

    def result(self):
        return {self.vehicle: self.speed}

    def answer(self):
        return "{veh} is travelling at {spd}mph".format(veh=self.vehicle, spd=self.speed)
