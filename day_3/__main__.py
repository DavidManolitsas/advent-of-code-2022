"""
Advent of Code 2022 Day 3
"""
import argparse

from day_3.rucksack.compartment import get_rucksacks, split_all_rucksacks
from day_3.rucksack.group import get_rucksack_groups
from day_3.rucksack.priority import get_group_priority, get_rucksack_priority

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-f", "--file", type=str, required=True)
args = arg_parser.parse_args()

with open(args.file, "r", encoding="utf-8") as file:
    rucksacks = get_rucksacks(rucksack_input=file.read())

    # part one
    compartments = split_all_rucksacks(rucksacks=rucksacks)
    print(f"Part one: {get_rucksack_priority(rucksacks=compartments)}")

    # part two
    groups = get_rucksack_groups(rucksacks=rucksacks)
    print(f"Part two: {get_group_priority(groups=groups)}")
