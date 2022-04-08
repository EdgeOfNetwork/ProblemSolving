from collections import deque
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    cnt = 0
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        if 0 <= x < n and 0 <= y < m and graph[x][y]:
            cnt += 1
            graph[x][y] = 0 #visited 의 역할
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                queue.append((x + dx, y + dy)) #주변에 있는 친구 전
    return graph[x-1][y-1]

cnt_list = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            print(bfs(i,j))
#            cnt_list.append(bfs(i,j))

# cnt_list.sort()
# print(cnt_list)
# print(cnt_list[0])