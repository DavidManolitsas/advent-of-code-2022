

def get_sectors(assignment: str) -> tuple[int, int]:
    sectors = assignment.split("-")
    return int(sectors[0]), int(sectors[1])


def is_fully_contained(sectors_1: tuple[int, int], sectors_2: tuple[int, int]):
    if sectors_1[0] <= sectors_2[0] and sectors_1[1] >= sectors_2[1]:
        return True
    elif sectors_2[0] <= sectors_1[0] and sectors_2[1] >= sectors_1[1]:
        return True


def is_overlap_sectors(sectors_1: tuple[int, int], sectors_2: tuple[int, int]):
    if sectors_1[0] <= sectors_2[0] <= sectors_1[1]:
        return True
    elif sectors_2[0] < sectors_1[0] <= sectors_2[1]:
        return True
