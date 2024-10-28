# Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated
# sequence on a single line.Suppose the following input
# is supplied to the program: 8 Then, the output should be:40320

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def factorial_loop(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num

print(factorial_recursive(8))