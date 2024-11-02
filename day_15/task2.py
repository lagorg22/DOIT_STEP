
class Functor:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        if args[0] > 0:
            return self.func(*args, **kwargs)
        else:
            raise ValueError('Passed number must be positive integer.')


def fun(x: int):
    return x

functor = Functor(fun)
print(functor(-5))