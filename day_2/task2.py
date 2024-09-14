text = input('Enter text: ')

target_words = ['small', 'tall', 'middle']

word_found = False

for word in target_words:
    if word in text:
        word_found = True
        print(word)

if not word_found:
    print(f'None of these words: ({', '.join(target_words)}) were in the text: {text}')