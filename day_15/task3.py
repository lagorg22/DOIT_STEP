import time


def time_spent(func):
    def wrapper(*args, **kwargs):
        time_begin = time.time()
        func(*args, **kwargs)
        time_end = time.time()
        spent_time = (time_end - time_begin) * 1000
        print(f'This function took {spent_time.__round__(3)}ms to finish')

    return wrapper

@time_spent
def fun(n: int):
    for i in range(n):
        a = i

fun(50)