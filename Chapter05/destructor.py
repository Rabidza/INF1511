class Rect:
    n = 0

    def __init__(self, x, y):
        Rect.n += 1
        self.l = x
        self.b = y

    def __del__(self):
        Rect.n -= 1
        class_name = self.__class__.__name__
        print(class_name, "destroyed")

    def rectarea(self):
        print("Area of rectangle is", self.l * self.b)

    def noOfObjects(self):
        print("Number of objects are:", Rect.n)


r = Rect(3, 5)
r.rectarea()
s = Rect(5, 8)
s.rectarea()
r.noOfObjects()
del r
s.noOfObjects()
del s
