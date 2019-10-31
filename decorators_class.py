class Function:
    def __init__(self,name='',age=0,gender=""):
        self.name = name
        self.age = age
        self.gender = gender

    def Details(self):
        print("name is {} age is {} and gender is {}".format(self.name,self.age,self.gender))

    @classmethod
    def Owner(cls,name,gender):
         return Function(name,gender)
    
    @staticmethod
    def dog(age,color):
        print("age of the dog is {} and color is {}".format(age,color))
1
a=Function.Owner("afsaan","female")
a.Details()
Function.dog(12,"pink")