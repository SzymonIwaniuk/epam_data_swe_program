from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    """
    Add your code here or call it from here
    """
    n = len(sequence)
    tmp_sum = 0

    for i in range(n):
        if isinstance(sequence[i], (int, float)):
            tmp_sum += sequence[i]
        else:
            tmp_sum += seq_sum(sequence[i])

    return tmp_sum
