OBSTACLES = ("wall", "watr")

## REMEMBER ANNOTATIONS
def move_character(character, direction) -> tuple[int,int]:
    # update hp and mp here?
    (x, y) = character["coordinates"]
    if direction == "s":
        new_coordinates = (x + 1, y)
    if direction == "n":
        new_coordinates = (x - 1, y)
    if direction == "e":
        new_coordinates = (x, y + 1)
    if direction == "w":
        new_coordinates = (x, y - 1)
    return new_coordinates


def validate_move(board, character, direction):
    coordinates_moved = move_character(character, direction)
    if (coordinates_moved not in board.keys()) or (board[coordinates_moved]() in OBSTACLES):
        return False
    return True