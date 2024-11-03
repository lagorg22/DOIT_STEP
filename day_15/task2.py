
class Functor:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        if args[0] > 0:
            print(self.func(*args, **kwargs))
        else:
            raise ValueError('Passed number must be a positive integer.')


def fun(x: int):
    return x

functor = Functor(fun)
functor(-5)