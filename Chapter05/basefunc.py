from __future__ import division


class Rect:
    def __init__(self):
        self.l = 8
        self.b = 5

    def area(self):
        return self.l * self.b


class Triangle:
    def __init__(self):
        self.x = 17
        self.y = 13

    def area(self):
        return 1/2 * self.x * self.y


class Both(Rect, Triangle):
    pass


r = Both()
print("Area of a rectangle is", r.area())
