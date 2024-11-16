# Write a Python program that accepts a string and calculate the number
# of digits and letters.

def counter(str):
    counter_dict = {
        'letter': 0,
        'digit': 0
    }

    for char in str:
        if char.isdigit():
            counter_dict['digit'] += 1
        elif char.isalpha():
            counter_dict['letter'] += 1

    print(f"Letters: {counter_dict['letter']}")
    print(f"Digit: {counter_dict['digit']}")

counter('Hello321Bye360')