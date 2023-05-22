"""
Score the game of rock paper scissors.
"""

from day_2.shape.types import Game, Shape


def play_rock(opposing_shape: Shape):
    """
    Get the score if rock is played.

    :param opposing_shape: oppositions shape
    :return: game score
    """
    if opposing_shape is Shape.PAPER:
        return 0

    if opposing_shape is Shape.ROCK:
        return 3

    return 6


def play_paper(opposing_shape: Shape):
    """
    Get the score if paper is played.

    :param opposing_shape: oppositions shape
    :return: game score
    """
    if opposing_shape is Shape.SCISSORS:
        return 0

    if opposing_shape is Shape.PAPER:
        return 3

    return 6


def play_scissors(opposing_shape: Shape):
    """
    Get the score if scissor is played.

    :param opposing_shape: oppositions shape
    :return: game score
    """
    if opposing_shape is Shape.ROCK:
        return 0

    if opposing_shape is Shape.SCISSORS:
        return 3

    return 6


SHAPE_MAP = {
    Shape.ROCK: play_rock,
    Shape.PAPER: play_paper,
    Shape.SCISSORS: play_scissors,
}


def get_shape_score(shape: Shape):
    """
    Get score for individual shape.

    :param shape: rock paper scissor
    :return: shape score value
    """
    match shape:
        case Shape.ROCK:
            return 1
        case Shape.PAPER:
            return 2
        case Shape.SCISSORS:
            return 3


def score_game(game: Game):
    """
    Score an individual rock paper scissor game.

    :param game: rock paper scissor game
    :return: game score
    """
    return get_shape_score(game[1]) + SHAPE_MAP[game[1]](game[0])


def play_games(games: [Game]):
    """
    Play all rock paper scissor games.

    :param games: list of rock paper scissor games
    :return: total score of all games
    """
    return sum(score_game(game) for game in games)
