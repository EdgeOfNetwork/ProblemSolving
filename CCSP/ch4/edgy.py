from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Edge:
    u: int #정점 u에서 from
    v: int #정점 v로
    def reversed(self) -> Edge:
        return Edge(self, v, self.u)

    def __str__(self) -> str:
        return f"{self.u} -> {self.v}"
