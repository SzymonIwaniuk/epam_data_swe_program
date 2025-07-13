from typing import Dict


def generate_squares(num: int) -> Dict[int, int]:
    #  Dict comprehension
    if num > 0:
        res = {i: i * i for i in range(1, num + 1)}
    else:
        res = {}

    return res
