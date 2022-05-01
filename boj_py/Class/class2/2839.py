n = int(input())
#반례가 뭘까?
cnt = 0
while True:
    if n >= 5 and n % 5 == 0:
        n -= 5
        cnt += 1
    elif n >= 3:
        n -= 3
        cnt += 1
    elif n < 3:
        if n == 0:
            print(cnt)
            break
        else:
            print(-1)
            break


# n = int(input())
#
# cnt = 0
# while n >= 0 :
#     if n % 5 == 0:
#         cnt += (n // 5)
#         print(cnt)
#         break
#     n -= 3
#     cnt += 1
# else:
#     print(-1)

