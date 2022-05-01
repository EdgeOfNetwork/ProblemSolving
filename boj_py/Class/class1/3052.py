counting = [0] * 42

for i in range(10):
    n = int(input()) % 42
    counting[n] += 1 #카운팅을 해주고

cnt = 0
for i in counting:#0이 아니면 뭔가 존재한다는 거니까
    if i != 0:
        cnt += 1

print(cnt)