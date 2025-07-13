from __future__ import annotations
from typing import Type


class Currency:
    """
    1 EUR = 2 USD = 100 GBP

    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """

    cantor = {
        'Euro': {'Pound': 100.0, 'Dollar': 2.0, 'Euro': 1.0},
        'Dollar': {'Euro': 0.5, 'Pound': 50.0, 'Dollar': 1.0},
        'Pound': {'Euro': 0.01, 'Dollar': 0.02, 'Pound': 1.0},
        }
    
    currency_short = {
        'Euro': 'EUR',
        'Dollar': 'USD',
        'Pound': 'GBP',
    }

    def __init__(self, value: float):
        self.value = value
        

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        curr = cls.__name__
        other = other_cls.__name__
        rate = cls.cantor[curr][other]

        return f"{rate:.1f} {cls.currency_short[other]} for 1 {cls.currency_short[curr]}"
    

    def to_currency(self, other_cls: Type[Currency]) -> str:
        curr = self.__class__.__name__
        other = other_cls.__name__
        exchange = self.cantor[curr][other] * self.value
        
        return f"{exchange:.1f} {self.currency_short[other]}"

    def __add__(self, currency) -> str:
        curr = self.__class__.__name__
        other = currency.__class__.__name__
        exchange = self.cantor[other][curr] * currency.value
        total = self.value + exchange

        return f"{total:.1f} {self.currency_short[curr]}"

    def __eq__(self, currency) -> bool:
        curr = self.__class__.__name__
        other = currency.__class__.__name__
        exchange = self.cantor[other][curr] * currency.value

        return self.value == exchange

    def __gt__(self, currency) -> bool:
        curr = self.__class__.__name__
        other = currency.__class__.__name__
        exchange = self.cantor[other][curr] * currency.value

        return self.value > exchange

    def __lt__(self, currency) -> bool:
        curr = self.__class__.__name__
        other = currency.__class__.__name__
        exchange = self.cantor[other][curr] * currency.value

        return self.value < exchange
        

class Euro(Currency):
    pass


class Dollar(Currency):
    pass


class Pound(Currency):
    pass

