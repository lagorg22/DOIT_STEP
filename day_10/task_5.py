from functools import reduce

nums = [1, 'ada', 3, 'dsaf', 4, 5]

try:
    res = reduce(lambda a, b: a * b, nums)
    print(res)
except TypeError as e:
    print(e)