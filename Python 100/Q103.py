# Given a number N.Find Sum of 1 to N Using Recursion

def recursive_sum(n):
    if n == 1 or n == 0:
        return n
    else:
        return n + recursive_sum(n - 1)

print(recursive_sum(5))