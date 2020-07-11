def square_number(nums):
    square_list = []
    for i in nums:
        square_list.append(i*i)
    return square_list

my_nums = square_number([1,2,3,4,5])

print(my_nums)

# use of yield
def square_number(nums):
    for i in nums:
        yield i*i

my_nums = square_number([1,2,3,4,5])

# print(next(my_nums))
# print(next(my_nums)) 
# print(next(my_nums))  
# print(next(my_nums)) 
# print(next(my_nums)) 

for num in my_nums:
    print(num)