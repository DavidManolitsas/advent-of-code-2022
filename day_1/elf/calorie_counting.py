"""
Elf calorie counting functions
"""


def get_calorie_counts(all_calories: list[list[int]]) -> list[int]:
    """
    Get all elves total calorie counts.

    :param all_calories: list of list containing elf calorie intake
    :return: all elves calorie counts
    """
    return list(map(sum, all_calories))


def get_max_calorie_count(calorie_counts: list[int]) -> int:
    """
    Get the max elf calorie count.

    :param calorie_counts: all elves calorie counts
    :return: the max elf calorie count
    """
    return max(calorie_counts)


def get_n_max_calories_counts(calorie_counts: list[int], n: int) -> int:
    """
    Get the n max elf calorie counts combined.

    :param calorie_counts: all elves calorie counts
    :param n: number of elf calorie totals to sum
    :return: n max elf calorie counts combined
    """
    calorie_counts.sort()
    return sum(calorie_counts[-n:])
