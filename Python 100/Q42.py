# Write a program which can map() and filter() to make a list
# whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]

def square_list_even(lst):
    sq_lst = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, lst))
    return list(sq_lst)

print(square_list_even([1,2,3,4,5,6,7,8,9,10]))