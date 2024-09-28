sentence = input('Enter some sentence: ')

words = sentence.split(' ')

result = {word: words.count(word) for word in words}

print(result)