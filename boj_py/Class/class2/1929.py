m, n = map(int, input().split())

# for i in range(m, n + 1):
#     if 1 == i:
#         continue
#     for j in range(2, int(i ** 0.5) + 1):#다 검사할 필요가 없다.
#         if i % j == 0:
#             break
#     else:
#         print(i)


for i in range(m, n + 1):
    if 1 > i:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        print(i)


