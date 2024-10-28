# Write a program which will find all such numbers which
# are divisible by 7 but are not a multiple of 5, between
# 2000 and 3200 (both included).The numbers obtained should be
# printed in a comma-separated sequence on a single line.

def divisible_arr(start, end, n):
    div_arr = []
    for num in range(start, end+1):
        if num % n == 0 and num % 5 != 0:
            div_arr.append(num)

    return div_arr


print(divisible_arr(2000, 3500, 7))
