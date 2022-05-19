from __future__ import annotations
from typing import TypeVar, Generic, List
from edge import Edge
from graph import Graph
from copy import deepcopy
#import sys
#sys.path.insert(0, '../../../../OneDrive/문서') # so we can access the Chapter2 package in the parent directory

from ch2.generic_search import bfs, Node, node_to_path


V = TypeVar('V')


class Graph_modified(Graph[str], Generic[V]):

    def __init__(self, vertices: List[V] = [], start: str = "", dest: str = "") -> None:
        super().__init__(vertices)
        self.start = start
        self.dest = dest

    def delete_edge_by_vertices(self, first: V, second: V) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.delete_edge_by_indices(u, v)

    def delete_edge_by_indices(self, u: int, v: int) -> None:
        edge: Edge = Edge(u, v)
        self.delete_edge(edge)

    def delete_edge(self, edge: Edge) -> None:
        self._edges[edge.u].remove(edge)
        self._edges[edge.v].remove(edge.reversed())

    def goal_test(self) -> bool:
        return (self.edge_count == 0) and (self.start == self.dest)

    def successors(self) -> List[Graph_modified]:
        sucs: List[Graph_modified] = []
        for edge_to_delete in self._edges[self.index_of(self.start)]:
            sucs.append(deepcopy(self))
            sucs[-1].delete_edge(edge_to_delete)
            sucs[-1].start = self._vertices[edge_to_delete.v]
        return sucs
        

def display_solution(path: List[Graph]):
    if len(path) == 0:
        return
    route = [ipath.start for ipath in path]
    print("-".join(route))


if __name__ == "__main__":
    # 다리 만들기
    Koni_bridge: Graph_modified[str] = \
        Graph_modified(vertices = \
            ["A", "B", "C", "D", "AC1", "AC2", "AB1", "AB2", "E"])
    Koni_bridge.add_edge_by_vertices("A", "AB1")
    Koni_bridge.add_edge_by_vertices("B", "AB1")
    Koni_bridge.add_edge_by_vertices("A", "AB2")
    Koni_bridge.add_edge_by_vertices("B", "AB2")
    Koni_bridge.add_edge_by_vertices("A", "AC1")
    Koni_bridge.add_edge_by_vertices("C", "AC1")
    Koni_bridge.add_edge_by_vertices("A", "AC2")
    Koni_bridge.add_edge_by_vertices("C", "AC2")
    Koni_bridge.add_edge_by_vertices("A", "D")
    Koni_bridge.add_edge_by_vertices("B", "D")
    Koni_bridge.add_edge_by_vertices("C", "D")
    Koni_bridge.add_edge_by_vertices("A", "E")
    Koni_bridge.add_edge_by_vertices("E", "D")

    # test graphs
    # Koni_bridge: Graph_modified[str] = \
    #     Graph_modified(vertices = ["A", "B", "C", "D"])
    # Koni_bridge.add_edge_by_vertices("A", "B")
    # Koni_bridge.add_edge_by_vertices("B", "C")
    # Koni_bridge.add_edge_by_vertices("C", "D")
    # Koni_bridge.add_edge_by_vertices("D", "A")
    # Koni_bridge.add_edge_by_vertices("A", "C")
    # Koni_bridge.start = "A"
    # Koni_bridge.dest = "C"
    
    for start in Koni_bridge._vertices:
        Koni_bridge.start = start
        Koni_bridge.dest = start
        ...
        solution = bfs(Koni_bridge, 
                        Graph_modified.goal_test, 
                        Graph_modified.successors)
        if solution is not None:
            path: List[Graph_modified] = node_to_path(solution)
            display_solution(path)
            break
    else:
        print("No solution found")