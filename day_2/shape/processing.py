from day_2.shape.types import Shape, Game


def get_games(shape_input: str) -> list[Game]:
    shapes = [tuple(shape.split(" ")) for shape in shape_input.split("\n")]
    return map_shapes(shapes=shapes)


def map_shapes(shapes: []) -> list[Game]:
    return [(map_shape(shape[0]), map_shape(shape[1])) for shape in shapes]


def map_shape(shape: str) -> Shape:
    match shape:
        case "A" | "X":
            return Shape.ROCK
        case "B" | "Y":
            return Shape.PAPER
        case "C" | "Z":
            return Shape.SCISSORS
