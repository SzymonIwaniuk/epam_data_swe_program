from typing import Optional


class Counter:
    inf = float('inf')

    def __init__(self, start = 0, stop = inf) -> None:
        self.cnt = start
        self.stop = stop

    def increment(self) -> Optional[float]:
        if self.cnt == self.stop:
            return "The maximal value is reached."

        self.cnt += 1

    def get(self) -> int:
        return self.cnt

