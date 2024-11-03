
def positive_checker(func):
    def wrapper(*args, **kwargs):
        if args[0] > 0:
            print(func(*args, **kwargs))
        else:
            raise ValueError('Passed number must be a positive integer.')

    return wrapper



@positive_checker
def fun(x: int):
    return x

fun(-5)