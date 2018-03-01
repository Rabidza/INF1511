from __future__ import division


class Worker:
    def __init__(self, c, n, s):
        self.code = c
        self.name = n
        self.salary = s

    def showworker(self):
        print("Code is", self.code)
        print("Name is", self.name)
        print("Salary is", self.salary)


class Officer(Worker):
    def __init__(self, c, n, s):
        Worker.__init__(self, c, n, s)
        self.hra = s * 60/100

    def showofficer(self):
        Worker.showworker(self)
        print("HRA - House Rent Allowance is", self.hra)


class Manager(Officer):
    def __init__(self, c, n, s):
        Officer.__init__(self, c, n, s)
        self.da = s * 98/100

    def showmanager(self):
        Officer.showofficer(self)
        print("DA - Dearness Allowance is", self.da)


w = Worker(101, "John", 2000)
o = Officer(102, "David", 4000)
m = Manager(103, "Ben", 5000)

print("Information of worker is")
w.showworker()
print("\nInformation of officer is")
o.showofficer()
print("\nInformation of manager is")
m.showmanager()
