def squarenum(x):
    return x * x


iteratorobj = (squarenum(x) for x in range(6))
print("The squares of the first five sequence numbers")
print(iteratorobj.__next__())
print(iteratorobj.__next__())
print(iteratorobj.__next__())
print(iteratorobj.__next__())
print(iteratorobj.__next__())
print(iteratorobj.__next__())
