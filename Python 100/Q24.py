# Python has many built-in functions, and if you
#     do not know how to use it, you can read document
#     online or find some books. But Python has a built-in
#     document function for every built-in functions.

def get_docstring(f):
    return f.__doc__

print(get_docstring(abs))