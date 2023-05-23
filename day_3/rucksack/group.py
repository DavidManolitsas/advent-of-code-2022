"""
Rucksack group functions.
"""


def get_common_group_item(group: (str, str, str)):
    """
    Get common item from group of rucksacks.

    :param group: group of three rucksacks
    :return: common item in group
    """
    return list(set(group[0]) & set(group[1]) & set(group[2]))[0]


def get_rucksack_groups(rucksacks: [str]) -> [(str, str, str)]:
    """
    Get groups of three rucksacks.

    :param rucksacks: all rucksacks as list
    :return: rucksacks grouped into groups of three
    """
    return [tuple(rucksacks[i : i + 3]) for i in range(0, len(rucksacks), 3)]
