from __future__ import annotations
from typing import NewType, List
from abc import ABC, abstractmethod

Move = NewType('Move', int) #게임에서 이동을 나타내는 타입

class Piece: #게임보드의 말에 대한 기본 클래스 / 2개의 턴을 표시한다?
    @property
    def opposite(self) -> Piece:
        raise NotImplementedError('서브 클래스로 구현해야 합니다') #1. 서브클래스의 정의?

class Board(ABC):
    @property
    @abstractmethod
    def turn(self) -> Piece:
        ...

    @abstractmethod
    def move(self, location: Move) -> Board:
        ...

    @property
    @abstractmethod
    def legal_moves(self) -> List[Move]:
        ...

    @property
    @abstractmethod
    def is_win(self) -> bool:
        ...

    @property
    def is_draw(self) -> bool:
        return (not self.is_win) and (len(self.legal_moves) == 0)

    @abstractmethod
    def evaluate(self, player: Piece) -> float:
        ...