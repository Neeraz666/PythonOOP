

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
    
    def fullname(self):
        return (f"{self.first} {self.last}")


emp1 = Employee('Niraj', 'Pandey', 90000)
emp2 = Employee('Test', 'User', 50000)

print(emp1.email)
print(emp2.email)

print(emp1.fullname())
print(emp2.fullname())

print(Employee.fullname(emp1))

