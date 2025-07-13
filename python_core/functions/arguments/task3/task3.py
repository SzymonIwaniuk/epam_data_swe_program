from typing import Dict


def combine_dicts(*args: Dict[str, int]) -> Dict[str, int]:
    out = {}

    for dicts in args:
        for key, val in dicts.items():
            if key in out:
                out[key] += val
            else:
                out[key] = val

    return out
