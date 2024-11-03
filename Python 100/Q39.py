# Write a program to generate and print another tuple whose
# values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

def even_tup(tup):
    even = []
    for num in tup:
        if num % 2 == 0:
            even.append(num)

    return tuple(even)

print(even_tup((1,2,3,4,5,6,7,8,9,10)))