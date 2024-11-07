# Fib #2

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

fib_inp = input('Enter a number: ')
fib_list = [fib(n) for n in range(0, int(fib_inp) + 1)]
print(fib_list)