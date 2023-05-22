"""
Advent of Code 2022 Day 2
"""
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-f", "--file", type=str, required=True)
args = arg_parser.parse_args()

with open(args.file, "r", encoding="utf-8") as file:
    print(file.read())
