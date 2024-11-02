# Define a function which can generate a list where
# the values are square of numbers between 1 and 20
# (both included). Then the function needs to print
# the last 5 elements in the list.

def print_squared_numbers():
    lst = []
    for num in  range(1,21):
        lst.append(num ** 2)
    for num in lst[-5:]:
        print(num)
    return lst

print_squared_numbers()