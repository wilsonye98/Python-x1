# By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in
# [12,24,35,70,88,120,155].

lst = [12,24,35,70,88,120,155]
f_lst = [x for i,x in enumerate(lst) if not (1 < i < 5)]

print(f_lst)