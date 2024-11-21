if __name__ == '__main__':
    n = int(input())
    arr = list(set(list(map(int, input().split(' ')))))
    arr = sorted(arr)

    print(arr[-2])