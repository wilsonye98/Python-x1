#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    n_binary = bin(n)
    n_binary_string = str(str(n_binary).split(' ')[0][2:])
    maximum = 0
    current = 0

    for i, char in enumerate(n_binary_string):
        if char == '1':
            current += 1
        elif char == '0':
            if maximum > current:
                current = 0
            if current >= maximum:
                maximum = current
                current = 0

        if i == len(n_binary_string) - 1:
            if current > maximum:
                maximum = current
                current = 0

    print(maximum)





