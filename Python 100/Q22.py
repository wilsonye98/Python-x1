# Write a program to compute the frequency of the words
# from the input. The output should output after sorting the
# key alphanumerically.

string = input('STRING: ').split(' ')
word_counter = {}

for word in string:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1

word_counter = dict(sorted(word_counter.items()))

for prop, count in word_counter.items():
    print(f"{prop}: {count}")

