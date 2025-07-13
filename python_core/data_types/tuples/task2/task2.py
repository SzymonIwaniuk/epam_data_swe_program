from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    n = len(lst)

    if n == 0 or n == 1:
        return []

    res = []

    for i in range(n-1):
        res.append(tuple(lst[i:i+2]))

    return res
