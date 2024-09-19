import random

ANSWER = random.randint(1, 20)

lives = 7

while lives > 0:
    user_input = input('Enter any integer: ')
    try:
        guess = int(user_input)
    except ValueError:
        print('Enter a valid number.')
        continue

    if guess > ANSWER:
        print('Your guess is greater than the answer.')
    elif guess < ANSWER:
        print('Your guess is lower than the answer.')
    else:
        print(f'Congrats! You won. the answer was {ANSWER}')
        break
    lives -= 1
    print(f'You have {lives} lives left.\n')

else:
    print(f'Unfortunately you have lost the answer was {ANSWER}. Try again!')
