# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with
# a given n input by console (n>0).

def compute(val):
    total = 0
    for num in range(1, val+1):
        total += num/(num+1)
    return round(total, 3)

print(compute(5))
