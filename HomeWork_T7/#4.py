import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Время выполнения функции {func.__name__}: {end_time - start_time} сек.')
        return result
    return wrapper

@measure_time
def my_function():
    time.sleep(2)
    return "Hello, World!"

my_function()