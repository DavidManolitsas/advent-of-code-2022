"""
Advent of Code 2022 Day 1
"""
import argparse

from day_1.elf.calorie_counting import (
    get_calorie_counts,
    get_max_calorie_count,
    get_n_max_calories_counts,
)
from day_1.elf.calorie_processing import read_calories

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-f", "--file", type=str, required=True)
arg_parser.add_argument("-s", "--size", type=int, required=False)
args = arg_parser.parse_args()

with open(args.file, "r", encoding="utf-8") as file:
    all_calories = read_calories(calorie_input=file.read())
    calorie_counts = get_calorie_counts(all_calories=all_calories)

    # print max calories
    print(f"Part one: {get_max_calorie_count(calorie_counts=calorie_counts)}")

    if args.size:
        n = args.size
        print(
            f"Part two: "
            f"{get_n_max_calories_counts(calorie_counts=calorie_counts, n=n)}"
        )
