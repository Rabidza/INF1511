from __future__ import division


class Rect:
    def __init__(self):
        self.l = 8
        self.b = 5

    def area(self):
        print("Area of rectangle is", self.l * self.b)


class Triangle(Rect):
    def __init__(self):
        Rect.__init__(self)
        self.x = 17
        self.y = 13

    def area(self):
        Rect.area(self)
        print("Area of a triangle is", 1/2 * self.x * self.y)


r = Triangle()
r.area()
