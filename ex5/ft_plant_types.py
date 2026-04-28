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

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.bloomed: bool = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height:.1f}cm long and {self.trunk_diameter:.1f}wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            harvest_season: str,
            nutritional_value: int
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = nutritional_value
        self.height_increased: bool = False
        self.age_increased: bool = False

    def grow(self) -> None:
        self._height += 42
        self.height_increased = True

    def age(self) -> None:
        self._age += 20
        self.age_increased = True

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        if self.height_increased and self.age_increased:
            self.nutritional_value += 20
            print(f" Nutritional value: {self.nutritional_value}")
        else:
            print(f" Nutritional value: {self.nutritional_value}")


def main() -> None:
    f = Flower("Rose", 15, 10, "red")
    t = Tree("Oak", 200, 365, 5)
    v = Vegetable("Tomato", 5, 10, "April", 0)
    print("=== Garden Plant Types ===")

# Flower
    print("=== Flower")
    f.show()
    print("[asking the rose to bloom]")
    f.bloom()
    f.show()
    print()
# Tree
    print("=== Tree")
    t.show()
    print("[asking the oak to produce shade]")
    t.produce_shade()
    print()
# Vegetable
    print("=== Vegetable")
    v.show()
    print("[make tomato grow and age for 20 days]")
    v.grow()
    v.age()
    v.show()


if __name__ == "__main__":
    main()
