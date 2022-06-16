import sys, collections
from math import inf

shark_x, shark_y = 0, 0
shark_size = 2
eat_count = 0

fish_count = 0
fish_position = []

time = 0

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

n = int(input())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
#2차원 배열 입력받는 코드


#보드의 값을 수정하는
for i in range(n):
    for j in range(n):
        if 0 < board[i][j] <= 6: #물고기 수 및 위치 선정
            fish_count += 1
            fish_position.append((i, j))
        elif board[i][j] == 9:   #상어의 위치
            shark_x, shark_y = i, j #상어의 좌표를 데이터로 넘겨줌

board[shark_x][shark_y] = 0


def bfs(shark_x, shark_y):
    q = collections.deque([(shark_x, shark_y, 0)])
    dist_list = []
    visited = [[False] * n for _ in range(n)]
    visited[shark_x][shark_y] = True
    min_dist = inf
    while q:
        x, y, dist = q.popleft()
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y
            if 0 <= xx < n and 0 <= yy < n and not visited[xx][yy]:
                if board[xx][yy] <= shark_size:
                    visited[xx][yy] = True
                    if 0 < board[xx][yy] < shark_size:
                        min_dist = dist
                        dist_list.append((dist + 1, xx, yy))
                    if dist + 1 <= min_dist:
                        q.append((xx, yy, dist + 1))
    if dist_list: #dist_list가 비면 전체 로직이 멈추는 구조
        print(dist_list)
        print("="*50)
        dist_list.sort()
        print(dist_list)
        return dist_list[0]
    else:
        return False

while fish_count:
    result = bfs(shark_x, shark_y)
    if not result:
        break
    shark_x, shark_y = result[1], result[0]
    time += result[0]

    #fish count
    eat_count += 1
    fish_count -= 1

    if shark_size == eat_count:
        shark_size += 1
        eat_count = 0
    board[shark_x][shark_y] = 0

print(time)
