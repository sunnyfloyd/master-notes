from __future__ import annotations

class Vector:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar: int) -> Vector:
        return Vector(self.x * scalar, self.y * scalar)
    def __rmul__(self, scalar: int) -> Vector:
        return Vector(self.x * scalar, self.y * scalar)

    def __abs__(self) -> int:
        return pow((self.x**2 + self.y**2), 0.5)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __bool__(self) -> bool:
        return bool(abs(self))


v1 = Vector(2, 4)
v2 = Vector(2, 1)

print(v1)
print(v1 + v2)
print(abs(Vector(3, 4)))
print(Vector(3, 4) * 3)
print(3 * Vector(3, 4))
