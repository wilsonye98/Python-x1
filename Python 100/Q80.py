# Please write a program to print the list after removing
# even numbers in [5,6,77,45,22,12,24].

lst = [5,6,77,45,22,12,24]
f_lst = filter(lambda x: x % 2 == 1, lst)

print(f_lst)