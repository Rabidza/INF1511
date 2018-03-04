class MyException(Exception):
    def __init__(self, quantity):
        Exception.__init__(self)
        self.quantity = quantity


try:
    s = int(input("Enter quantity: "))
    if s <= 0:
        raise MyException(s)
except EOFError:
    print("You pressed EOF")
except MyException as ex:
    print("MyException: The quantity entered is %d, it must be some positive value" %ex.quantity)
else:
    print("No exception raised.")
