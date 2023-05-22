"""
Process elf calorie utility functions.
"""


def process_calories(calorie_list: list[str]) -> list[list[int]]:
    """
    Process elf calories into a list

    :param calorie_list: elf calories chunked into a str
    :return: elf calories as list
    """
    return [list(map(int, (load.split("\n")))) for load in calorie_list]


def read_calories(calorie_input: str) -> list[list[int]]:
    """
    Read input file to list of elf calories

    :param calorie_input: input calorie file
    :return: all elf calories
    """
    calorie_list = calorie_input.split("\n\n")
    all_calories = process_calories(calorie_list=calorie_list)
    return all_calories
