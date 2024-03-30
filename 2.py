
class Employee:

    increment = 1.5

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increment = 2

    def increase(self):
        self.salary = self.salary * self.increment
        self.salary = self.salary * Employee.increment


harry = Employee('harry', 'potter', 1000)
rohan = Employee('rohan', 'potter', 1000)


harry = Employee('harry', 'potter', 1000)
rohan = Employee('rohan', 'potter', 1000)


print(harry.salary)
harry.increase()
print(harry.salary)


print(harry.__dict__)
print(Employee.__dict__)
