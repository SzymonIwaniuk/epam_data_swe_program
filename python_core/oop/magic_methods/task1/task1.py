from typing import List, Any


class Counter:
    def __init__(self, values: List[int]):
        self.values = values

    def __add__(self, x: Any) -> List[str]:
        return [f"{num} {x}" for num in self.values]
