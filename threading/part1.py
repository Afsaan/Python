# normal program
import time

start = time.perf_counter()


def some_function():
    print('start of the function')
    time.sleep(1)
    print('end of the function')

some_function()
some_function()

finish = time.perf_counter()

print(f' time taken to finish the execution: {round(finish - start,2)}')
# it takes 2 seconds to finsh the program in the part2 filw we will see the use of threadinf on the same program