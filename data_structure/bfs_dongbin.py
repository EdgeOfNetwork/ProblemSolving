graph = [[] for _ in range(3)]
print(graph)

#노드 0에 연결된 정보 저장
graph[0].append((1, 7))
print(graph)
graph[0].append((2, 5))
print(graph)
graph[0].append((3,3))
print(graph)
graph[0].pop()
print(graph)
#스택처럼 사용 가능

print(graph[0][0])

#노드 1에 연결된 노드 정보 저장
graph[1].append((0, 7))
print(graph)

graph[2].append((0, 5))
print(graph)