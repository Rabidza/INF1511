class Rect:
    def __init__(self, x, y):
        self.__l = x
        self.__b = y

    def rectarea(self):
        return self.__l * self.__b


r = Rect(5, 8)
print("Area of rectangle is", r.rectarea())
print("Area of rectangle is", r._Rect__l * r._Rect__b)
