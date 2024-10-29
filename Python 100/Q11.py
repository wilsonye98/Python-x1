# Write a program which accepts a sequence of comma
# separated 4 digit binary numbers as its input and
# then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed
# in a comma separated sequence.

def binary_div_by_5():
    input_str = input("Input: ").split(',')
    divisible_by_5 = []
    for ip in input_str:
        if int(ip, 2) % 5 == 0:
            divisible_by_5.append(ip)
    print(divisible_by_5)

binary_div_by_5()

