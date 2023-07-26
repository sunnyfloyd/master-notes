from typing import Protocol


class HasName(Protocol):
    name: str


class Person:
    name: str


class Android:
    code: str


def say_hello(obj: HasName) -> None:
    print(f"Hello {obj.name}")


say_hello(Person())
say_hello(Android())
