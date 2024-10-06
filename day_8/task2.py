def count_symbol(s1: str, s2: str):
    return s1.count(s2)


string = input('Enter a String: ')
symbol = input('Enter a symbol: ')
print(count_symbol(string, symbol))