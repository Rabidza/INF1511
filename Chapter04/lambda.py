def f(x):
    return x * 2


print("function:", f(3))

# Above function redone as a lambda function:
g = lambda x: x * 2
print("lambda:", g(3))

# A lambda function also does not need to be assigned to a variable
print("Lambda function without assignment: ")
print((lambda x: x * 2)(3))
