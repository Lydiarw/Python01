class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._height: float = 0.0
        self._age: int = 0

        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
        else:
            self._height = height
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
        else:
            self._age = age

    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm")

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days")

    def __str__(self) -> str:
        return (f"{self.name}: {float(self._height)}cm, {self._age} days old")


def main() -> None:
    print("=== Garden Security System ===")

    p1 = Plant("Rose", 15, 10)
    print(f"Plant created: {p1}\n")

    p1.set_height(25)
    p1.set_age(30)
    print()

    p1.set_height(-1)
    p1.set_age(-1)
    print()

    print(f"Current state: {p1}")


if __name__ == "__main__":
    main()
