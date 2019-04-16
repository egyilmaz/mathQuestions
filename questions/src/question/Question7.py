import random
from .BaseQuestion import BaseQuestion
from .resources.Resource import slow_vehicles, slow_speeds, duration
from .Types import Types, Complexity


class Question7(BaseQuestion):
    def __init__(self):
        self.type = Types.Vehicle_speed_time_distance
        self.complexity = Complexity.Moderate
        self.vehicle = random.choice(slow_vehicles)
        self.speed = random.choice(slow_speeds)
        self.duration = random.choice(duration)
        self.distance = self.speed * self.duration
        self.body = "It takes {dur} hours for a {veh} to travel a distance of {dist} miles."\
                    " What is the speed of this {veh}".format(veh=self.vehicle, dist=self.distance, dur=self.duration)

    def question(self):
        return self.body

    def answer(self):
        return "{veh} is travelling at {spd}mph".format(veh=self.vehicle, spd=self.speed)
