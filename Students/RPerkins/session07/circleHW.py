__author__ = 'Robert W. Perkins'

from math import pi


class Circle(object):

    def __init__(self, radius):
        self.radius = float(radius)

    @property
    def diameter(self):
        return self.radius * 2.0

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2.0

    @property
    def area(self):
        return self.radius**2 * pi