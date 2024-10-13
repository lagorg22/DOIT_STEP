#filters out non-palindrome strings from the list
l = ['abcd', 'aba', 'aaaaa', 'fsdfsfg', 'fdsddsdf']

res = list(filter(lambda s: s == s[::-1], l))
print(res)

