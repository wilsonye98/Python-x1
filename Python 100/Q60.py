# f(n)=f(n-1)+100 when n>0
# and f(0)=0

def f(n):
    if n == 0:
        return 0
    else:
        return f(n - 1) + 100

inp = int(input('Please enter a number: '))
print(f(inp))