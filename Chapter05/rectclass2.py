class Rect:
    l = 8
    b = 5


print("Length is %d, Breadth is %d" % (Rect.l, Rect.b))
print("Class name is", Rect.__name__, "and Base class is", Rect.__bases__)
print("Attributes of this class are", Rect.__dict__)
