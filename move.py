import game


def move_character_direction(character, direction):
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


def move_character(board, character, direction):
    (x, y) = character["coordinates"]
    coordinates_moved = move_character_direction(character, direction)
    if (coordinates_moved not in board.keys()) or (board[coordinates_moved]() == "wall"):
        print(f"can't move there! -> {coordinates_moved}")
        return x, y
    return coordinates_moved


def main():
    """
    Drives the program.
    """
    my_board = game.make_board(10, 10)
    game.print_board(my_board)
    character = game.make_character("Collin")
    character["coordinates"] = move_character(my_board, character, "w")
    character["coordinates"] = move_character(my_board, character, "e")
    character["coordinates"] = move_character(my_board, character, "e")
    character["coordinates"] = move_character(my_board, character, "s")
    character["coordinates"] = move_character(my_board, character, "s")
    print(character)

if __name__ == "__main__":
    main()