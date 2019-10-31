class Fly:
    def __init__(self,job1="",job2="",job3=""):
        self.x = job1
        self.y = job2
        self.z = job3
        self._new = "c++"   # this is the protected class

    def All_jobs (self):
        print(self.x,self.y,self.z,self._new)


    def Some_method(self,algo,lib):
        print(algo)
        print('\n')
        print(lib)

    def getter(self): #setter and getter is required if you want to change value
        print (self._new)

    def setter(self,value):  #getter
        self._new = value

    