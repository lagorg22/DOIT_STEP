with open('task_2.txt', 'w') as f:
    for i in range(18):
        if i+1 in [2, 8, 10, 13, 17]:
            f.write(str(i+1) + '\n')
        else:
          f.write('\n')