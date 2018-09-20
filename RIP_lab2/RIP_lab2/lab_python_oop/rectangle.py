from lab_python_oop.figure import Figure
from lab_python_oop.color import Color


class Rectangle(Figure):
    def __init__(self, name, x, y, color):
        self.name = name
        self.x = x
        self.y = y
        self.color = Color(color)

    def area(self):
        return self.x * self.y

    def name(self):
        return self.name

    def __repr__(self):
        return '{} {} {} {} {}'.format(self.name, self.x, self.y, self.color.c, self.area())
