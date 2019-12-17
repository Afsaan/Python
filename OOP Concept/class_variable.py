class Employee:

    raise_amount = 1.05   # class attribute
    employee_count = 0 # to count the number of employee

    def __init__(self , first , last , pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first +"" +self.last+"@gmail.com"
        Employee.employee_count +=1

    def fullname(self):
        return '{} {}'.format(self.first , self.last)

    def apply_raise(self):
        # self.pay = self.pay*raise_amount ---->this you cannot use now 
        self.pay = self.pay*self.raise_amount #---->correct way
        return self.pay
emp1 = Employee("afsaan" , "khan" , 2000)

emp2 = Employee("test" , "User" , 2000)


# print(emp1.apply_raise())
# print(emp2.apply_raise())

#trick
# print(emp1.__dict__)
# print(emp2.__dict__)
# print(Employee.__dict__)

Employee.raise_amount = 1.04 

# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)

Employee.raise_amount = 1.04
# change the value of raise_amount

emp1.raise_amount = 1.06

print(emp1.apply_raise())
print(emp2.apply_raise())

print(emp1.__dict__)

print(Employee.employee_count)