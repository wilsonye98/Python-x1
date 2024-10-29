# Write a program that accepts a sequence of
# whitespace separated words as input and prints
# the words after removing all duplicate words and
# sorting them alphanumerically.

def sort_string_no_duplicates(str):
    n_str = str.split(" ")
    n_arr = []
    for word in n_str:
        if word in n_arr:
            pass
        else:
            n_arr.append(word)
    n_arr_sorted = sorted(n_arr)
    # n_str_sorted = ""
    # for word in n_arr_sorted:
    #     n_str_sorted += word + " "
    return " ".join(n_arr_sorted)

print(sort_string_no_duplicates("hello world and practice makes perfect and hello world again"))
