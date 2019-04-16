import random
from .BaseQuestion import BaseQuestion
from .resources.Resource import fast_vehicles, fast_speeds, duration, subjects
from .utils.Utility import get_two_distinct
from .Types import Types, Complexity


class Question9(BaseQuestion):
    def __init__(self):
        self.type = Types.Vehicle_speed_time_distance
        self.complexity = Complexity.Moderate
        self.passenger = random.choice(subjects)
        self.vehicle1, self.vehicle2 = get_two_distinct(fast_vehicles)
        self.speed1, self.speed2 = get_two_distinct(fast_speeds)
        self.duration1, self.duration2 = get_two_distinct(duration)
        self.distance = self.speed1 * self.duration1 + self.speed2 * self.duration2
        self.body = "{pas} uses a {veh1} for {dur1} hours than uses a {veh2} for {dur2} hours to travel. The {veh1}'s" \
                    " speed is {spd1}mph and {veh2}'s speed is {spd2}mph. What is the total distance travelled"\
            .format(pas=self.passenger, veh1=self.vehicle1, veh2=self.vehicle2, spd1=self.speed1, spd2=self.speed2
                    , dur1=self.duration1, dur2=self.duration2)

    def question(self):
        return self.body

    def answer(self):
        return "Total journey is {dist} miles".format(dist=self.distance)
