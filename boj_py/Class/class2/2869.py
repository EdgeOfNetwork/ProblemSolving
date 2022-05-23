a, b, v = map(int, input().split())
import math

day = (v - b) / (a - b)
print(math.ceil(day))
# sum = 0
# cnt = 0
#
# while 1: # 시간초과 흠, 어떻게 접근해야할까?
#     sum += a
#     cnt += 1
#     if sum >= v :
#         print(cnt)
#         break
#     sum -= b


