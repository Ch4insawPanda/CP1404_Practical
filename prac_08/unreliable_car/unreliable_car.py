from prac_08.Taxi.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Specialized version of Superclass object Car that includes a degree or reliability."""
        super().__init__( name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Generate a random float between 1-100 and drive 0 if reliability is less."""
        if self.reliability < random.randint(1, 100):
            distance = 0
        else:
            distance = super().drive(distance)
        return distance
