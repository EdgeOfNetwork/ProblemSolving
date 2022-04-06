import sys

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None

n = int(input())
card = list(map(int, sys.stdin.readline().split()))
sorted(card)

m = int(input())
check = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    if binary_search(card, check[i], 0, n - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')