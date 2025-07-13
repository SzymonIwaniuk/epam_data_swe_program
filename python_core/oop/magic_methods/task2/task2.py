class Bird:
    def __init__(self, name: str) -> None:
        self.name = name

    def walk(self) -> str:
        return f"{self.name} bird can walk"

    def fly(self) -> str:
        return f"{self.name} bird can fly"


class FlyingBird(Bird):
    def __init__(self, name: str, ration="grains") -> None:
        super().__init__(name)
        self.ration = ration

    def __str__(self) -> str:
        return f"{self.name} bird can walk and fly"

    def eat(self) -> str:
        return f"It eats mostly {self.ration}"


class NonFlyingBird(Bird):
    def __init__(self, name: str, ration="fish") -> None:
        super().__init__(name)
        self.ration = ration

    def swim(self) -> str:
        return f"{self.name} bird can swim"

    def eat(self) -> str:
        return f"It eats mostly {self.ration}"

    def fly(self) -> None:
        raise AttributeError(f"'{self.name}' object has no attribute 'fly'")


class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name: str, ration="fish") -> str:
        super().__init__(name, ration)

    def __str__(self) -> str:
        return f"{self.name} bird can walk, swim and fly"

    def fly(self) -> str:
        return f"{self.name} bird can fly"
