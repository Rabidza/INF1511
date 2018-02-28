class Rect:
    l = 8
    b = 5

    def rectarea(self):
        return Rect.l * Rect.b


r = Rect()
print("Area of rectangle is", r.rectarea())
