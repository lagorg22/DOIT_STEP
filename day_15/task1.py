
def positive_checker(func):
    def wrapper(*args, **kwargs):
        if args[0] > 0:
            return func(*args, **kwargs)
        else:
            raise ValueError('Passed number must be positive integer.')

    return wrapper



@positive_checker
def fun(x: int):
    return x

print(fun(-5))