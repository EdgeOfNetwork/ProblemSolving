def quick_sort(arr, low, high):
    if low <= high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

N = int(input())
M = []

for i in range(N):
    M.append(int(input()))

quick_sort(M, 0, len(M) - 1)

for i in range(len(M)):
    print(M[i])


