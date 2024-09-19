SENTINEL = 'sum'

total_sum = 0

while True:
    user_input = input('Enter a positive number: ')
    if user_input == SENTINEL:
        print(f'Sum: {total_sum}')
        break

    try:
        num = float(user_input)
    except:
        print('Invalid input.')
        continue

    if num <= 0:
        print('Enter only positive number.')
        continue
    else:
        total_sum += num
