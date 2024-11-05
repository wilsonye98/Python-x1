# Define a class named Circle which can be constructed by a radius.
# The Circle class has a method which can compute the area.

from math import pi

class Circle:
    def __init__(self, r):
        self.radius = r

    def radius(self):
        return pi * self.radius ** 2

