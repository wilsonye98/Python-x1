# Write a program which can map() to make a list
# whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

def square_list(lst):
    sq_lst = map(lambda x: x ** 2, lst)
    return list(sq_lst)

print(square_list([1,2,3,4,5,6,7,8,9,10]))
