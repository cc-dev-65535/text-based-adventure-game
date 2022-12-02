def get_character_name():
    return input("State your name foolish human\nYour reply: ")


def print_intro(name):
    print(f"\nHello, {name}.\n"
          f"It seems you are trapped in this dungeon until you can defeat me.\n"
          f"I will be waiting for you when the time has come (i.e., you reach level 3)\n"
          f"Sincerely, Baldur\n")


def print_instructions():
    print(f"instructions go here")


def print_end_of_game(name):
    print(f"you have finished, {name}")
