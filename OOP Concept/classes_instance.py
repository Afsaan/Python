class Person:
    def __init__(self , first , last):  # constructor
        self.first = first
        self.last = last
    
    def printf(self):
        print("{} {}".format(self.first , self.last))

emp1 = Person("afsaan" , "khan")
emp1.printf()
#or
Person.printf(emp1)