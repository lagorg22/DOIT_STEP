
def digit_sum(n):
    if not n:
        return 0

    return n % 10 + digit_sum(n //10)

print(digit_sum(123456))