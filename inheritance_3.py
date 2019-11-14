class Animal:
    def __init__(self,name,age):
        self.x = name
        self.y = age
        self._z = 10
    def DogName(self):
        print("name of the dog is {}".format(self.x))

    # to use protected varibale we have to use setter and getter
    def get_value(self,value):
        self._x = value

    def set_value(self):
        return self._x

class Dog(Animal):
    def __init__(self,name,age,owner):
        self.name = name
        self.age = age
        self.owner = owner

    def ownerName (self):
        print("name of the owner is {} and dog name is {} and age of the dog is {}".format(self.owner,self.name,self.age))


object = Dog("hello",34,"rahul")
object.ownerName()
object1 = Animal("afsaan",35)
object1.DogName()

# name in dog class is 
print(object.name)

print("\n")

print(object1.x)

# now if u call the method which there in child class and no thier in parent class
object.DogName()