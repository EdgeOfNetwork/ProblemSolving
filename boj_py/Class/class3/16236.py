import sys, collections
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

print(fish_position)

board[shark_x][shark_y] = 0


def bfs(shark_x, shark_y):
    q = collections.deque([(shark_x, shark_y, 0)])
    dist_list = []
    visited = [[False] * n for _ in range(n)]
    visited[shark_x][shark_y] = True
    min_dist = int(1e9)
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
    if dist_list:
        dist_list.sort()
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



"""
먹이 먹는 로직

아기상어 = 2

if 아기상어 크기 < 물고기 크기 :


# """
# import sys, collections
#
# shark_x, shark_y = 0, 0
# shark_size = 2
# eat_cnt = 0
#
# fish_cnt = 0
# fish_pos = []
#
# time = 0
#
# dx = (1, -1, 0, 0)
# dy = (0, 0, 1, -1)
#
# n = int(sys.stdin.readline())  # NxN 크기의 공간 입력받기.
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]  # 공간의 상태 입력받기.
#
# for i in range(n):
#     for j in range(n):
#         if 0 < board[i][j] <= 6:  # 물고기 수 및 위치 설정
#             fish_cnt += 1
#     fish_pos.append((i, j))
#     elif board[i][j] == 9:  # 아기 상어 위치 설정
#     shark_x, shark_y = i, j
#
# board[shark_x][shark_y] = 0
#
#
# def bfs(shark_x, shark_y):
#     q = collections.deque([shark_x, shark_y, 0)])
#     dist_list = []
#     visited = [[False] * n for _ in range(n)]
#     visited[shark_x][shark_y] = True
#     min_dist = int(1e9)  # int를 무한대로 지정하는 방법 중에 하나.
#
#
# while q:
#     x, y, dist = q.popleft()
#     for i in range(4):
#         xx = dx[i] + x
#     yy = dy[i] + y
#     if 0 <= xx < n and 0 <= yy < n and not visited[xx][yy]:  # (xx, yy) 위치에 물고기가 있고, 아직 방문하지 않았다면
#         if board[xx][yy] <= shark_size:  # (xx,yy) 위치의 물고기가 아기상어보다 작거나 같다면
#             visited[xx][yy] = True  # 아기상어를 (xx,yy) 위치로 이동.
#         if 0 < board[xx][yy] < shark_size:  # (xx,yy) 위치의 물고기 크기가 아기상어보다 작다면
#             min_dist = dist  # 지금까지 상어가 이동한 거리를 min_dist로 설정.
#             dist_list.append((dist + 1, xx, yy))  # 상어가 이동한 거리 및 위치 저장.
#         if dist + 1 <= min_dist:
#             q.append((xx, yy, dist + 1))  # 상어가 다음 턴에 이동할 인접한 좌표 및 최소거리 deque에 추가.
# if dist_list:
#     dist_list.sort()  # dist_list[0]으로 상어가 이동한 총 거리 쉽게 추출하기 위해서 정렬.
#     return dist_list[0]  # 상어가 이동한 총 거리 및 현재 상어 위치 return.
# else:
#     return False
#
# while fish_cnt:
#     result = bfs(shark_x, shark_y)
# if not result:
#     break
# shar_x, shark_y = result[1], result[2]
# time += result[0]
# eat_cnt += 1  # 먹은 물고기 수 카운트하여 상어 크기 측정하깅 위함.
# fish_cnt -= 1  # while문 1번에 물고기 한마리 먹는다.
# if shark_size == eat_cnt:
#     shark_size += 1
#     eat_cnt = 0
# board[shark_x][shark_y] = 0
#
# print(time)