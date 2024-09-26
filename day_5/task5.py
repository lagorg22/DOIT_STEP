matrix = [
    [2, 9, 4],
    [7, 1, 3],
    [4, 2, 6]
]

for i in range(len(matrix)):
    for j in range(i + 1, len(matrix[0])):
        matrix[i][j], matrix[j][i] = matrix[j][i],  matrix[i][j]

print('Transponed matrix: ')
for row in matrix:
    print(row)