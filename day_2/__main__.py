"""
Advent of Code 2022 Day 2
"""
import argparse

from day_2.game.score import play_games
from day_2.shape.processing import get_games

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-f", "--file", type=str, required=True)
args = arg_parser.parse_args()

with open(args.file, "r", encoding="utf-8") as file:
    games = get_games(shape_input=file.read())
    print(f"Part two: {play_games(games=games)}")
