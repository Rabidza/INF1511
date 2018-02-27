def square(x):
    return x * x


sqr = map(square, range(1, 11))
print(list(sqr))

k = map(int, [5, 10.15, 20, 25.628, 7])
print(list(k))
