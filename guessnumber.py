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


print(guess())
