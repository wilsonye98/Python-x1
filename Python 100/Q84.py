# By using list comprehension, please write a program generate a 3*5*8 3D
# array whose each element is 0.

array_3d = [[[0 for _ in range(8)] for _ in range(5)] for _ in range(3)]
print(array_3d)

array_3d2 = []

for _ in range(3):
    a_arr = []
    for _ in range(5):
        b_arr = []
        for _ in range(8):
            b_arr.append(0)
        a_arr.append(b_arr)
    array_3d2.append(a_arr)

print(array_3d2)