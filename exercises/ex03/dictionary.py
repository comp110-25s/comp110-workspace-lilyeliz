"""Dictionary function practice"""

__author__: str = "730799969"


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    """flips keys and values"""
    result: dict[str, str] = {}
    temp: str
    for key in dict_1:
        if dict_1[key] in result:
            raise KeyError(f"{dict_1[key]} Already in Dictionary")
        temp = dict_1[key]
        result[temp] = key
    return result


def count(values: list[str]) -> dict[str, int]:
    """counts how many times a string appears in a list"""
    result: dict[str, int] = {}
    idx: int = 0
    if idx < len(values):
        while idx < len(values):
            if values[idx] in result:
                result[values[idx]] += 1
            else:
                result[values[idx]] = 1
            idx += 1
    return result


def favorite_color(name_color: dict[str, str]) -> str:
    """gives back the mode of people's favorite color"""
    color_list: list[str] = []
    idx: int = 0
    result: str = ""
    highest: int = 0
    for key in name_color:
        color_list.append(name_color[key])
    colors_count: dict[str, int] = count(color_list)
    for key in colors_count:
        if colors_count[key] > highest:
            result = key
            highest = colors_count[key]
        idx += 1
    return result


def bin_len(strs: list[str]) -> dict[int, set[str]]:
    """returns sets of strings and their lengths"""
    result: dict[int, set[str]] = {}
    idx: int = 0
    while idx < len(strs):
        length: int = len(strs[idx])
        if length not in result:
            result[length] = set()
        result[length].add(strs[idx])
        idx += 1
    return result
