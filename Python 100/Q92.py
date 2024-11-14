# Please write a program which accepts a string from console and print
# the characters that have even indexes.

string = "H1e2l3l4o5w6o7r8l9d"

def filter_even_indices(string):
    flist = list(filter(lambda x: x[0] %2 == 0, enumerate(list(string))))

    return ''.join([x[1] for x in flist])

def filter_even_indices2(string):
    flist = string[::2]
    return flist

print(filter_even_indices(string))
print(filter_even_indices2(string))