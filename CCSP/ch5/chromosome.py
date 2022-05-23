from __future__ import annotations #future -> python 2와 3을 함께쓰는 패키지
from typing import TypeVar, Tuple, Type #-> typing 패키지는 뭘까
from abc import ABC, abstractmethod

T = TypeVar('T', bound='Chromosome') #type에 맞지않는 데이터가 드가면 warning을 띄워준다.
#TypeVar 클래스 T가 Chromosome 클래스와 바인딩되어 있음
#타입 T인 변수는 크로모좀 클래스의 인스턴스 혹은 서브클래스여야함.

#서브클래스??

#모든 염색체의 베이스 클래스, 모든 메서드는 오버라이드 됨
class Chromosome(ABC):
    @abstractmethod #추상 메서드의 용도란?
    def fitness(self) -> float:
        ...

    @classmethod
    @abstractmethod
    def random_instance(cls : Type[T]) -> T:
        ...

    @abstractmethod
    def crossover(self: T, other:T) -> Tuple[T, T]:
        ...

    @abstractmethod
    def mutate(self) -> None:
        ...

