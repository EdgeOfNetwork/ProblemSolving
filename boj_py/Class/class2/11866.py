from collections import deque
n, k = map(int, input().split())

pipe = deque()
answer = []

for i in range(1, n + 1):
    pipe.append(i)

while pipe: #파이프 내에 요소 체크
    for i in range(k - 1): #3개면 2개를 다른 파이프로 보내고
        pipe.append(pipe.popleft())
    answer.append(pipe.popleft())

print("<", end="")
for i in range(len(answer) - 1):
    print("%d, "%answer[i], end="")
print(answer[-1], end="")
print(">")