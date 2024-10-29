# With a given integral number n, write a program to
# generate a dictionary that contains (i, i x i) such
# that is an integral number between 1 and n (both included).
# and then the program should print the dictionary

def create_square_dict():
    num_input = int(input("Please enter a number: "))
    dict = {}
    for num in range(1, num_input + 1):
        dict[num] = num ** 2
    return dict

print(create_square_dict())
