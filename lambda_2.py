#The power of lambda is better shown when you use them as an anonymous function inside another function.

def one(n):
    return lambda x : x+n

a = one(4)

print(a(5))

