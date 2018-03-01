class Rect:
    def __init__(self, x, y):
        self.l = x
        self.b = y

    def rectarea(self):
        return self.l * self.b


r = Rect(5, 8)
s = r
print("Area of a rectangle is", r.rectarea())
print("Area of a rectangle is", s.rectarea())
