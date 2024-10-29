# Write a program that computes the value of a+aa+aaa+aaaa
# with a given digit as the value of a.

def compute_value(n):
    final_value = 0
    for val in range(1, 5):
        n_val = int(n * val)
        final_value += n_val
    return final_value

print(compute_value('9'))