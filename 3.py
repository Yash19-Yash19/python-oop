class Employee:

    increment = 1.5
    no_of_employees = 0
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees += 1


    def increase(self):
        self.salary = self.salary * self.increment
        self.salary = self.salary * Employee.increment
    @classmethod
    def change_increment(cls, amount):
        cls.change_increment = amount 

# print(Employee.no_of_employees)
# harry = Employee('harry', 'potter', 1000)
# print(Employee.no_of_employees)
# rohan = Employee('rohan', 'potter', 1000)
# print(Employee.no_of_employees)
harry = Employee('harry', 'potter', 1000)

print(harry.salary)
harry = Employee('harry', 'potter', 1000)
Employee.change_increment(3)
harry.increase()
print(harry.salary)
rohan = Employee('rohan', 'potter', 1000)


