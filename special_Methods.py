class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
    
    def fullname(self):
        return (f"{self.first} {self.last}")

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return f"Employee {self.first} {self.last} {self.pay}"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"
    
    def __add__(self, other):
        return self.pay + other.pay


emp1 = Employee('Niraj', 'Pandey', 90000)
emp2 = Employee('Test', 'User', 50000)

# print(emp1)

# print(repr(emp1))
# print(str(emp1))

# print(emp1.__repr__())
# print(emp1.__str__())

print(emp1+emp2)

