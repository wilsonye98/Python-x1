# Define a function that can accept two strings as input and print
# the string with maximum length in console. If two strings have the same length,
# then the function should print all strings line by line.

def longest_string(n, m):
    if len(m) > len(n):
        longest = m
        print(longest)
    elif len(m) == len(n):
        print(n)
        print(m)
    else:
        print(n)

longest_string('Hello World', "World Hello")