"""
Rock paper scissor shapes, result and game types.
"""

from enum import Enum

Shape = Enum("Shape", ["ROCK", "PAPER", "SCISSORS"])

Game = Shape, Shape

Result = Enum("Result", ["WIN", "LOSE", "DRAW"])
