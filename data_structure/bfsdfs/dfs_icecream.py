n, m = map(int, input().split()) #행, 렬

#2차원 리스트 맵 입력 정보 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    #주어진 범위를 벗어나면 종료
    if x <= -1 or x >= n or y <= -1 or y>= m: # 0이상 n 이하
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1 #방문처리
        dfs(x - 1, y) #상
        dfs(x, y - 1) #하
        dfs(x + 1, y) #좌
        dfs(x , y + 1)#우 다 체크해서 범위까지 검색했다면
        return True
    return False

cnt = 0
for i in range(n): #행의 개수 만큼
    for j in range(m):
        if dfs(i, j) == True:
            cnt += 1

print(cnt)