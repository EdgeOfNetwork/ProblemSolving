n, k = map(int, input().split())

A = []
for _ in range(n):
    A.append(int(input()))

A.sort(reverse=True) #큰 단위부터 확인

count = 0
for target in A:
    count += k // target #목표 가격을 최대한 가장 큰 녀석으로 담을 수 있는지 + 거스름돈의 개수를 더해주는 과정
    k %= target         #그 이후에는 이 화폐 단위보다 작아져야 하기 때문에 k를 화폐 단위만큼 쪼개서 update한다

print(count)