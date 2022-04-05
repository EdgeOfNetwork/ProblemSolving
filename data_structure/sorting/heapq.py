import heapq
import time
import random


if __name__ == "__main__":
    start = 0
    finish = 5000000
    a = []
    for i in range(start, finish):
        a.append(random.randrange(start, finish))

    #print(a)
    start_time = time.time()
    heapq.heapify(a)
    #print(a)

    res = []
    while a:
        res.append(heapq.heappop((a)))

    #print(res)
    print("Time: ", time.time() - start_time)
