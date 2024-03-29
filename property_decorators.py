class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"
    
    @property
    def fullname(self):
        return (f"{self.first} {self.last}")
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
    
emp1 = Employee('Niraj', 'Pandey', 90000)

# emp1.first = 'Jim'
emp1.fullname = 'John Smith'


print(emp1.first)
print(emp1.email)
print(emp1.fullname)

del emp1.fullname
