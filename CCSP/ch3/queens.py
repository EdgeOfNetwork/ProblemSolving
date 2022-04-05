from csp import Constraint, CSP
from typing import Dict, List, Optional

class QueenConstraint(Constraint[int, int]):
    def __init__(self, columns:List[int]) -> None:
        super().__init__(columns)
        self.columns:List[int] = columns

    def satisfied(self, assignment:Dict[int, int]) -> bool:
        # q1c 퀸1열 q1r 퀸1행
        for q1c, q1r in assignment.items():
            for q2c in range(q1c + 1, len(self.columns) + 1):
                if q2c in assignment:
                    q2r: int = assignment[q2c]
                    if q1r == q2r:
                        return False
                    if abs(q1r - q2r) == abs(q1c - q2c):
                        return False
        return True #충돌 없음


if __name__ == "__main__":
    columns: List[int] = [1,2,3,4,5,6,7,8]

    rows : Dict[int, List[int]] = {}
    for column in columns:
        rows[column] = [1,2,3,4,5,6,7,8]
    # 체스 판 드로잉

    csp: CSP[int, int] = CSP(columns, rows)

    csp.add_constraint(QueenConstraint(columns))

    solution: Optional[Dict[int, int]] = csp.backtracking_search()
    if solution is None:
        print("답을 찾을 수 없습니다")
    else:
        print(solution)