from typing import Tuple, List, Callable
import math
import heapq


matrix = [
    [True, True, True, False, False, False, False],
    [True, False, True, False, False, False, False],
    [True, False, True, True, True, True, True],
    [True, False, True, False, False, False, True],
    [True, False, True, False, True, True, True],
    [True, False, True, False, True, False, False],
    [True, True, True, True, True, True, True],
]


Coord = Tuple[int, int]

start = (2, 2)
dest = (6, 6)

total_cost, paths, vis, heuristic_cost = a_star(matrix, start, dest)



