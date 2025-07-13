from typing import List


def check(
    row_start: int, row_end: int, column_start: int, column_end: int
) -> List[List[int]]:
    sol = [[] for _ in range(row_end + 1 - row_start)]
    idx = 0

    for i in range(row_start, row_end + 1):
        for j in range(column_start, column_end + 1):
            sol[idx].append(i * j)

        idx += 1

    return sol
