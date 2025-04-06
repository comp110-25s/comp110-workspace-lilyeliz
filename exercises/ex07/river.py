"""File to define River class."""

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    day: int
    bears: list
    fish: list

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        bears_survived: list[Bear] = []
        fish_survived: list[Fish] = []
        for bear in self.bears:
            if bear.age <= 5:
                bears_survived.append(bear)
        self.bears = bears_survived
        for fish in self.fish:
            if fish.age <= 3:
                fish_survived.append(fish)
        return None

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        bears_survived: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                bears_survived.append(bear)
        self.bears = bears_survived
        return None

    def repopulate_fish(self):
        new_fish: int = len(self.fish) // 2 * 4
        x: int = 0
        while x < new_fish:
            self.fish.append(Fish())
            x += 1
        return None

    def repopulate_bears(self):
        new_bears: int = len(self.bears) // 2
        x: int = 0
        while x < new_bears:
            self.bears.append(Bear())
            x += 1
        return None

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        day: int = 1
        while day <= 7:
            self.one_river_day()
            day += 1
        return None

    def remove_fish(self, amount: int):
        idx: int = 0
        while idx < amount:
            self.fish.pop(idx)
            idx += 1
        return None
