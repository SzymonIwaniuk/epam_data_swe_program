class PriceControl:
    """
    Descriptor which don't allow to set price
    less than 0 and more than 100 included.
    """
    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Price must be between 0 and 100.")
        setattr(instance, self.private_name, value)


class NameControl:
    """
    Descriptor which don't allow to change field value after initialization.
    """
    def __set_name__(self, owner, name):
        self.private_name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if hasattr(instance, self.private_name):
            raise ValueError(f"{self.private_name[1:].capitalize()} can not be changed.")
        setattr(instance, self.private_name, value)


class Book:
    author = NameControl()
    name = NameControl()
    price = PriceControl()

    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price



