"""Test for Dictionary function practice"""

__author__: str = "730799969"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_count_spots() -> None:
    """tests words that occur more than once in different spots"""
    assert count(["hi", "bye", "hi"]) == {"hi": 2, "bye": 1}


def test_count_multiple() -> None:
    """tests if there's one of each for multiple"""
    assert count(["love", "hate", "indifferent"]) == {
        "love": 1,
        "hate": 1,
        "indifferent": 1,
    }


def test_count_nothing() -> None:
    assert count([]) == {}


def test_invert_singular() -> None:
    """tests singular letters"""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_whole() -> None:
    """tests whole words"""
    assert invert({"dog": "pup", "kangaroo": "joey"}) == {
        "pup": "dog",
        "joey": "kangaroo",
    }


def test_invert_nothing() -> None:
    """flips nothing when there is nothing in dicttionary"""
    assert invert({}) == {}


def test_favorite_color_tie() -> None:
    """tests that the function returns the first color if there's a tie"""
    assert (
        favorite_color(
            {"LILY": "BLUE", "LIV": "GREEN", "CASSIDY": "GREEN", "PERSON": "BLUE"}
        )
        == "BLUE"
    )


def test_favorite_color_mode() -> None:
    """test that my function can return the color that occrs the most when it is greater than 1"""
    assert (
        favorite_color({"LILY": "BLUE", "LIV": "GREEN", "CASSIDY": "GREEN"}) == "GREEN"
    )


def test_favorite_color_nothing() -> None:
    """tests that the function returns and empty string if there is nothing in the dictionary argument"""
    assert favorite_color({}) == ""


def test_bin_len_multiple() -> None:
    """tests multiple same length words and another length"""
    assert bin_len(["apple", "ape", "app"]) == {5: {"apple"}, 3: {"ape", "app"}}


def test_bin_len_all() -> None:
    """tests all same length"""
    assert bin_len(["words", "stare", "stars"]) == {5: {"words", "stare", "stars"}}


def test_bin_len_single() -> None:
    """tests a single character is length of 1"""
    assert bin_len(["a"]) == {1: {"a"}}


def test_bin_len_0() -> None:
    """tests that the function can return 0 when nothing is in the string"""
    assert bin_len([""]) == {0: {""}}
