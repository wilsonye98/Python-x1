# Write a program which accepts a sequence of comma-separated numbers
# from console and generate a list and a tuple which contains every number.

def array_and_tuple(*args):
    n_arr = []
    n_tup = ()
    for num in args:
        n_arr.append(num)
        n_tup = n_tup + (num,)
    return [n_arr, n_tup]

y_arr, y_tup = array_and_tuple(34,67,55,33,12,98)

print(y_arr)
print(y_tup)

