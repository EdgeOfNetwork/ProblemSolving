def downheap(i, size):
    while 2 * i <= size:
        k = 2*i
        if k < size and a[k] < a[k+1]:
            k += 1
        if a[i] >= a[k]:
            break
        a[i], a[k] = a[k], a[i]
        i = k

def create_heap(a):
    hsize = len(a) - 1
    for i in reversed(range(1, hsize//2 + 1)):
        downheap(1, hsize)

def heap_sort(a):
    N = len(a) - 1
    for i in range(N):
        a[1], a[N] = a[N], a[1] #루트와 힙의 마지막 항목 교환
        N -= 1 #힙크기 1 감소

