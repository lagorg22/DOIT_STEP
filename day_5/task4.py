matrix_1 = [
    [4, 7, 2, 9],
    [6, 1, 8, 3],
    [5, 2, 4, 7],
    [9, 6, 3, 1]
]

matrix_2 = [
    [8, 3, 1, 6],
    [2, 9, 4, 5],
    [7, 1, 3, 8],
    [4, 2, 6, 9]
]

rows = len(matrix_1)
cols = len(matrix_1[0])

res_matrix = []

for i in range(rows):
    current_row = []
    for j in range(cols):
        current_row.append(matrix_1[i][j] + matrix_2[i][j])
    res_matrix.append(current_row)

for r in res_matrix:
    print(r)