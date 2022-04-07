n = int(input())
graph = []

block_cnt = 0
for _ in range(n):
    graph.append(list(map(int, input())))

cnt_list = []


def dfs(x, y):
    global block_cnt
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False, _
    if graph[x][y] == 1:
        graph[x][y] = 0  # 방문하면 cnt를 올린다
        dfs(x - 1, y)  # 좌를 다 돌아
        dfs(x, y - 1)  # 우 다 돌아
        dfs(x + 1, y)  # 상 다 돌아
        dfs(x, y + 1)  # 하 다 돌아 아... 조건이구나
        block_cnt += 1
        return True, block_cnt
    return False, _


cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            flag, block_cnt = dfs(i, j)
            cnt_list.append(block_cnt)
            block_cnt = 0
            if flag is True:
                cnt += 1
cnt_list.sort()

"""
a.sort() 객체에 반환까지 해줌
sorted(a) 메서드 사용만 하고 객체에 적용은 한함
"""
print(cnt)
for i in range(cnt):
    print(cnt_list[i])
