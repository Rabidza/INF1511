import functools


def add(x, y):
    return x + y


r = functools.reduce(add, range(1, 11))
print(r)
