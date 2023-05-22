"""
Processing rock paper scissor shapes and results.
"""
from day_2.shape.types import Game, Result, Shape


def get_games(shape_input: str) -> list[Game]:
    """
    Get all rock paper scissor games from input.

    :param shape_input: input file contents
    :return: list of rock paper scissor games
    """
    return map_shape_result(
        shape_result=[
            tuple(shape.split(" ")) for shape in shape_input.split("\n")
        ]
    )


def map_rock(result: Result):
    """
    Map rock to player shape by intended result.

    :param result: intended result
    :return: player shape
    """
    match result:
        case Result.WIN:
            return Shape.PAPER
        case Result.LOSE:
            return Shape.SCISSORS
        case Result.DRAW:
            return Shape.ROCK


def map_paper(result: Result):
    """
    Map paper to player shape by intended result.

    :param result: intended result
    :return: player shape
    """
    match result:
        case Result.WIN:
            return Shape.SCISSORS
        case Result.LOSE:
            return Shape.ROCK
        case Result.DRAW:
            return Shape.PAPER


def map_scissors(result: Result):
    """
    Map scissors to player shape by intended result.

    :param result: intended result
    :return: player shape
    """
    match result:
        case Result.WIN:
            return Shape.ROCK
        case Result.LOSE:
            return Shape.PAPER
        case Result.DRAW:
            return Shape.SCISSORS


SHAPE_MAP = {
    Shape.ROCK: map_rock,
    Shape.PAPER: map_paper,
    Shape.SCISSORS: map_scissors,
}


def map_shape_result(shape_result: []) -> list[Game]:
    """
    Map shape and result from input to enum values.

    :param shape_result: shape result tuple
    :return: list of games composed of two rock paper scissor shapes
    """
    shape_result_list = [
        (map_shape(shape[0]), map_result(shape[1])) for shape in shape_result
    ]
    return [
        (shape_result[0], SHAPE_MAP[shape_result[0]](shape_result[1]))
        for shape_result in shape_result_list
    ]


def map_shape(shape: str) -> Shape:
    """
    Map shape string value to Enum.

    :param shape: input string representation
    :return: shape enum
    """
    match shape:
        case "A":
            return Shape.ROCK
        case "B":
            return Shape.PAPER
        case "C":
            return Shape.SCISSORS


def map_result(result: str) -> Result:
    """
    Map result string value to Enum.

    :param result: input string representation
    :return: result enum
    """
    match result:
        case "X":
            return Result.LOSE
        case "Y":
            return Result.DRAW
        case "Z":
            return Result.WIN
