# You are given words. Some words may repeat. For each word,
# output its number of occurrences. The output order should correspond
# with the input order of appearance of the word. See the sample input/output
# for clarification.

def word_counter(words):
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

words = []

while True:
    word = input('Please enter a word: ')
    if word:
        words.append(word)
    else:
        break

print(word_counter(words))
