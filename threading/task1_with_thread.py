# from a given list of numbers print the square and cube of every number in the list
import time
import threading

start = time.perf_counter()

numbers = [2,3,8,9]

def square():
    square_list = [ number**2 for number in numbers ]
    time.sleep(5)
    print(square_list)

def cube():
    cube_list = [number**3 for number in numbers]
    time.sleep(5)
    print(cube_list)


t1 = threading.Thread(target=square)
t2 = threading.Thread(target=cube)

t1.start()
t2.start()

t1.join()
t2.join()


finish = time.perf_counter()

print(f'total time taken is {round(finish-start , 2)}')