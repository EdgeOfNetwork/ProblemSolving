from collections import deque

n, m = map(int, input().split())
MAX = 10 ** 6
visited = [0] * (MAX + 1)


def bfs(start, end):
    queue = deque()
    queue.append(start)
    while queue:
        x = queue.popleft()
        if x == end:
            print(visited[x])
            break
        for dx in (x - 1), (x + 1), (2 * x):
            if 0 <= dx < MAX and not visited[dx]:
                visited[dx] = visited[x] + 1
                queue.append(dx)
bfs(n, m)