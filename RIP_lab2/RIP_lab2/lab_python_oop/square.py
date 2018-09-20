from lab_python_oop.rectangle import Rectangle
from lab_python_oop.color import Color


class Square(Rectangle):
    def __init__(self, name, x, color):
        self.name = name
        self.x = x
        self.color = Color(color)

    def area(self):
        return self.x * self.x

    def name(self):
        return self.name

    def __repr__(self):
        return '{} {} {} {}'.format(self.name, self.x, self.color.c, self.area())
