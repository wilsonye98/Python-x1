# Enter your code here. Read input from STDIN. Print output to STDOUT

total = int(input())
count = 0

while count < total:
    string = input()

    result = [[], []]

    for i, char in enumerate(string):
        if i % 2 == 0:
            result[0].append(char)
        else:
            result[1].append(char)

    print(f"{''.join(result[0])} {''.join(result[1])}")

    count += 1
