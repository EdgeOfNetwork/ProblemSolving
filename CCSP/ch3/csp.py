from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

V = TypeVar('V') #변수 타입
D = TypeVar('D') #도메인 타입

class Constraint(Generic[V, D], ABC): #모든 제약 조건에 대한 베이스 클래스
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

        @abstractmethod
        def satisfied(self, assignment: Dict[V, D]) -> bool:
            ...

class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]])-> None:
        self.variables: List[V] = variables #제약조건을 확인할 수 있는 변수
        self.domains: Dict[V, List[D]] = domains
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("모든 변수에 도메인이 할당되어야 합니다.")

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("제약 조건 변수가 아닙니다.")
            else:
                self.constraints[variable].append(constraint)

    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        if len(assignment) == len(self.variables): return assignment
        unassigned: List[V] = [v for v in self.variables if v not in assignment]
        print(unassigned)
        first: V = unassigned[0] #이게 문젠데
        for value in self.domains[first]:
            local_assignment = assignment.copy() # 왜 copy를 썼다그랬지?
            local_assignment[first] = value
            if self.consistent(first, local_assignment):
                print(self.consistent(first, local_assignment)) #중복 빼고 OK를 내뱉음
                result: Optional[Dict[V, D]] = self.backtracking_search(local_assignment) # 재귀적 접근?
                if result is not None:
                    return result
        return None # 솔루션 없는 경우


