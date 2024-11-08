# Please write a program to randomly print a integer number between 7 and 15 inclusive.

import random

def get_rand_int():
    return random.randint(7, 15)

print(get_rand_int())