from typing import List, Tuple


def sort_unique_elements(str_list: Tuple[str, ...]) -> List[str]:
    unique = list(set(list(str_list)))
    unique.sort()

    return unique
