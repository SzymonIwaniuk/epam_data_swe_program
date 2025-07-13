from typing import Any, Dict, List, Set


def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    unique = set()

    for dict in lst:
        unique.update(dict.values())

    return unique
