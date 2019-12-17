# static and class mathod

# Their are three types of method 1- regular method = which has the instance as the first argumnet which i called as self
# 2- class mehtod = you pass class name as the first argument which is called as clss
# 3- static method = you do not pass anything as a first argument and it is a normal function

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
        self.pay = self.pay*self.raise_amount 
        return self.pay
    
    @classmethod
    def separate(cls , emp):
        first , last , pay = emp.split("-")
        return cls(first , last , pay)




emp1 = Employee("afsaan" , "khan" , 2000)
emp2 = Employee("test" , "User" , 2000)

# Employee.set_raise_amount(10)

# emp_str1 = "meenu-manoj-1997"              ---|
# emp_str2 = "rahul-tiwari-1998"                |
#                                               |
# first , last , pay = emp_str1.split("-")      |==> now this i have to do for each and every employee so
#                                               |      the alternative is to create a class mehtod constructor
# emp_str1 = Employee(first , last , pay)    ---|

emp_str1 = "meenu-manoj-1997"          
emp_str2 = "rahul-tiwari-1998"

emp3 = Employee.separate(emp_str2)
print(emp3.__dict__)
print(emp3.fullname())





