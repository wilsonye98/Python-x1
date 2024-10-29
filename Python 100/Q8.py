# _Write a program which takes 2 digits, X,Y as input and
# generates a 2-dimensional array. The element value in the
# i-th row and j-th column of the array should be i _ j.*

def multi_depth_arr(rows, columns):
    outer_rows = []
    for row in range(0, rows):
        inner_rows = []
        for column in range(0, columns):
            inner_rows.append(row * column)
        outer_rows.append(inner_rows)
    return outer_rows

print(multi_depth_arr(3,5))