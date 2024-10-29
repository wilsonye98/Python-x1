# Write a program that accepts a sentence and
# calculate the number of letters and digits.

letters = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

def count_letters_digits():
    user_input = list(input('Please enter a string'))
    letter_count = 0
    digit_count = 0

    for char in user_input:
        if char in letters:
            letter_count += 1
        elif char in digits:
            digit_count += 1

    print(f'LETTERS: {letter_count}')
    print(f'DIGITS: {digit_count}')

count_letters_digits()
