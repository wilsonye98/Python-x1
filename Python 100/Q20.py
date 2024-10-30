# Define a class with a generator which can iterate the
# numbers, which are divisible by 7, between a given range 0 and n.

class generator:
    def divisible(n):
        for item in range(0, n + 1, 7):
            if item % 7 == 0:
                yield item

for num in generator.divisible(7):
    print(num)

