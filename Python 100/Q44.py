# Write a program which can map() to make a list whose
# elements are square of numbers between 1 and 20 (both included).

def square_1_to_20():
    sq_lst = list(map(lambda x: x ** 2, list(range(1,21))))
    return sq_lst

print(square_1_to_20())