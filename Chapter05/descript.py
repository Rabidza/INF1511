class Product:
    def __init__(self, name, x=5):
        self.name = name
        self.price = x

    def __set__(self, obj, value):
        print("Setting attribute", self.name)
        self.price = value

    def __get__(self, obj, objtype):
        print("Getting attribute", self.name)
        return self.price

    
class Cart:
    p = Product("butter", 7)


k = Cart()
print(k.p)

k.p = 10
print(k.p)
