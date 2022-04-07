n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
cnt_list = []

def dfs(x, y): #스택의 원리로 재귀적 풀이
    count = 0
    if 0 <= x < n and 0 <= y < n and graph[x][y]:
        count += 1
        graph[x][y] = 0
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            count += dfs(x + dx, y + dy)
    return count

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt_list.append(dfs(i,j))

print(len(cnt_list))
for cnt in sorted(cnt_list):
    print(cnt)

