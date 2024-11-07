# Please write a binary search function which searches an item in a
# sorted list. The function should return the index of element to be
# searched in the list.

def find_item(lst, item):
    if item in lst:
        return lst.index(item)
    return False


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = round((low + high) / 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
    return None

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(my_list, 8))

print(13 // 2)
