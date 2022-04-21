n, m = map(int, input().split())
A = list(map(int, input().split()))

for i in A:
    if i < m:
        print(i, end=' ')