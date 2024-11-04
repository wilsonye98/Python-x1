# Write a program which can filter() to make a list whose elements
# are even number between 1 and 20 (both included).

def even_between_1_and_20():
    even_lst = list(filter(lambda x: x % 2 == 0, list(range(1,21))))
    return even_lst

print(even_between_1_and_20())
