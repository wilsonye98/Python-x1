# You are given a string S and width W. Your task is to wrap the string
# into a paragraph of width.

def wrap_string(str, width):
    wrapped = []
    nstr = ''
    nstrlen = 0
    for char in str:
        nstr += char
        nstrlen += 1
        if nstrlen == width:
            wrapped.append(nstr)
            nstr = ''
            nstrlen = 0
    wrapped.append(nstr)

    for str in wrapped:
        print(str)
    return wrapped

import textwrap

def wrap(string, max_width):
    string = textwrap.wrap(string,max_width)
    string = "\n".join(string)
    return string

# wrap_string('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4)

print(wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4))