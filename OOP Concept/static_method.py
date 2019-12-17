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
    
    @staticmethod
    def is_weekday(day):
        if day.weekday()==6 or day.weekday()==7:
            return False
        else:
            return True
        

emp1 = Employee("afsaan" , "khan" , 2000)
emp2 = Employee("test" , "User" , 2000)

import datetime
my_data = datetime.date(2019 , 7 , 10)

print(Employee.is_weekday(my_data))