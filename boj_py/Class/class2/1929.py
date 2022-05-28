n = int(input())
A = list(map(int, input().split()))
cnt = 0


for num in A: # 5
    error = 0
    if num > 1: # 0과 1을 제거하는 로직
        for i in range(2, num): #그치 다 볼필요는 없지
            if num % i == 0:    #완탐
                error += 1 #에러 없이 풀수는 없을까?
        if error == 0:
            cnt += 1

print(cnt)

