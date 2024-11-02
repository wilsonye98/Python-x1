# Define a function which can print a dictionary where
# the keys are numbers between 1 and 20 (both included)
# and the values are square of keys.

def squared_dict():
    dict = {}
    for num in range(1, 21):
        dict[num] = num ** 2
    return dict

print(squared_dict())

