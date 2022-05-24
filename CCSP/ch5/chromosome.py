from __future__ import annotations #future -> python 2와 3을 함께쓰는 패키지
from typing import TypeVar, Tuple, Type #-> typing 패키지는 뭘까
from abc import ABC, abstractmethod

T = TypeVar('T', bound='Chromosome') #type에 맞지않는 데이터가 드가면 warning을 띄워준다.
#자신을 반환한다??
#TypeVar 클래스 T가 Chromosome 클래스와 바인딩되어 있음
#타입 T인 변수는 크로모좀 클래스의 인스턴스 혹은 서브클래스여야함.

#서브클래스??

#모든 염색체의 베이스 클래스, 모든 메서드는 오버라이드 됨
class Chromosome(ABC): #추상 클래스 상속
    @abstractmethod #추상 메서드의 용도란?
    def fitness(self) -> float: #염색체가 문제를 얼마나 잘 해결하는지
        ...

    @classmethod
    @abstractmethod
    def random_instance(cls : Type[T]) -> T:
        ...

    @abstractmethod
    def crossover(self: T, other:T) -> Tuple[T, T]: # 세대마다 염색체의 유전자가 (무작위로) 변이될 가능성 존재
        ...

    @abstractmethod
    def mutate(self) -> None:
        ...

"""
도형 아래 
삼각형, 사각형, 원 등이 있다.

도형이라는 추상클래스가 있다면 도형에는 
꼭지점세기, 색깔입히기 등 모든 도형을 아우르는 메서드들을 넣을 수 있겠다.
즉, 하나의 개념에 대해 "추상적인 개념들을 집어넣는 상대적 윗 개념의 클래스를 선언하여
공통분모를 만드는 것이라 볼 수 있겠다.

"""

