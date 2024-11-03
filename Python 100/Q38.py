# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to
# print the first half values in one line and the last half values in one line.

def separate_half(tup):
    tup_len = len(tup)
    first_half = tup[:round(tup_len/2)]
    second_half = tup[round(tup_len/2):]
    print(first_half)
    print(second_half)

separate_half((1,2,3,4,5,6,7,8,9,10))