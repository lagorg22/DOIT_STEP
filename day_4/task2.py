user_input = input('Enter text: ')

ascii_vals = [ord(char) for char in user_input]

print('Characters and corresponding ASCII values in input text: ')
for ch, ascii_val in zip(user_input, ascii_vals):
    print(f'{ch}: {ascii_val}')
