from collections import deque

dx = [0, 0, 1, -1] #이유는?
dy = [1, -1, 0, 0]

def bfs(graph, a ,b):
    n = len(graph)
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i range(4):
            nx = 


n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph,i ,j)) #