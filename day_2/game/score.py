"""
Score the game of rock paper scissors.
"""

from day_2.shape.types import Shape, Game


def play_rock(opposing_shape: Shape):
    if opposing_shape is Shape.PAPER:
        return 0

    if opposing_shape is Shape.ROCK:
        return 3

    return 6


def play_paper(opposing_shape: Shape):
    if opposing_shape is Shape.SCISSORS:
        return 0

    if opposing_shape is Shape.PAPER:
        return 3

    return 6


def play_scissors(opposing_shape: Shape):
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
    match shape:
        case Shape.ROCK:
            return 1
        case Shape.PAPER:
            return 2
        case Shape.SCISSORS:
            return 3


def score_game(game: Game):
    score = get_shape_score(game[1])
    score += SHAPE_MAP[game[1]](game[0])
    return score


def play_games(games: [Game]):
    return sum([score_game(game) for game in games])





