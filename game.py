"""
Robert Oh
A01321210

Collin Chan
A01337496

The main module of our text-based adventure game.
"""
import random
import itertools

"""
#----combat----
#combat()
#intiative()
#combat_victory()
#hit_detection() # rng calculation according to stats

    for rows in rows:
        for column in columns:
            # board[(row,column)] = ["Welcome to this room", None]
            # roll rng, assign challenge according to roll dice

    # return dictionary:
        # key: coordinate tuple
        # value: list [string that describes location, event/character to interact, [choices1, choices2]]
        
def describe_current_location(board, character):
    # read board location and character, print out
    
REMEMBER ANNOTATIONS
"""

# Global constant for enumerating user choices in movement
USER_INPUT_MOVING = ("NORTH", "EAST", "SOUTH", "WEST", "MAP")
# Global constants for enumerating user choices in fighting
USER_INPUT_FIGHTING_LEVEL_ONE = ("PUNCH", "KICK", "ICE BOLT")
USER_INPUT_FIGHTING_LEVEL_TWO = ("PUNCH", "KICK", "ICE BOLT", "FIREBALL")
USER_INPUT_FIGHTING_LEVEL_THREE = ("PUNCH", "KICK", "ICE BOLT", "FIREBALL", "WORLD ENDER")
# Global constant for obstacle environments
OBSTACLES = ("wall", "water")
# Global constant for enemy stats with "type" key's value coming from the entries in the ENVIRONMENTS global constant
ENEMY_STATS = ({"type": "bat", "HP": 100, "damage range": [0, 10], "exp gained": 10},
               {"type": "goblin", "HP": 150, "damage range": [10, 20], "exp gained": 25})
# Global constant for random event environments
ENVIRONMENTS = (("bat", "?", "A weak bat flutters around you"),
                ("goblin", "?", "A ferocious goblin sees you"),
                ("nothing", "?", "There is nothing here"))


"""
BOARD RELATED FUNCTIONALITY START
"""


def fill_board_coordinates_vertical(board, coords, times, generate_function) -> None:
    (start_x, start_y) = coords
    for pair in zip(range(start_x, start_x + times), itertools.repeat(start_y, times)):
        board[pair] = generate_function


def fill_board_coordinates_horizontal(board, coords, times, generate_function):
    (start_x, start_y) = coords
    for pair in zip(itertools.repeat(start_x, times), range(start_y, start_y + times)):
        board[pair] = generate_function


def set_coordinate_state(board, coordinate, generate_function):
    board[coordinate] = generate_function


def make_board(rows, columns):
    """
    """
    board = {}
    for row_coordinate in range(rows):
        for pair in zip(itertools.repeat(row_coordinate, rows), range(columns)):
            board[pair] = random_event
    # Create initial map layout here
    fill_board_coordinates_horizontal(board, (4, 2), 2, wall)
    fill_board_coordinates_horizontal(board, (4, 6), 2, wall)
    fill_board_coordinates_vertical(board, (0, 2), 4, water)
    fill_board_coordinates_vertical(board, (0, 7), 4, water)
    set_coordinate_state(board, (0, 0), item)
    return board


def map_board(board, character):
    print("\nMAP:")
    for coordinate, generate_function in board.items():
        print(f"[{generate_function(character)[1]}] ", end="")
        if coordinate[1] == 9:
            print("")
    print("Legend: ! = you, # = water, % = wall, ? = an event, @ = an item\n")


"""
BOARD RELATED FUNCTIONALITY END
"""


"""
GAME PROGRESSION RELATED FUNCTIONALITY START
"""


def leveled_up():
    pass


"""
GAME PROGRESSION RELATED FUNCTIONALITY END
"""


"""
COMBAT RELATED FUNCTIONALITY START
"""


def damage_the_enemy(enemy, character, skill):
    skill_stat_list = [skills_stats for skills_stats in character["SKILLS"] if skills_stats["type"] == skill]
    skill_stat = skill_stat_list[0]
    print(skill_stat)
    damage = random.randint(skill_stat["damage range"][0], skill_stat["damage range"][1])
    enemy["HP"] -= damage
    character["CURRENT MP"] -= skill_stat["MP cost"]


def damage_the_character(character, enemy):
    damage = random.randint(enemy["damage range"][0], enemy["damage range"][1])
    print(damage)
    character["CURRENT HP"] -= damage


def character_get_exp(character, enemy):
    character["CURRENT EXP"] += enemy["exp gained"]


def handle_level_up(character):
    character["CURRENT EXP"] = 0
    character["level"] += 1
    print(f'congratulations for levelling to {character["level"]}')


def character_has_leveled(character):
    return character["CURRENT EXP"] >= character["EXP TO LEVEL"]


def execute_challenge_protocol(character, current_environment):
    print(f"you are fighting the {current_environment[0]}!")
    enemy_stats_list = [enemy_with_stats for enemy_with_stats in ENEMY_STATS if enemy_with_stats["type"] == current_environment[0]]
    enemy = enemy_stats_list[0]
    while enemy["HP"] >= 0 and is_alive(character):
        skill = get_user_choice(USER_INPUT_FIGHTING_LEVEL_ONE)
        damage_the_enemy(enemy, character, skill)
        damage_the_character(character, enemy)
        print(character)
        print(enemy)
    character_get_exp(character, enemy)


"""
COMBAT RELATED FUNCTIONALITY END
"""


"""
BOARD ENVIRONMENT RELATED FUNCTIONALITY START
"""


def random_event(character):
    weak_enemies_list = list(itertools.repeat(ENVIRONMENTS[0], character["level"]))
    strong_enemies_list = list(itertools.repeat(ENVIRONMENTS[1], character["level"]))
    none_list = list(itertools.repeat(ENVIRONMENTS[2], 5))
    scaled_environment_list = list(itertools.chain.from_iterable([weak_enemies_list, strong_enemies_list, none_list]))
    # print(scaled_environment_list)
    return random.choice(scaled_environment_list)


def cool_description(_):
    return random.choice([("", "!", "The musty ground envelops you"), ("", "!", "The dark air is suffocating"),
                          ("", "!", "You can't see through this fog"), ("", "!", "You smell rotting flesh")])


def wall(_):
    return "wall", "%", "A wall towers over you"


def water(_):
    return "water", "#", "A large body of water"


def item(_):
    return "item", "@", "You see a item to help your adventures"


def final_boss(_):
    return "boss", "@", "The final boss is menacing"


"""
BOARD ENVIRONMENT RELATED FUNCTIONALITY END
"""


"""
MOVEMENT RELATED FUNCTIONALITY START
"""


def move_character(character, direction) -> tuple[int, int]:
    update_character_status(character)
    new_coordinates = ()
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


"""
MOVEMENT RELATED FUNCTIONALITY END
"""


"""
PRINTING RELATED FUNCTIONALITY START
"""


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


def print_obstacle_message(character, direction):
    print(f"can't move to {move_character(character, direction)}, there is an obstacle")


def describe_current_location(board, character):
    environment = board[character["coordinates"]](character)
    print(f"{environment[2]}, you are at {character['coordinates']}\n")
    return environment


"""
PRINTING RELATED FUNCTIONALITY END
"""

"""
CHARACTER RELATED FUNCTIONALITY START
"""


def is_alive(character):
    return character["CURRENT HP"] >= 0


def update_character_status(character):
    pass


def make_character(name):
    return {"name": name, "coordinates": (6, 4), "level": 1, "CURRENT HP": 150,
            "MAX HP": 150, "CURRENT MP": 150, "MP": 150, "CURRENT EXP": 0, "EXP TO LEVEL": 150,
            "SKILLS": (
                {"type": "PUNCH", "MP cost": 0, "damage range": [5, 10]},
                {"type": "KICK", "MP cost": 0, "damage range": [10, 20]},
                {"type": "ICE BOLT", "MP cost": 50, "damage range": [50, 100]},
                {"type": "FIREBALL", "MP cost": 60, "damage range": [50, 150]}
            )
            }


"""
CHARACTER RELATED FUNCTIONALITY END
"""


def is_none(environment):
    return environment[0] != "nothing"


def get_user_choice(choice_list):
    user_input = ""
    choices_to_print = "make a selection:\n"
    enumerated_choices = list(enumerate(choice_list, 1))
    valid_input = [str(choice[0]) for choice in enumerated_choices]
    while user_input not in valid_input:
        for choice in enumerated_choices:
            choices_to_print += f"{choice[0]}.{choice[1]}\n"
        user_input = input(f"{choices_to_print}\n")
        choices_to_print = "invalid input, make another selection:\n"
    input_name = [choice[1] for choice in enumerated_choices if str(choice[0]) == user_input]
    # print(input_name)
    return input_name[0]


def game():
    rows = 10
    columns = 10
    name = get_character_name()
    character = make_character(name)
    board = make_board(rows, columns)
    achieve_goal = False
    print_intro(name)
    print_instructions()
    while not achieve_goal and is_alive(character):
        set_coordinate_state(board, character["coordinates"], cool_description)
        describe_current_location(board, character)
        direction = get_user_choice(USER_INPUT_MOVING)
        if direction == "MAP":
            map_board(board, character)
            continue
        valid_move = validate_move(board, character, direction)
        if valid_move:
            set_coordinate_state(board, character["coordinates"], random_event)
            character["coordinates"] = move_character(character, direction)
            current_environment = describe_current_location(board, character)
            if current_environment in list(filter(is_none, list(ENVIRONMENTS))):
                execute_challenge_protocol(character, current_environment)
                print(character)
                if character_has_leveled(character):
                    handle_level_up(character)
            # achieved_goal = check_if_goal_attained(board, character) # reached level 3, killed boss
                # one of the key: value pair in character should be boss_killed : False
        else:
            print_obstacle_message(character, direction)
    print_end_of_game(name)


def main():
    """
    Drives the program.
    """
    game()


if __name__ == "__main__":
    main()
