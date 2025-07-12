from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    sub = []

    for item in sequence:
        if isinstance(item, (int, float)):
            sub.append(item)
        else:
            sub.extend(linear_seq(item))

    return sub
