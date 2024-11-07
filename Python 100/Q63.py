# Please write a program using generator to print the even numbers
# between 0 and n in comma separated form while n is input by console.

def even_generator(n):
    for num in range(0 , n + 1):
        if num % 2 == 0:
            yield num

num_inp = int(input('Please enter a valid number: '))
even_list = [n for n in even_generator(num_inp)]
print(even_list)