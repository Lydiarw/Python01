class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self._height: float = 0.0
        self._age: int = 0
        self._stats: Plant.Stats = Plant.Stats(name)

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
        self._stats.record_show()
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    class Stats:
        def __init__(self, name: str) -> None:
            self.name = name
            self.grow_calls: int = 0
            self.age_calls: int = 0
            self.show_calls: int = 0

        def display_stats(self) -> None:
            print(f"[statistics for {self.name}]")
            print(
                f"Stats: {self.grow_calls} grow, {self.age_calls} age, "
                f"{self.show_calls} show"
            )

        def record_grow(self) -> None:
            self.grow_calls += 1

        def record_age(self) -> None:
            self.age_calls += 1

        def record_show(self) -> None:
            self.show_calls += 1

    def display_stats(self) -> None:
        self._stats.display_stats()

    @staticmethod
    def above_one_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls(name='Unknown plant', height=0, age=0)

    def anonymous_stats(self) -> None:
        self.display_stats()


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.bloomed: bool = False
        self.seeds: Flower.Seeds = self.Seeds()

    def grow(self, _height: float) -> None:
        self._height = _height
        self._stats.record_grow()

    def age(self, _age: int) -> None:
        self._age = _age
        self._stats.record_age()

    def bloom(self) -> None:
        self.bloomed = True
        self.seeds.seeds_on_hand += 42

    def flower_stats(self) -> None:
        self.display_stats()

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")
        if self.name == "Sunflower":
            print(f" Seeds: {self.seeds.seeds_on_hand}")

    class Seeds:
        def __init__(self) -> None:
            self.seeds_on_hand: int = 0


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
        self.shade_calls: int = 0

    def produce_shade(self) -> None:
        self.shade_calls += 1
        print(
            f"Tree {self.name} now produces a shade of {self._height:.1f}cm "
            f"long and {self.trunk_diameter:.1f}cm wide."
        )

    def tree_stats(self) -> None:
        self.display_stats()
        print(f" {self.shade_calls} shade")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


def display_stats(plant: Plant) -> None:
    print('=== ALL Plant Statistics ===')
    plant.display_stats()


def main() -> None:
    f = Flower("Rose", 15, 10, "red")
    f1 = Flower("Sunflower", 80, 45, "yellow")
    t = Tree("Oak", 200, 365, 5)
    # v = Vegetable("Tomato", 5, 10, "April", 0)
    a = Plant.create_anonymous()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.above_one_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.above_one_year(400)}")
    print()

    print("=== Flower")
    f.show()
    f.flower_stats()
    print("[asking the rose to grow and bloom]")
    f.grow(23)
    f.bloom()
    f.show()
    f.flower_stats()
    print()

    print("=== Tree")
    t.show()
    t.tree_stats()
    print("[asking the oak to produce shade]")
    t.produce_shade()
    t.tree_stats()
    print()

    print("=== Seed")
    f1.show()
    print("[make sunflower grow, age and bloom]")
    f1.bloom()
    f1.grow(110)
    f1.age(65)
    f1.show()
    f1.flower_stats()
    print()

    print("=== Anonymous")
    a.show()
    a.anonymous_stats()
    print()

    display_stats(f)
    display_stats(t)
    display_stats(a)


if __name__ == "__main__":
    main()
