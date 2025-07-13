from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    nums = list(str(num))
    tup = tuple(map(lambda n: int(n), nums))

    return tup

