class Rect:
    def __init__(self, x, y):
        self.l = x
        self.b = y

    def rectarea(self):
        return self.l * self.b


r = Rect(5, 8)
print("The area of rectangle is", r.rectarea())
