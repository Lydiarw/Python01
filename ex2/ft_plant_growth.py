class Plant:
    def __init__(self, name: str, height: float, age_num: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age_num: int = age_num

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.age_num += 1

    def show(self) -> None:
        print(
            f"{self.name}: {round(self.height, 1)}cm, "
            f"{self.age_num} days old"
        )


def main() -> None:
    p1 = Plant('Rose', 25.0, 30)
    print('=== Garden Plant Growth ===')
    for i in range(7):
        print(f"=== Day {i + 1} ===")
        p1.show()
        p1.grow()
        p1.age()
    growth = round(p1.height - 25)
    print(f"Growth this week: {growth}cm")


if __name__ == "__main__":
    main()
