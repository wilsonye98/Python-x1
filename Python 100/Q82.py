# By using list comprehension, please write a program to print
# the list after removing the 0th, 2nd, 4th,6th numbers in
# [12,24,35,70,88,120,155].

lst = [12,24,35,70,88,120,155]
f_lst = [x for i, x in enumerate(lst) if i != 0 and i != 2 and i != 4 and i != 6]

print(f_lst)
