class Book:
    price = 100

    @classmethod
    def display(cls):
        print(cls.price)

    def show(self, x):
        self.price = x
        print(self.price)


b = Book()
c = Book()

Book.display()
b.display()
b.show(200)
c.show(300)
