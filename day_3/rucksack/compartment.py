"""
Rucksack compartment functions
"""


def split_rucksack(rucksack: str):
    """
    Split rucksack into two compartments.

    :param rucksack: rucksack.
    :return: rucksack split into two compartments
    """
    return rucksack[0 : len(rucksack) // 2], rucksack[len(rucksack) // 2 :]


def split_all_rucksacks(rucksacks: [str]) -> [(str, str)]:
    """
    Split all rucksacks into two compartments.

    :param rucksacks: all rucksacks.
    :return: all rucksacks with split compartments
    """
    return [split_rucksack(rucksack) for rucksack in rucksacks]


def get_rucksacks(rucksack_input: str):
    """
    Get all rucksacks from provided input.

    :param rucksack_input: input file as str
    :return: list of rucksacks
    """
    return rucksack_input.split("\n")


def get_common_compartment_item(rucksack: (str, str)):
    """
    Get common item from rucksack compartments.

    :param rucksack: rucksack of two compartments
    :return: common item in rucksack compartments
    """
    return list(set(rucksack[0]) & set(rucksack[1]))[0]
