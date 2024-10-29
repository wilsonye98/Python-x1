# Write a program that accepts a comma separated sequence of
# words as input and prints the words in a comma-separated sequence
# after sorting them alphabetically.

def sorted_string():
    string = input('Please enter words separated by a comma: ')
    string_arr = string.split(',')
    string_arr.sort()
    return ",".join(string_arr)

print(sorted_string())