import math
n = int(input())

A = []
for _ in range(n):
    A.append(int(input()))

#산술평균 출력
sum = 0
for i in A:
    sum += i

print(float(sum/len(A), 2))

sorted_A = sorted(A)

#중앙값
if sorted_A % 2 == 0 : #짝수라면 14라면 7과 8 사이란건데
    median_mean = sorted_A[len(sorted_A) // 2] + sorted_A[len(sorted_A)]
    print(median_mean)
else:
    median_mean = sorted_A[math.ceil(len(sorted_A) // 2)]
    print(median_mean)


#최빈값

count = [0] * n
set_A = set(sorted_A)
for i in set_A:
    if i in sorted_A:
        count


for


#범위
print(max(sorted_A) - min(sorted_A))