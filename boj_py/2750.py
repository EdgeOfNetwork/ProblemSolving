def quick_sort(arr, low, high): #low, high 번째
    if low <= high:#다 돌았냐
        pivot = partition(arr, low, high) #피벗 업데이트
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] #교환??
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# def partition(arr, low, high):
#     pivot = arr[high] #가장 높은 값
#     i = low - 1 #첫번째 요소 세팅
#     for j in range(low, high):
#         if arr[j] <= pivot: # arr[j]가 가장 큰 이하면
#             i += 1 #첫번째 값 이후 계속
#             arr[]


N = int(input())
M = []

for i in range(N):
    M.append(int(input()))

M = quick_sort(M, 0, len(M) - 1) #0부터 카운트가 시작하니까 -1이다

for i in range(len(M)):
    print(M[i])


