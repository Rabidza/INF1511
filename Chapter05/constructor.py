class Rect:
    def __init__(self, x=8, y=5):
        self.l = x
        self.b = y

    def rectarea(self):
        return self.l * self.b


r = Rect()
s = Rect(10, 20)
print("Area of rectangle is", r.rectarea())
print("Area of rectangle is", s.rectarea())
