l = ['hello', 'riding', 'coding', 'nod']
ending = 'ing'

try:
    res = list(filter(lambda s: s.count(ending) and s.rindex(ending) + len(ending) == len(s), l))
    print(res)
except (TypeError, AttributeError) as e:
    print(e)

