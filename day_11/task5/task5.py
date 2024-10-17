
def fun(filename: str) -> None:
    with open(filename, 'r') as f:
        new_file_lines = []
        count = 0
        for line in f.readlines():
            new_file_lines.append(line)
            if len(new_file_lines) == 10:
                with open(f'file{count}', 'w') as file:
                    file.writelines(new_file_lines)
                new_file_lines.clear()
                count += 1
        else:
            with open(f'file{count}', 'w') as file:
                file.writelines(new_file_lines)

filename = 'task_5.txt'
fun(filename)

