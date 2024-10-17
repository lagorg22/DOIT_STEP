
with open('task_1.txt', 'w') as f:
    for i in range(1, 1001):
        f.write(f'{i}. hello Mr Irakli\n')

with open('task_1.txt', 'r') as f:
    line_count = f.readlines()[-1].split()[0][:-1]
    print(line_count)