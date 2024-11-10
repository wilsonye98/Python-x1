# By using list comprehension, please write a program to print the
# list after removing numbers which are divisible by 5 and 7 in
# [12,24,35,70,88,120,155].

def not_div(num):
    if not (num % 7 == 0 and num % 5 == 0):
        return True
    else:
        return False

lst = [12,24,35,70,88,120,155]
f_lst = [x for x in lst if not (x % 7 == 0 and x % 5 == 0)]

print(f_lst)