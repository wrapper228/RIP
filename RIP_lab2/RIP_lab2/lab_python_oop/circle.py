from lab_python_oop.figure import Figure
from lab_python_oop.color import Color
from math import pi


class Circle(Figure):
    def __init__(self, name, r, color):
        self.name = name
        self.r = r
        self.color = Color(color)

    def area(self):
        return pi * self.r * self.r

    def name(self):
        return self.name

    def __repr__(self):
        return '{} {} {} {}'.format(self.name, self.r, self.color.c, self.area())
