try:
# creating the class
    class First:
        def __init__(self,x=4,y=0):
            self.x=x
            self.y=y
        def first(self,x,y):
            print(self.x+self.y)

# creating the instane of the class
    object = First(10,20)
    a = object.x
    print(a)
    object.first(5,6)
    object1 = First()
    print(object1.x)
# deleting the attribute x of object1
    del object1.x
    print(object1.x)


# handling the error
except AttributeError:
    print("Attribute of object 1 was deleted")
