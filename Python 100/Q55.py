# Write a program which accepts a sequence of words separated by
# whitespace as input to print the words composed of digits only.

def only_digits(string):
    digits = []
    for words in string.split(' '):
        if words.isdigit():
            digits.append(words)
    return digits

print(only_digits('2 cats and 3 dogs.'))