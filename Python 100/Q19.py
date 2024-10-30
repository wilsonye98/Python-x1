# You are required to write a program to sort the (name, age, score) tuples
# by ascending order where name is string, age and score are numbers. The
# tuples are input by console.

people_array = []

while True:
    person = tuple(input('Please enter name, age, score: ').split(','))
    if len(person) == 3:
        people_array.append(person)
    else:
        break


sorted_people_array = sorted(people_array, key=lambda x: (x[0], x[1], x[2]))

print(sorted_people_array)