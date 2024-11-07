# Please write a program to randomly generate a list with
# 5 even numbers between 100 and 200 inclusive.

import random

even_lst = random.sample([n for n in range(100, 201) if n % 2 == 0], 5)
print(even_lst)