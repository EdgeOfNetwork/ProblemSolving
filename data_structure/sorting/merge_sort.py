import time
import random


def merge(a, b, low, mid, high):
    i = low
    j = mid + 1
    for k in range(low, high + 1): #a의 앞/뒷부분을 합병하여 b에 저장
        if i > mid:
            b[k] = a[j] #a의 앞부분이 먼저 소진되었을 시 뒷부분을 b로 복사
            j += 1
        elif j > high:
            b[k] = a[i]
            i += 1
        elif a[j] < a[i]:
            b[k] = a[j]
            j += 1
        else:
            b[k] = a[i]
            i += 1
    for k in range(low, high + 1):
        a[k] = b[k]

def merge_sort(a, b, low, high):
    if high <= low: return
    mid = low + (high - low) // 2
    merge_sort(a, b, low, mid)
    merge_sort(a, b, mid + 1, high)
    merge(a, b, low, mid, high)

if __name__ == "__main__":
    start = 0
    finish = 5000000
    a = []
    for i in range(start, finish):
        a.append(random.randrange(start, finish))

    #print(a)
    start_time = time.time()

    b = [None] * len(a) #보조 리스트?

    merge_sort(a, b, 0, len(a) - 1)
    #print(a)
    print("Time: ", time.time() - start_time)