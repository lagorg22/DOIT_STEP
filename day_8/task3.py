from functools import cache

@cache
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)

def fibo_seq(n):
    return [fibo(i) for i in range(n)]

print(*fibo_seq(15))

fibo.cache_clear()


