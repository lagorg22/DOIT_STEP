def reverse_str(s: str):
    if len(s) == 1:
        return s

    return  reverse_str(s[1:]) + s[0]

print(reverse_str('Hello'))