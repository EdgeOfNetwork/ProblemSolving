from __future__ import annotations
from typing import TypeVar, Generic, List, Tuple, Callable
from enum import Enum
from random import choices, random
from heapq import nlargest
from statistics import mean
from chromosome import Chromosome


C = TypeVar('C', bound=Chromosome)


class GeneticAlgorithm(Generic[C]): #크로모좀을 바인딩한 제네릭 형태를 input으로하겠다.
    SelectionType = Enum("SelectionType", "ROULETTE TOURNAMENT") #룰렛휠 선택 / 토너먼트

    def __init__(self, initial_population: List[C], threshold: float
                 , max_generations: int = 100, mutation_chance: float = 0.01
                 , crossover_chance: float=0.7, selection_type:SelectionType = SelectionType.TOURNAMENT):
        self._population: List[C] = initial_population #1세대 알고리즘의 염색체
        self._threshold: float = threshold              #솔루션이 발견되었음을 나타내는 적합도 수준
        self._max_generations: int = max_generations    #실행할 최대 세대 수
        self._mutation_chance: float = mutation_chance #많은 세대를 실행하여 임곗값을 초과하는 적합도 수준의 솔루션이 발견되지 않으면 발견된 최고의 솔루션을 반환
        self._crossover_chance: float = crossover_chance      #두 부모 염색체가 재생산할떄 자식 염색체에 그들의 유전자가 섞일 확률
        self._selection_type: GeneticAlgorithm.SelectionType = selection_type #유전 알고리즘의 처리 방법 결정
        self._fitness_key: Callable = type(self._population[0]).fitness


    # 두 부모를 선택하기 위해 룰렛휠을 사용
    # 메모 : 음수 적합도와 작동하지 않음
    def _pick_roulette(self, wheel: List[float]) -> Tuple[C, C]:
        return tuple(choices(self._population, weights=wheel, k = 2))

    def _pick_tournament(self, num_participants: int) -> Tuple[C, C]:
        participants: List[C] = choices(self._population, k=num_participants)
        return tuple(nlargest(2, participants, key=self._fitness_key))

    #집단을 새로운 세대로 교체
    def _reproduce_and_replace(self) -> None:
        new_population: List[C] = []
        #새로운 세대가 채워질때까지 반복
        while len(new_population) < len(self._population):
            #Parent  중 두 부모를 선택
            if self._selection_type == GeneticAlgorithm.SelectionType.ROULETTE:
                parents: Tuple[C, C] = self._pick_roulette(
                    [x.fitness() for x in self._population]
                )
            else:
                parents = self._pick_tournament(len(self._population) // 2)
            # 두 부모의 크로스오버
            if random() < self._crossover_chance:
                new_population.extend(parents[0].crossover(parents[1]))
            else:
                new_population.extend(parents)
        #새 집단의 수가 홀수라면 이전 집단보다 하나 더 많으므로 제거
        if len(new_population) > len(self._population):
            new_population.pop()
        self._population = new_population #새 집단으로 참조를 변경

    # mutation chance 확률로 각 개별 염색체를 돌연변이한다.
    def _mutate(self) -> None:
        for individual in self._population:
            if random() < self._mutation_chance:
                individual.mutate()

    # max_generations 만큼 유전 알고리즘을 실행, 최상의 적합도를 가진 개체를 반환
    def run(self) -> C:
        best: C = max(self._population, key = self._fitness_key)
        for generation in range(self._max_generations):
            #임곗값을 초과하면 개체를 바로 반환
            if best.fitness() >= self._threshold:
                return best
            print(f"세대 {generation} 최상 {best.fitness()} 평균 {mean(map(self._fitness_key, self._population))}")
            self._reproduce_and_replace()
            self._mutate()
            highest: C = max(self._population, key= self._fitness_key)
            if highest.fitness() > best.fitness():
                best = highest

        return best