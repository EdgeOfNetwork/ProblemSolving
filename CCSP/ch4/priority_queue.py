from typing import TypeVar, Generic, List
from heapq import heappush, heappop

T = TypeVar('T')

"""
TODO : 이걸 heapq 없이 구현해볼 수 있을까?
"""

class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container #컨테이너가 비었다면 false가 아님

    def push(self, item: T) -> None:
        heappush(self._container, item) #우선순위 push

    def pop(self) -> T:
        return heappop(self._container) #우선순위 pop

    def __repr__(self) -> str:
        return repr(self._container)