# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers

def list_odd_square(*args):
    odd_squared_list = [x ** 2 for x in args if x % 2 == 1]
    return odd_squared_list

print(list_odd_square(1,2,3,4,5,6,7,8,9))