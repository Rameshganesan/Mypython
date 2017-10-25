class Employee:
    def __init__(self, fname, lname, pay):
        self.first_name = fname
        self.last_name = lname
        self.e_mail = fname+'.'+lname+'@company.com'
        self.pay = int(pay)
    def increase_pay(self, percent):
        self.pay = self.pay * percent


emp1 = Employee('Ramesh','Ganesan',20000)
emp2 = Employee('Sam','Walton',200000)

print(emp1.first_name)
print(emp1.e_mail)
print(emp2.first_name)
print(emp2.e_mail)
emp1.increase_pay(1.05)
print(emp1.pay)
print(emp2.pay)
