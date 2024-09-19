user_input = input('Enter a positive integer: ')

try:
    num = int(user_input)

    if num <= 0:
        print('The number must be greater than 0.')
    else:
        res = ''
        while num > 0:
            res += f'{num},'
            num -= 1
        res = res[:-1]
        print(res)
except ValueError:
    print('You must enter an integer.')
