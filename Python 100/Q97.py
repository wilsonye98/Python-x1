# You are given an integer, N. Your task is to print an alphabet rangoli of size
# N. (Rangoli is a form of Indian folk art based on creation of patterns.)

import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    lines = []
    for i in range(size):
        sub_seq = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
        lines.append(sub_seq.center(4*size-3, '-'))
    print('\n'.join(lines[::-1] + lines[1:]))

N = 4
print_rangoli(N)