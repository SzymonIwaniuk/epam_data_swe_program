from typing import List


class HistoryDict:
    def __init__(self, element: dict[str, int]) -> None:
        self.history = []
        self.storage = element

    def set_value(self, key: str, val: int) -> None:
        self.storage[key] = val
        self.update_history(key)

    def get_history(self) -> List[str]:
        return self.history

    def update_history(self, key: str) -> None:
        if len(self.history) == 5:
            self.history.pop(0)
        self.history.append(key)
