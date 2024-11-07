# Please write a program using generator to print the numbers
# which can be divisible by 5 and 7 between 0 and n in comma
# separated form while n is input by console.

def five_and_seven_divisible(n):
    for num in range(0, n+1):
        if num % 5 == 0 and num % 7 == 0:
            yield num

num_inp = int(input('Please enter a valid number: '))
div_list = [n for n in five_and_seven_divisible(num_inp)]
print(div_list)
