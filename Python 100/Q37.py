# Define a function which can generate and print a
# tuple where the value are square of numbers between
# 1 and 20 (both included).

def tuple_squared_numbers_from_array():
    lst = []
    for num in  range(1,21):
        lst.append(num ** 2)
    print(tuple(lst))
    return tuple(lst)

tuple_squared_numbers_from_array()