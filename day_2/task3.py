try:
    num_1 = float(input('Enter the first number: '))
    num_2 = float(input('Enter the second number: '))
    operator = input(f'Enter an operator: ')

    expression = f'{num_1}{operator}{num_2}'

    print(eval(expression))
except:
    print('Invalid inputs.')
