import time

start = time.time()  # 시작 시간 저장
# a, b = map(int, input().split())
# print(a - b)
# #3.7초

a, b = input().split()
print(int(a) - int(b))
#2초
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간