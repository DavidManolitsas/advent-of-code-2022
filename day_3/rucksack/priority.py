"""
Item priority functions.
"""
from string import ascii_lowercase, ascii_uppercase

from day_3.rucksack.compartment import get_common_compartment_item
from day_3.rucksack.group import get_common_group_item


def get_item_priority(item: str):
    """
    Get priority value of item.

    :param item: rucksack item.
    :return: item priority value
    """
    if item.islower():
        return ascii_lowercase.index(item) + 1

    return ascii_uppercase.index(item) + 27


def get_rucksack_priority(rucksacks: [(str, str)]):
    """
    Get priority of rucksack compartments.

    :param rucksacks: all compartmentalised rucksacks
    :return: sum of all rucksack priorities
    """
    common_items = [
        get_common_compartment_item(rucksack=rucksack)
        for rucksack in rucksacks
    ]
    return sum(get_item_priority(item=item) for item in common_items)


def get_group_priority(groups: [(str, str, str)]):
    """
    Get priority of rucksack groups.

    :param groups: groups of three rucksacks
    :return: sum of all group prioritises
    """
    common_items = [get_common_group_item(group=group) for group in groups]
    return sum(get_item_priority(item=item) for item in common_items)
