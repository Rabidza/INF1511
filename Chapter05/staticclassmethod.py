class Product:
    count = 0

    def __init__(self, name):
        self.name = name
        Product.count += 1

    @staticmethod
    def prodstatcount():
        return Product.count

    @classmethod
    def prodclasscount(cls):
        print("Class info:", cls)
        print("Class Method - The product count is:", cls.count)


p1 = Product("Camera")
p2 = Product("Cell")
print("Static method - The product count is:", Product.prodstatcount())
p2.prodclasscount()
