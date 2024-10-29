# Write a program that accepts a sentence
# and calculate the number of upper case letters
# and lower case letters.

def calculate_cases(string):
    cases = {
        'upper': 0,
        'lower': 0
    }

    for char in string:
        if char.isupper():
            cases['upper'] += 1
        elif char.islower():
            cases['lower'] += 1

    print(f'UPPERCASES: {cases["upper"]}')
    print(f'LOWERCASE: {cases["lower"]}')

calculate_cases('Hello world!')
