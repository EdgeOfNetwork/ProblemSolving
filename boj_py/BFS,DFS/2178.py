from collections import deque

n, m = map(int, input().split())


graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for dx, dy in (-1,0), (1,0), (0, -1), (0, 1):
            if 0 <= x + dx < n and 0 <= y + dy < m and graph[x + dx][y + dy] == 1:
                graph[x + dx][y + dy] = graph[x][y] + 1
                queue.append((x + dx, y + dy))
    return graph[n - 1][m - 1]

print(bfs(0,0))
