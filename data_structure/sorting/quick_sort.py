import time
import random

def qsort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        qsort(a, low, pivot - 1)
        qsort(a, pivot + 1, high)

def partition(a, pivot, high):
    i = pivot + 1
    j = high
    while True:
        while i < high and a[i] < a[pivot]:
            i += 1
        while j > pivot and a[j] > a[pivot]:
            j -= 1
        if j <= i:
            break
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    a[pivot], a[j] = a[j], a[pivot]
    return j

if __name__ == "__main__":
    start = 0
    finish = 5000000
    a = []
    for i in range(start, finish):
        a.append(random.randrange(start, finish))

    #print(a)
    start_time = time.time()
    qsort(a, 0, len(a) - 1)

    #print(res)
    print("Time: ", time.time() - start_time)
