from __future__ import annotations
from typing import Iterator, Tuple, List, Iterable
from math import sqrt


class DataPoint: #공동 인터페이스 정의
    def __init__(self, initial: Iterable[float]) -> None:
        self._originals: Tuple[float, ...] = tuple(initial)
        self.dimensions: Tuple[float, ...] = tuple(initial)

    @property
    def num_dimensions(self) -> int:
        return len(self.dimensions)

    def distance(self, other: DataPoint) -> float:
        combined: Iterator[Tuple[float, float]] = zip(self.dimensions, other.dimensions) #뭐랑 뭐를 묶는거지
        differences: List[float] = [(x - y) ** 2 for x, y in combined] #각 차원의 각 점과 해당 제곱값 간의 차이를 찾음
        return sqrt(sum(differences))

    def __eq__(self, other: object) -> bool: #모든 데이터 포인트는 다른 데이터 포인트와 비교할 수 있어야 한다.
        if not isinstance(other, DataPoint):
            return NotImplemented

    def __repr__(self) -> str:              #디버깅 출력을 위해 사람이 읽을 수 있도록 하는 메서드
        return self._originals.__repr__()