from __future__ import annotations
from typing import TypeVar, Generic, List, Tuple, Callable
from enum import Enum
from random import choices, random
from heapq import nlargest
from statistics import mean
from chromosome import Chromosome


C = TypeVar('C', bound=Chromosome)


class GeneticAlgorithm(Generic[C]): #크로모좀을 바인딩한 제네릭 형태를 input으로하겠다.
    SelectionType = Enum("SelectionType", "ROULETTE TOURNAMENT")

    def __init__(self, initial_population: List[C], threshold: float
                 , max_generations: int = 100, mutation_chance: float = 0.01
                 , croessover_chance: float=0.7, selection_type:SelectionType = SelectionType.TOURNAMENT):

