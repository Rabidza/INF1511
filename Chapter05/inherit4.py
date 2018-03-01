class Student:
    def __init__(self, r, n):
        self.roll = r
        self.name = n

    def showstudent(self):
        print("Roll :", self.roll)
        print("Name is", self.name)


class Science(Student):
    def __init__(self, r, n, p, c):
        Student.__init__(self, r, n)
        self.physics = p
        self.chemistry = c

    def showscience(self):
        Student.showstudent(self)
        print("Physics marks :", self.physics)
        print("Chemistry marks :", self.chemistry)


class Arts(Student):
    def __init__(self, r, n, h, g):
        Student.__init__(self, r, n)
        self.history = h
        self.geography = g

    def showarts(self):
        Student.showstudent(self)
        print("History marks :", self.history)
        print("Geography marks :", self.geography)


s = Science(101, "David", 65, 75)
a = Arts(102, "Ben", 70, 60)
print("Information of science student is")
s.showscience()
print("\nInformation of arts student is")
a.showarts()
