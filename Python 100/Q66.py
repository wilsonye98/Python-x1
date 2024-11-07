# Please write a program which accepts basic mathematic
# expression from console and print the evaluation result.

def evaluate_expression(exp):
    replace_mul = exp.replace('x', '*')
    return eval(replace_mul)

user_inp = input('Please enter a basic mathematical expression: ')
print(evaluate_expression(user_inp))