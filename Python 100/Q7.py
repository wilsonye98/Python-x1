# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.

class Strung:
    def __init__(self, n):
        self.strung = n

    def getString(self, n):
        self.strung = n

    def printString(self):
        return self.strung.upper()

n_strung = Strung("Testing")
print(n_strung.printString())

n_strung.getString('Ohh noooo!')
print(n_strung.printString())