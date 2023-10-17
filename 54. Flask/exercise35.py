import time

current_time = time.time()


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        stop_time = time.time()
        return (stop_time - start_time)
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


print(current_time)
print(f"fast_function run time: {fast_function()}")
print(f"slow_function run time: {slow_function()}")
