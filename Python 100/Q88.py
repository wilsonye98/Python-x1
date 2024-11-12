# With a given list [12,24,35,24,88,120,155,88,120,155], write a
# program to print this list after removing all duplicate values
# with original order reserved.

def remove_dupe(array):
    flst = []
    for item in array:
        item_count = 0
        for subitem in array:
            if subitem == item:
                item_count += 1
        if item_count == 1:
            flst.append(item)
    flst.reverse()
    return flst

print(remove_dupe([12,24,35,24,88,120,155,88,120,155]))