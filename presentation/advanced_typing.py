from collections.abc import Iterable
from decimal import Decimal
from fractions import Fraction
from typing import TypeVar, Protocol, Any


class SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool:
        return True


NumberT = TypeVar("NumberT", float, Decimal, Fraction)


def mode(data: Iterable[NumberT]) -> NumberT:
    return max(data)


LT = TypeVar("LT", bound=SupportsLessThan)


def top(series: Iterable[LT], length: int) -> list[LT]:
    ordered = sorted(series, reverse=True)
    return ordered[:length]
