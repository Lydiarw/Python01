class Plant:
    def __init__(
            self,
            name: str,
            starting_height: float,
            starting_age: int
    ) -> None:
        self.name: str = name
        self.starting_height: float = starting_height
        self.starting_age: int = starting_age

    def show(self) -> None:
        print(
            f"Created: {self.name}: {self.starting_height}cm, "
            f"{self.starting_age} days old"
        )


def main() -> None:
    plants = [
        Plant('Rose', 25.0, 30),
        Plant('Oak', 200.0, 365),
        Plant('Cactus', 5.0, 90),
        Plant('Sunflower', 80.0, 45),
        Plant('Fern', 15.0, 120)
    ]
    print('=== Plant Factory Output ===')
    # for banana in plants: >>> banana.show()
    for plant in plants:
        plant.show()


if __name__ == "__main__":
    main()
