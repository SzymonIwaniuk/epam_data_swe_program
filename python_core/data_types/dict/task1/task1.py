from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    s = s.lower()
    res = {}

    for ch in s:
        if ch not in res:
            res[ch] = 0

        res[ch] += 1

    return res
