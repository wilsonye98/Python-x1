# Please write a program to output a random number, which is
# divisible by 5 and 7, between 10 and 150 inclusive using random
# module and list comprehension.
import random

div_5and7_lst = [n for n in range(10, 151) if n % 7 == 0 and n % 5 == 0]
print(random.choice(div_5and7_lst))