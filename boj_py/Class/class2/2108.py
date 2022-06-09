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
counts = dict()
for i in range(1, n + 1):
    counts[i] = []

print(counts)
max_count = 1
count = 1

for j in range(1, n):
    if sorted_A[j] == sorted_A[j - 1]: #sort가 되어있다는 전제가 있기때문에 자신있게 이렇게 푼 것
        count += 1
    else:
        counts[count].append(sorted_A[j - 1]) #연속성이 끊기면, 즉, [1,1,1,2] 에서 1에서 2로 넘어간다면
        if max_count < count:
            max_count = count
        count = 1
    if j == n - 1:
        counts[count].append(sorted_A[j])
        if max_count < count : max_count = count

if n == 1:
    counts[1].append(sorted_A[0])

counts[max_count].sort()
if len(counts[max_count]) == 1:
    print(counts[max_count][0])
else:
    print(counts[max_count][1])

#범위
print(max(sorted_A) - min(sorted_A))