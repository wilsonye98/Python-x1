# Write a program that accepts sequence of lines
# as input and prints the lines after making all
# characters in the sentence capitalized.

inputting = True
inputs = []

while inputting:
    input_line = input("String: ")
    if input_line:
        inputs.append(input_line)
    else:
        inputting = False

inputs = list(map(lambda x: x.upper(), inputs))
for ip in inputs:
    print(ip)