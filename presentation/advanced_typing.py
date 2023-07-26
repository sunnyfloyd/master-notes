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


Ok, małe uzupełnienie dotyczące tematów, których nie byłem w stanie w pełni wyjaśnić w trakcie prezentacji:
- W przypadku weryfikacji typów istnienie metod dotyczy duck typingu (czyli sprawdzenie w trakcie runtime), natomiast w przypadku static typingu weryfikacja opiera się o drzewo dziedziczenia i metody/atrybuty obiektu w przypadku użycia protokołów. Jeśli nie chcemy dziedziczyć po danej klasie abstrakcyjnej (własnej lub wbudowanej) to jesteśmy skazani na użycie protokołu.
- W kodzie można dziedziczyć klasy protokołów i jeśli takie dziedziczenie nie jest w akompaniamencie `Protocol` to wówczas klasa protokołu zamienia się w klasę typu ABC (pod względem zachowania w dziedziczeniu)!
```python
class HasName(Protocol):
    def check(self, other_name: str) -> bool: ...


class Child(HasName):  # protokół jako parent class
    def __init__(self, name: str):
        self.name = name
    def check(self, other_name: str) -> bool:
        return self.name == other_name
```
- Różnica w użyciu pomiędzy `TypeVar` a `typing.Protocol`:
  - `TypeVar` słuzy m.in. do definiowanaia zmiennych dla generycznych typów. W sytuacji, gdy wiemy, że obiekt o danym typie będzie używany w wielu miejscach możemy zdefiniować taki generyczny typ i używać go ze zmiennej. W razie późniejszych zmian taki generyk łatwo zmodyfikować, bo wystarczy zmienić w jednym miejscu.
  - `TypeVar` jest jedynym sensownym sposobem wprowadzenia typingu dla generycznych funkcji i klas. Chodzi o to, że w przypadku, gdy niewiele wiadomo o obiektach, które będą przekazywane do funkcji/metod i mogą one na dodatek zmieniać swoją strukturę i zachowanie w trakcie działania programu, to wówczas typowanie za pomocą protokołów może być niemożliwe.