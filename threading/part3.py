#threading
import time
import threading

start = time.perf_counter()


def some_function():
    print('start of the function')
    time.sleep(1)
    print('end of the function')
    

threads = []
for _ in range(10):
    t = threading.Thread(target=some_function)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


finish = time.perf_counter()

print(f' time taken to finish the execution: {round(finish - start,2)}')