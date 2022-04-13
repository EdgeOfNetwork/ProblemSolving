from typing import TypeVar, Generic, List, Optional
from edge import Edge

V = TypeVar('V')

class Graph(Generic[V]):
    def __init__(self, vertices:List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices]

    @property
    def vertex_count(self) -> int:
        return len(self._vertices) #정점의 수

    @property
    def edge_count(self) -> int:
        return sum(map(len, self._edges)) #엣지 수

    def add_vertex(self, vertex: V) -> int: #그래프에 정점을 추가하고 인덱스를 반환
        self._vertex.append(vertex)
        self._edges.append([]) #엣지에 빈 리스트를 추가
        return self.vertex_count #추가된 정점의 인덱스 반환

    def add_edge(self, edge: Edge) -> None: #무향 그래프이므로 항상 양반향으로 엣지 추가
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    def add_edge_by_indices(self, u: int, v:int) -> None:
        edge: Edge = Edge(u, v)
        self.add_edge(edge)

    def add_edge_by_vertices(self, first : V, second : V) -> None:
        u : int = self._vertices.index(first)
        v : int = self._vertices.index(second)
        self.add_edge_by_indices(u, v)

    def vertex_at(self, index: int) -> V:
        return self._vertices[index]

    def index_of(self, vertex: V) -> int: #정점 인덱스를 찾는다.
        return self._vertices.index(vertex)

    def neighbors_for_index(self, index: int) -> List[V]:
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    def neighbors_for_vertex(self, vertex: V) -> List[V]:
        return self.neighbors_for_index(self.index_of(vertex))

    def edges_for_index(self, index: int) -> List[Edge]:
        return self._edges[index]

    def edges_for_vertex(self, vertex: V) -> List[Edge]:
        return self.edges_for_index(self.index_of(vertex))

    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)\n"
            return desc

