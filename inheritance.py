class animal:
    x=10
    y=20
    def printf(self):
        print(self.x , self.y)

class cat(animal):
    #what happens behind the scene is that all the attribute of the animal class function comes inside the cat class
    """
    x = 10
    y = 20
    def printf(self):
        print(self.x,self.y)
    """
    pass


A = cat()

A.printf()