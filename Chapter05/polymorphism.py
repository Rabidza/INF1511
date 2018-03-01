class Book:
    def __init__(self, x):
        self.price = x


class Stockist(Book):
    def __init__(self, x):
        Book.__init__(self, x)

    def commission(self):
        self.comm = self.price * 5/100
        print("Commission of Stockist is %.2f" % self.comm)


class Distributor(Book):
    def __init__(self, x):
        Book.__init__(self, x)

    def commission(self):
        self.comm = self.price * 8/100
        print("Commission of Distributor is %.2f" % self.comm)


class Retailer(Book):
    def __init__(self, x):
        Book.__init__(self, x)

    def commission(self):
        self.comm = self.price * 10/100
        print("Commission of Retailer is %.2f" % self.comm)


r = Stockist(100)
s = Distributor(100)
t = Retailer(100)
prncomm = [r, s, t]

for c in prncomm:
    c.commission()
