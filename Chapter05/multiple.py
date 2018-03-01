class Student:
    def __init__(self, r, n):
        self.roll = r
        self.name = n

    def showstudent(self):
        print("Roll :", self.roll)
        print("Name is", self.name)


class Science:
    def __init__(self, p, c):
        self.physics = p
        self.chemistry = c

    def showscience(self):
        print("Physics marks :", self.physics)
        print("Chemistry marks :", self.chemistry)


class Results(Student, Science):
    def __init__(self, r, n, p, c):
        Student.__init__(self, r, n)
        Science.__init__(self, p, c)
        self.total = self.physics + self.chemistry
        self.percentage = self.total / 200 * 100

    def showresults(self):
        Student.showstudent(self)
        Science.showscience(self)
        print("Total marks :", self.total)
        print("Percentage marks :", self.percentage)


s = Results(101, "David", 65, 75)
print("Result of student is")
s.showresults()
