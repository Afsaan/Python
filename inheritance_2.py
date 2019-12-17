class Animal:   # parent class
    def __init__(self,name,age):
        self.x = name
        self.y = age

    def NameOfDog(self):
        print("name of the do is" + self.x)

class Dog(Animal): # this is base class which inherits the property of parent class
    def __init__(self,name,age,owner):
        super().__init__(name,age)
        self.owner = owner
    
    def OwnerOfDog(self):
        print("owmer of the dog is " + self.owner)


object = Dog("tinku",34,"rahul")
object.NameOfDog()
object.OwnerOfDog()
