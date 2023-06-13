import random


def guess():
    x = int(input('Enter a number: '))
    # print(f'The entered number is {x}')
    number = int(input(f'Enter a number between 1 and {x}: '))
    gen_num = random.randint(1, x)
    print('The number has been generated.')

    while gen_num != number:
        # print('In the loop 01')
        if gen_num > number:
            # print('In the loop 02')
            print('Guessed number is low. Try again.')
        elif gen_num < number:
            # print('In the loop 03')
            print('Guessed number is high. Try again.')
        number = int(input(f'Enter a number between 1 and {x}: '))

    return f'You have guessed the right number which is {number}'


# print(guess())


def computer_guess():
    # low = 'l'
    # high = 'h'
    # correct = 'c'

    x = int(input('Enter a number for the computer to guess: '))
    print('Now, its time for you to guess the number that I have given.')
    print('Let me give you a range for you to guess quickly.')
    lower = int(input('Lower limit of range: '))
    higher = int(input('Higher limit of range: '))
    print(f'The range of numbers for you to guess is in between {lower} and {higher}')

    r_num = random.randint(lower, higher + 1)  # generating a random number

    while x != r_num:
        if x > r_num:
            print('Wrong guess. Try again')
        elif x < r_num:
            print('Wrong guess. Try again.')
        r_num = random.randint(lower, higher + 1)
    return 'You got the answer correct'


print(computer_guess())
