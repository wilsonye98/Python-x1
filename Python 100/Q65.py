# Please write assert statements to verify that
# every number in the list [2,4,6,8] is even.

lst = [2,4,6,8]

for item in lst:
    assert item % 2 == 0, "Item is not even"
