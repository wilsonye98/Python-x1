# Define a function which can generate and print a
# list where the values are square of numbers between
# 1 and 20 (both included).

def print_squared_numbers():
    lst = []
    for num in  range(1,21):
        lst.append(num)
        print(num ** 2)
    return lst

print_squared_numbers()