import time
import random

def time_measurement(header):
    def time_measurement_inner(func):
        def wrapper(*args, **kwargs):
            t1 = time.perf_counter()
            result = func(*args, **kwargs)
            t2 = time.perf_counter()
            run_time = t2 - t1
            print(f"{header}: {func.__name__} performed in {run_time} seconds")
            wrapper.run_time.append(run_time)
            return result
        wrapper.run_time = []
        return wrapper
    return time_measurement_inner




@time_measurement("A")
def f():
    time.sleep(2 * random.random())
    #return 1

@time_measurement("B")
def g():
    time.sleep(2 * random.random())
    #return 1



a = f()
g()
#print(a)
#print(f"MAIN: {f.run_time}")
g()
a = f()
#print(a)
#print(f"MAIN: {f.run_time}")

print()
print(f.run_time)
print(g.run_time)


print("END")