n = list(map(int, input().split()))

res = 0
for i in n:
    res += pow(i, 2)

res = res % 10

print(res)