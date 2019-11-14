# init function

class Animal:
    p=10
    def __init__(self,legs,sound):
        self.legs = legs
        self.sound = sound

    def printf(self):
        # print(self.legs,self.sound)
        print("hello cat")

class Cat(Animal):
    def __init__(self,legs,sound,size):
        super().__init__(legs,sound)  # __init fucntion in the Cat base class overides the __init function of the Animal clas
        self.size = size
    
    def print_n(self):
        print(self.size)
        print(self.legs,self.sound)

animal = Cat(4,"meow","4.5")
animal.print_n()
animal.printf()


    