user_input = input('Enter a string: ')
symbols = set()
for ch in user_input:
    symbols.add(ch)

print(f'Symbols in " {user_input} ": {symbols}')