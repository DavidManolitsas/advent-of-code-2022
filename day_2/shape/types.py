from enum import Enum

Shape = Enum("Shape", ["ROCK", "PAPER", "SCISSORS"])

Game = Shape, Shape
