# Please write a program to print the running time of execution of "1+1" for 100 times.

import time

def one_plus_one():
    before = time.time()
    for _ in range(0, 100):
        1+1
    after = time.time()
    execution = after - before
    return execution

print(one_plus_one())