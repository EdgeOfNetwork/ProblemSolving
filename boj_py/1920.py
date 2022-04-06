def qsort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        qsort(a, low, pivot - 1)
        qsort(a, pivot + 1, high)
    return a

def partition(a, pivot, high): #low가 피벗으로 들어갔네?
    i = pivot + 1 #왜 low에 +1을 할까
    j = high
    while True:
        while i < high and a[i] < a[pivot]:
            i += 1
        while j > pivot and a[j] > a[pivot]:
            pass


if __name__ == "__main__":
    N = int(input())
    li = []

    for i in range(N):
        li.append(int(input()))
    qsort(li)


