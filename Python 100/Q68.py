import random

def rand_number():
    rand_num = random.random() * 100
    if rand_num < 10:
        rand_num += 10
    return rand_num

def rand_number2():
    return random.uniform(10, 100)

print(rand_number2())
print(rand_number())
