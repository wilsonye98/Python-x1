# Define a function which can generate a dictionary
# where the keys are numbers between 1 and 20 (both included)
# and the values are square of keys. The function should just
# print the keys only.

def squared_dict():
    dict = {}
    for num in range(1, 21):
        dict[num] = num ** 2
    return dict.keys()

print(squared_dict())