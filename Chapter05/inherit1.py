from __future__ import division


class Rect:
    def __init__(self):
        self.l = 8
        self.b = 5

    def rectarea(self):
        return self.l * self.b


class Triangle(Rect):
    def __init__(self):
        Rect.__init__(self)
        self.x = 17
        self.y = 13

    def trigarea(self):
        return 1/2 * self.x * self.y


r = Triangle()
print("Area of rectangle is", r.rectarea())
print("Area of triangle is", r.trigarea())

