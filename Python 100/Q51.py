# Write a function to compute 5/0 and use try/except to catch the exceptions.

def dividing_by_zero():
    try:
        return 5/0
    except ZeroDivisionError:
        print('Division by zero is not possible')

dividing_by_zero()