# Please write a program which count and print the numbers of each character
# in a string input by console.

def count_char(string):
    charDict = {}
    for char in string:
        charDict[char] = charDict.get(char, 0) + 1

    for item in charDict:
        print(item, charDict[item])
    
    return charDict

print(count_char('abcdefgabc'))
