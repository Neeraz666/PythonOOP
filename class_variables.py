class Employee:

    num_of_emps = 0

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1
    
    def fullname(self):
        return (f"{self.first} {self.last}")

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)



emp1 = Employee('Niraj', 'Pandey', 90000)
emp2 = Employee('Test', 'User', 50000)

# emp1.apply_raise()
# print(emp1.pay)

print(emp1.__dict__)

print(Employee.raise_amount) 
print(emp1.raise_amount)
print(emp2.raise_amount)
