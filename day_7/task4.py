t1 = (1, 2, 3 ,4)

try:
    first, *mid, last = t1
    t2 = (last, *mid, first)
    print(f'Tuple with first and last elements swapped: {t2}')
except ValueError:
    print('Tuple must contain two or more elements.')
