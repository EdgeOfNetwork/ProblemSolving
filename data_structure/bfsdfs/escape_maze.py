from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))



def bfs(x, y):
    queue = deque()
    queue.append((x, y)) #root 지정
    while queue:
        x, y = queue.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            if 0 <= x + dx < n and 0 <= y + dy < m and graph[x + dx][y + dy] == 1:
                graph[x + dx][y + dy] = graph[x][y] + 1
                queue.append((x + dx, y + dy))
    return graph[n - 1][m - 1]
#최단경로 뽑기

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]


# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i] #일단 이동을 한거잖아
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#             if graph[nx][ny] == 0:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y] + 1
#                 queue.append((nx, ny))
#     return graph[n - 1][m - 1]

print(bfs(0, 0))

"""
예시

5 6
101010
111111
000001
111111
111111
"""