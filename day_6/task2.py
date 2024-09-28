operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b ,
    '//': lambda a, b: a // b,
    '**': lambda a, b: a ** b
}

num_1 = float(input('Enter first number: '))
num_2 = float(input('Enter second number: '))
operation = input('Enter one of these operations(+, -, *, /, //, **): ')

try:
    print(operations[operation](num_1, num_2))
except (ZeroDivisionError, KeyError, ValueError) as e:
    print(f'Invalid input: {e}')
