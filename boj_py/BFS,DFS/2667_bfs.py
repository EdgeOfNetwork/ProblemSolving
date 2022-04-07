from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
cnt_list = []

def bfs(x, y): #queue를 사용
    count = 0
    queue = deque()
    queue.append((x, y)) #root 좌표 입력
    while queue:
        x, y = queue.popleft()
        if 0 <= x < n and 0 <= y < n and graph[x][y]:
            count += 1
            graph[x][y] = 0 #visited표시
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                queue.append((x + dx, y + dy))
    return count

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt_list.append(bfs(i, j))

print(len(cnt_list))
for cnt in sorted(cnt_list):
    print(cnt)