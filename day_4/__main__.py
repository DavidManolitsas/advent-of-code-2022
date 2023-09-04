"""
Advent of Code 2022 Day 4
"""
import argparse

from day_4.cleaning.sector import is_fully_contained, is_overlap_sectors, get_sectors

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-f", "--file", type=str, required=True)
args = arg_parser.parse_args()


with open(args.file, "r", encoding="utf-8") as file:
    fully_contained_count = 0
    overlap_count = 0

    for pair in file.read().split("\n"):
        assignments = pair.split(",")

        if is_fully_contained(sectors_1=get_sectors(assignment=assignments[0]),
                              sectors_2=get_sectors(assignment=assignments[1])):
            fully_contained_count += 1

        if is_overlap_sectors(sectors_1=get_sectors(assignment=assignments[0]),
                              sectors_2=get_sectors(assignment=assignments[1])):
            overlap_count += 1

    # part one: 471
    print(f'fully contained: {fully_contained_count}')
    # part two: 888
    print(f'overlap: {overlap_count}')

