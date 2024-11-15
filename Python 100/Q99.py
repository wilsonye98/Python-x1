# Given 2 sets of integers, M and N, print their symmetric difference
# in ascending order. The term symmetric difference indicates those values
# that exist in either M or N but do not exist in both.

def sym_diff(m, n):
    m_set = set(m.split(' '))
    n_set = set(n.split(' '))

    c_set = list(m_set ^ n_set)
    c_set = sorted(list(map(lambda x: int(x), c_set)))

    for num in c_set:
        print(num)

    return c_set

print(sym_diff('2 4 5 9', '2 4 11 12'))