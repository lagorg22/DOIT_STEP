#reads the lines and prints out the ones which are palindromes

with open('task_4.txt', 'w') as f:
    f.write('madam\n'
            'sun\n'
            'level\n'
            'languages\n'
            'radar\n'
            'dog\n'
            'noon\n'
            'books\n'
            'civic\n'
            'mountains\n'
            )

with open('task_4.txt', 'r') as f:
        for line in f.readlines():
            if line[:-1] == line[::-1][1:]:
                    print(line)
