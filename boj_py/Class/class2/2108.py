import math
n = int(input())

A = []
for _ in range(n):
    A.append(int(input()))

#산술평균 출력
sum = 0
for i in A:
    sum += i

print(int(round(sum/len(A), 0)))

sorted_A = sorted(A)

#중앙값
if len(sorted_A) % 2 == 0 : #짝수라면 14라면 7과 8 사이란건데
    median_mean = sorted_A[len(sorted_A) // 2] + sorted_A[len(sorted_A)]
    print(median_mean)
else:
    median_mean = sorted_A[math.ceil(len(sorted_A) // 2)]
    print(median_mean)


#최빈값

set_A = sorted(set(sorted_A)) #요소가 있는지 확인
count = [0] * len(set_A)

for i in range(len(sorted_A)):
    if sorted_A[i] in set_A: #요소가 안에 있으면 set_A와 count가 일치하는 index를 올려야한다
        count[]




#범위
print(max(sorted_A) - min(sorted_A))