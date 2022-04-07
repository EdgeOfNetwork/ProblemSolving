from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


def bfs(x, y):
    queue = deque()
    queue.append((x,y)) #root 지정
    while queue:
        x, y = queue.popleft()
        if 0 <= x < n and 0 <= y < m and graph[x][y] != 0:
            graph[x][y] = 0 #이미 간 곳은 1 표시로 visited
            for dx, dy in (-1,0), (1,0),(0,-1),(0,1):
                if graph[x + dx][y + dy] == 1:
                    graph[x + dx][y + dy] = graph[x][y] + 1
                    queue.append((x + dx, y + dy))
    return graph[n - 1][m - 1]
#최단경로 뽑기

print(bfs(0,0))
