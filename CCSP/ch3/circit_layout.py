"""
HW2 : 회로판 레이아웃 문제 해결
"""

from typing import NamedTuple, List, Dict, Optional
from random import choice
from string import ascii_uppercase
from csp import CSP, Constraint


Grid = List[List[str]] #str로 해놓고 블록 구분을 AAAA BBBB로 할까?

class GridLocation(NamedTuple):
    row : int
    column : int

#def generate_grid(rows: int, columns: int) -> Grid:
#    return

def generate_domain():
    pass

class CircitSearchConstraint(Constraint[str, List[GridLocation]]):
    def __init__(self) -> None:



if __name__ == "__main__":
    columns: List[int] = [1,2,3,4,5,6,7,8,9]


    rows : Dict[int, List[int]] = {}
    for column in columns:
        rows[column] = [1,2,3,4,5,6,7,8,9]
    # 체스 판 드로잉
    csp : CSP[int, int] = CSP(columns, rows) #맞나?

    blocks: List[List[List[str]]] = [
        [['A', 'A', 'A', 'A'], ['A', 'A', 'A', 'A'], ['A', 'A', 'A', 'A'], ['A', 'A', 'A', 'A']],
        [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']],
        [['C'], ['C'], ['C'], ['C'], ['C'], ['C'], ['C']],
        [['D', 'D'], ['D', 'D'], ['D', 'D'], ['D', 'D']],
    ]

    csp.add_constraint(CircitSearchConstraint(blocks))

    solution: Optional[Dick[]]