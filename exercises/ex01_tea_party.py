"""Tea Party Expenses"""

__author__: str = "730799969"


def main_planner(guests: int) -> None:
    """entrypoint of my program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))
    return None


def tea_bags(people: int) -> int:
    """number of tea bags for people"""
    return people * 2


def treats(people: int) -> int:
    """number of treats for people"""
    return tea_bags(people=int(people * 1.5))


def cost(tea_bags: int, treats: int) -> float:
    """cost of tea bags and treats combined"""
    return tea_bags * 0.50 + treats * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
