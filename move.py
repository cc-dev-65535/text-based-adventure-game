# Global constant for obstacle environments
OBSTACLES = ("wall", "water")


def move_character(character, direction) -> tuple[int,int]:
    # update hp and mp here?
    (x, y) = character["coordinates"]
    if direction == "SOUTH":
        new_coordinates = (x + 1, y)
    if direction == "NORTH":
        new_coordinates = (x - 1, y)
    if direction == "EAST":
        new_coordinates = (x, y + 1)
    if direction == "WEST":
        new_coordinates = (x, y - 1)
    return new_coordinates


def validate_move(board, character, direction):
    coordinates_moved = move_character(character, direction)
    if (coordinates_moved not in board.keys()) or (board[coordinates_moved](character)[0] in OBSTACLES):
        return False
    return True