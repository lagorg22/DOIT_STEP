def is_anagram(s1, s2):
    if len(s1) != len(s2) or sorted(s1) != sorted(s2):
        print(f'{s1} and {s2} are not anagrams.')
    else:
        print(f'{s1} and {s2} are anagrams.')

first = input('Enter first string: ')
second = input('Enter second string: ')

is_anagram(first, second)
