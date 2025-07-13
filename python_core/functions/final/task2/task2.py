from typing import List


def split_by_index(s: str, indexes: List[int]) -> List[str]:
    n = len(s)
    indexes += [n]
    splitted = []
    prev = 0

    for idx in indexes:
        if idx > n:
            continue

        splitted.append(s[prev:idx])
        prev = idx

    return splitted
