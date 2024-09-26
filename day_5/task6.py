import random

rand_matrix = []
for _ in range(4):
    row = [random.randint(0, 100) for _ in range(4)]
    rand_matrix.append(row)

print('Random matrix: ')

for row in rand_matrix:
    print(row)