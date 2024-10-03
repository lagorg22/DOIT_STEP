t = (1, (2, 3), (4, (5, 6)))

def solve(tup, result):
    for elem in tup:
        if type(elem) is tuple:
            solve(elem, result)
        else:
            result.append(elem)


result = []
solve(t, result)

result = tuple(result)
print(f'Tuple with all elements: {result}')