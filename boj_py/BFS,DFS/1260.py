from collections import deque

def dfs(graph, root):
    visited =[]
    stack = [root] #start

    while stack:
        n = stack.pop()
        print(n)
        print(type(n))
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited)) #set으로 중복을 제거한다
                temp.sort(reverse=True)
                stack += temp
    return " ".join(str(i) for i in visited)

def bfs(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp
    return " ".join(str(i) for i in visited)


graph = {}
n = input().split(' ')
node, edge, start = [int(i) for i in n] #문제 조건
for i in range(edge): #그래프 생성
    edge_info = input().split(' ')
    n1, n2 = [int(j) for j in edge_info] #n1에서 n2
    if n1 not in graph:
        graph[n1] = [n2] #머지
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

print(dfs(graph, start))
print(bfs(graph, start))

# dict = {1:2, 2:3, 3:4}
# print(dict[1]) # 2가 나옴
