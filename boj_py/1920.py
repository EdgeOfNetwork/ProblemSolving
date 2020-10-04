def binary_search(array, value, low, high):
    if low > high : return False

    mid = (low + high) // 2
    if array[mid] > value:
        return binary_search(array, value, low, mid-1)
    elif array[mid] < value:
        return binary_search(array, value, mid + 1, high)
    else:
        return True


N = int(input())
A = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))
A = sorted(A)

for m in M_list:
    if binary_search(A, m, 0, N-1):
        print(1)
    else:
        print(0)



#수정
