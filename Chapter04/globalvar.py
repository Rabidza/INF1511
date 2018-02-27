def compute():
    global x
    print("The value of x in compute function is", x)
    x += 5
    return None


def dispvalue():
    global x
    print("The value of x in dispvalue function is", x)
    x -= 2
    return None


x = 0
compute()
dispvalue()
compute()
