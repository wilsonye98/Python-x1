# You are given a string.Your task is to count the frequency of
# letters of the string and print the letters in descending order
# of frequency.

def letter_freq(string):
    lst = list(string)
    let_freq = {}
    for char in lst:
        if char in let_freq:
            let_freq[char] += 1
        else:
            let_freq[char] = 1
    let_freq = sorted(let_freq.items(), key=lambda x: x[1], reverse=True)
    for letter in let_freq:
        print(f"{letter[0]} {letter[1]}")


letter_freq('aabbbccde')