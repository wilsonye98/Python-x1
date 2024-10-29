# Write a program, which will find all such
# numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even
# number.The numbers obtained should be printed
# in a comma-separated sequence on a single line.
all_even = []

min_num = 1000
max_num = 3000

def all_even_bool(n):
    even = list(str(n))
    for nu in even:
        if int(nu) % 2 == 1:
            return False
    return True

for num in range(min_num, max_num + 1):
    if all_even_bool(num):
        all_even.append(num)

print(','.join(list(map(lambda x: str(x), all_even))))
