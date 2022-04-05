import random
import time

def selection_solting(a): #최솟값을 선택해서 굴리는 정렬방법
    for i in range(0, len(a) - 1): #갯수만큼 전체를 돌림
        min = i
        for j in range(i, len(a)): #전체 배열에서 최소값을 찾음
            if a[min] > a[j]: #선택된 값이, 최소값보다 작으면 (즉 선택값이 최솟값이면)
                min = j      #최솟값 업데이트
        a[i], a[min] = a[min], a[i] #파이썬이라 가능한 방법, 원래는 Temp를 써서 돌려야한다.
    return a

def insert_solting(a):
    for i in range(1, len(a)):
        for j in range(i, 0, -1): #-1은
            if a[ j - 1] > a[j]: #다음 것 보다 이전 것이 더 크다면
                a[j], a[ j - 1 ] = a[ j - 1 ], a[j]
    return a

def shell_solting(a):
    h = 4 #간격, 여기서는  3x+1의 간격(3개씩 뽑겠다) 1, 4, 13 ...중에서 4와 1만 사용
    while h >= 1:
        for i in range(h, len(a)): #h정렬 수행
            j = i
            while j >= h and a[j] < a[j-h]: #각 그룹에 대한 삽입정렬 파트
                a[j], a[j-h] = a[j-h], a[j] #
                j -= h
        h //= 3
        print(a)
    return a



def time_lap(res):
    start_time = time.time()
    #selection_solting(res)
    #insert_solting(res)#속도차이가 왜 월등하지?
    shell_solting(res)
    print("Time: ",time.time() - start_time)

if __name__ == "__main__":
    start = 0
    finish = 5000
    rand_num = []
    for i in range(start, finish):
        rand_num.append(random.randrange(start, finish))

    print("origin:", rand_num)
    time_lap(rand_num)

