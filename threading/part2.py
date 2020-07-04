# threading program
import time
import threading

start = time.perf_counter()


def some_function():
    print('start of the function')
    time.sleep(1)
    print('end of the function')


# creating 2 thread objects
t1 = threading.Thread(target = some_function)
t2 = threading.Thread(target = some_function)

t1.start()
t2.start()

t1.join()
t2.join()


finish = time.perf_counter()

print(f' time taken to finish the execution: {round(finish - start,2)}')

# in part 3 lets take 10 threads and run the program
