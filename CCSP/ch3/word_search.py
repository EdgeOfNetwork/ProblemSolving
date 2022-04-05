from typing import NamedTuple, List, Dict, Optional
from random import choice
from string import ascii_uppercase
from csp import CSP, Constraint

Grid = List[List[str]]

class GridLocation(NamedTuple):
    row : int
    column : int

def generate_grid(rows: int, columns: int) -> Grid:
    return [[choice(ascii_uppercase) for c in range(columns)] for r in range(rows)]

def display_grid(grid: Grid) -> None:
    for row in grid:
        print("".join(row))

def generate_domain(word: str, grid:Grid) ->List[List[GridLocation]]:
    domain: List[List[GridLocation]] = []
    height: int = len(grid)
    width: int = len(grid[0])
    length: int = len(word)
    for row in range(height):
        for col in range(width):
            columns: range = range(col, col + length + 1)
            rows: range = range(row, row + length + 1)
            if col + length <= width:
                domain.append([GridLocation(row, c) for c in columns])
                if row + length <= height:
                    domain.append([GridLocation(r, col + (r - row)) for r in rows])
            if row + length <= height:
            #위에서 아래로
                domain.append([GridLocation(r, col) for r in rows])
                if col - length >= 0:
                    domain.append([GridLocation(r, col - (r - row)) for r in rows])
    return domain

class WordSearchConstraint(Constraint[str, List[GridLocation]]):
    def __init__(self, words: List[str]) -> None:
        super().__init__(words)
        self.words: List[str] = words

    def satisfied(self, assignment: Dict[str, List[GridLocation]]) -> bool:
        #all_locations = [locs for values in assignment.values() for locs in values]
        for values in assignment.values():
            for locs in values:
                all_locations = locs
        print(all_locations)
        return len(set(all_locations)) == len(all_locations) # 중복제거는 왜?

    #satisfied는 True // False를 뱉는다.

"""
HW1 : 중복단어 허용하는 단어 검색 구현 
"""


if __name__ == "__main__":
    grid: Grid = generate_grid(9, 9)
    words: List[str] = ["MATTHEW", "JOE", "MARY", "SARAH", "SALLY"]
    locations: Dict[str, List[List[GridLocation]]] = {}
    for word in words:
        locations[word] = generate_domain(word, grid)
    csp: CSP[str, List[GridLocation]] = CSP(words, locations) # V ,D : 모든 변수에 도메인이 할당 된 상태
    csp.add_constraint(WordSearchConstraint(words))
    solution: Optional[Dict[str, List[GridLocation]]] = csp.backtracking_search()
    if solution is None:
        print("답을 찾을 수 없습니다.")
    else:
        for word, grid_locations in solution.items():
            if choice([True, False]):
                grid_locations.reverse()
            for index, letter in enumerate(word):
                (row, col) = (grid_locations[index].row, grid_locations[index].column)
                grid[row][col] = letter
        display_grid(grid)


"""
TODO : 결과에서 정답이 어디있는지를 보여주는 show_result도 구현해보자
"""