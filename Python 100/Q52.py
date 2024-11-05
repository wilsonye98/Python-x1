# Define a custom exception class which takes a string message as attribute.

class CustomError(Exception):
    def __str__(self):
        return 'Ops something went wrong.'

def errorFunction():
    try:
        if True:
            raise CustomError
    except CustomError as e:
        print(f'Error: {e}')

errorFunction()