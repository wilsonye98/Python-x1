# Define a class Person and its two child classes: Male and Female.
# All classes have a method "getGender" which can print "Male" for Male
#     class and "Female" for Female class.

class Person:
    def __init__(self, name):
        self.name = name

class Male(Person):
    def __next__(self, name):
        super(name)

    def getGender(self):
        return 'Male'

class Female(Person):
    def __next__(self, name):
        super(name)

    def getGender(self):
        return 'Female'

male_one = Male('Johnny2Hat')
female_one = Female('Jessy1Sock')

print(male_one.getGender())
print(female_one.getGender())