def evenval(x):
    return x % 2 == 0


evens = filter(evenval, range(1, 11))
print(list(evens))
