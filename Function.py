# 1 how to define function
# 2 positional and functional argument

def hello(num,age=29): # num is the positional argument and age is the keyword argument
    print("name is {} and age is {}".format(num,age))
hello(43,56)


#*args and **Kwargs

def fun1(*args,**kwargs):  #args = postional argumnet and **kwargs= keyword argumnet
    print(args)
    print(kwargs)

fun1(29,12,12,12,12,12,12,12,age=49)