# this function is also known as anonymoous function or the function with no name

#normal method
def add(a,b):
    return a+b

print(add(10,2))

#lambda 
a=lambda a,b:a+b

print(a(10,20))

# one more

#normal mehtod
def even(n):
    if n %2==0:
        return "number is even"

print(even(10))

#lambda
a = lambda n: n%2==0

print(a(10))
