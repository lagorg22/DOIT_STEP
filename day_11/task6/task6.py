def fun(filename1: str, filename2: str) -> None:
    with open(filename1, 'r') as f:
        content = f.read()

    with open(filename1, 'w') as f:
        pass

    with open(filename2, 'w') as f:
        f.write(content)

fun('f1.txt', 'f2.txt')