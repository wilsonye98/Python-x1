# Please generate a random float where the value is between 5 and 95 using Python module.
import random

def rand_number():
    rand_num = random.random() * 95
    if rand_num < 5:
        rand_num += 5
    return rand_num

def rand_number2():
    return random.uniform(5, 95)
