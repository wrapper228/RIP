class Color:
    def __init__(self, color):
        self.color = color

    def getc(self):
        return self.color

    c = property(getc)
