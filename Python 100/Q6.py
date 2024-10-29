# Write a program that calculates and prints the value
# according to the given formula:
# Q = Square root of [(2 _ C _ D)/H]
# C is 50. H is 30.

from math import sqrt

C = 50
H = 30

def sqrt_form(D):
    return round(sqrt((2*C*D)/H))

arr_input = input("Please enter numbers separated by commas. ")
arr_input = arr_input.split(",")
arr_results = []

for num in arr_input:
    arr_results.append(sqrt_form(round(int(num))))

print(",".join(list(map(lambda a: str(a), arr_results))))
