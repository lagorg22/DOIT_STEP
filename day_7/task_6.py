s1 = {'a', 'b', 'c'}
s2 = {1, 2, 3}

result = set()
for a in s1:
    for b in s2:
        result.add((a, b))

print(f'All combinations of two sets: {result}')
