class Product:
    price = 25
    def __init__(self, name):
        self.name = name

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __getattr__(self, name):
        return self.name


p = Product("Camera")
print(p.price)
print(p.name)
p.price = 15
p.name = "Cell"
print(p.name)
print(p.price)
