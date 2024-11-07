# Please write a program to output a random even number between
# 0 and 10 inclusive using random module and list comprehension.
import random

even_lst = [n for n in range(1, 11) if n % 2 == 0]
print(random.choice(even_lst))
