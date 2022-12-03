"""
Robert Oh
A01321210

Collin Chan
A01337496

The main module of our text-based adventure game.
"""
import random
import itertools
import copy
import sys

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
USER_INPUT_MOVING = ("NORTH", "EAST", "SOUTH", "WEST", "MAP", "QUIT")

# Global constant used for obstacle environment detection
OBSTACLES = ("wall", "table", "door")

# Global constant for random event environments
ENVIRONMENTS = (("weak duelist", "?", "Yikes! A weak duelist approaches you"),
                ("strong duelist", "?", "Oh no! A strong duelist approaches you"),
                ("nothing", "?", "There is nothing here, phew"))


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
    # Create initial map layout here with items, walls, and water
    fill_board_coordinates_horizontal(board, (3, 2), 2, wall)
    fill_board_coordinates_horizontal(board, (3, 6), 2, wall)
    fill_board_coordinates_vertical(board, (0, 2), 3, wall)
    fill_board_coordinates_vertical(board, (0, 7), 3, wall)
    fill_board_coordinates_vertical(board, (5, 1), 4, table)
    fill_board_coordinates_vertical(board, (5, 3), 4, table)
    fill_board_coordinates_vertical(board, (5, 6), 4, table)
    fill_board_coordinates_vertical(board, (5, 8), 4, table)
    fill_board_coordinates_horizontal(board, (3, 4), 2, door)
    fill_board_coordinates_horizontal(board, (1, 4), 2, table)
    set_coordinate_state(board, (0, 4), final_boss)
    set_coordinate_state(board, (0, 0), item)
    set_coordinate_state(board, (0, 9), item)
    set_coordinate_state(board, (9, 9), item)
    set_coordinate_state(board, (9, 0), item)
    set_coordinate_state(board, (6, 5), item)
    return board


def map_board(board, character):
    print("\nMAP OF CONVENTION CENTRE:")
    for coordinate, generate_function in board.items():
        print(f"[{generate_function(character)[1]}] ", end="")
        if coordinate[1] == 9:
            print("")
    print("LEGEND: ! = you, # = table, % = wall, - = door, "
          "? = unknown, @ = piece of exodia, $ = Maximillion Pegasus\n")


"""
BOARD RELATED FUNCTIONALITY END
"""


"""
GAME PROGRESSION RELATED FUNCTIONALITY START
"""


def character_get_exp(character, enemy):
    character["CURRENT EXP"] += enemy["exp gained"]


def handle_level_up(board, character):
    character["CURRENT EXP"] = 0
    character["level"] += 1
    character["MAX HP"] = character["level"] * 100
    character["CURRENT HP"] = character["MAX HP"]
    character["cards allowed"] += 1
    if character["level"] == 3:
        fill_board_coordinates_horizontal(board, (3, 4), 2, random_event)
    print(f'Congratulations on leveling to level {character["level"]}!')


def character_has_leveled(character):
    return character["CURRENT EXP"] >= character["EXP TO LEVEL"]


"""
GAME PROGRESSION RELATED FUNCTIONALITY END
"""


"""
COMBAT RELATED FUNCTIONALITY START
"""


def effect_the_enemy(enemy, character, skill):
    skill_stat_list = [skills_stats for skills_stats in character["SKILLS"] if skills_stats["type"] == skill]
    skill_stat = skill_stat_list[0]
    print(skill_stat)
    if "heal range" in skill_stat.keys():
        return False
    damage = random.randint(skill_stat["damage range"][0], skill_stat["damage range"][1])
    print(enemy["HP"])
    print(max(enemy["HP"] - damage, 0))
    enemy["HP"] = max(enemy["HP"] - damage, 0)
    print(damage)
    print(f'You chose to attack with {skill_stat["type"]}!')
    print(f'The opposing duelist received {damage} damage to their lifepoints! '
          f'Their lifepoints are now: {enemy["HP"]}')
    return enemy["HP"] <= 0


def effect_the_character(enemy, character, skill):
    skill_stat_list = [skills_stats for skills_stats in character["SKILLS"] if skills_stats["type"] == skill]
    skill_stat = skill_stat_list[0]
    print(skill_stat)
    if "heal range" in skill_stat.keys():
        health_gained = random.randint(skill_stat["heal range"][0], skill_stat["heal range"][1])
        character["CURRENT HP"] = min(character["CURRENT HP"] + health_gained, character["MAX HP"])
        print(f'You chose to heal with {skill_stat["type"]}!\n')
        print(f'You healed {health_gained} lifepoints! '
              f'Your lifepoints are now: {character["CURRENT HP"]}')
    damage = random.randint(enemy["damage range"][0], enemy["damage range"][1])
    print(damage)
    character["CURRENT HP"] = max(character["CURRENT HP"] - damage, 0)
    print(f'The opposing duelist prepares an attack!\n')
    print(f'you received {damage} damage to your lifepoints! '
          f'Your current lifepoints are: {character["CURRENT HP"]}')


def execute_challenge_protocol(character, current_environment, enemies):
    print(f"you are fighting a {current_environment[0]}!")
    enemy_stats_list = [enemy_stats for enemy_stats in enemies if enemy_stats["type"] == current_environment[0]]
    enemy = copy.copy(enemy_stats_list[0])
    while is_alive(character):
        skill_choices = random.sample(USER_INPUT_FIGHTING, character["cards allowed"])
        skill = get_user_choice(skill_choices)
        if effect_the_enemy(enemy, character, skill):
            break
        effect_the_character(enemy, character, skill)
        print(character)
        print(enemy)
    character_get_exp(character, enemy)


def enemies_init():
    return ({"type": "weak duelist", "HP": 100, "damage range": [0, 15], "exp gained": 10},
            {"type": "strong duelist", "HP": 150, "damage range": [20, 30], "exp gained": 20},
            {"type": "boss", "HP": 100000, "damage range": [9000, 10000], "exp gained": 20})


"""
COMBAT RELATED FUNCTIONALITY END
"""


"""
BOARD ENVIRONMENT RELATED FUNCTIONALITY START
"""


def random_event(character):
    weak_enemies_list = list(itertools.repeat(ENVIRONMENTS[0], character["level"]))
    strong_enemies_list = list(itertools.repeat(ENVIRONMENTS[1], character["level"] * 2))
    none_list = list(itertools.repeat(ENVIRONMENTS[2], 5))
    scaled_environment_list = list(itertools.chain.from_iterable([weak_enemies_list, strong_enemies_list, none_list]))
    # print(scaled_environment_list)
    return random.choice(scaled_environment_list)


def cool_description(_):
    return random.choice([("", "!", "You feel the cool air in the convention center"),
                          ("", "!", "The sound of duelists is deafening"),
                          ("", "!", "There are people everywhere"),
                          ("", "!", "There are duels going on eveywhere")])


def door(_):
    return "door", "-", "A door towers over you"


def wall(_):
    return "wall", "%", "A wall towers over you"


def table(_):
    return "table", "#", "A large table"


def item(_):
    return "item", "@", "You have found a piece of exodia!"


def final_boss(_):
    return "boss", "$", "Uh oh. Maximillion Pegasus moves towards you..."


"""
BOARD ENVIRONMENT RELATED FUNCTIONALITY END
"""


"""
MOVEMENT RELATED FUNCTIONALITY START
"""


def move_character(character, direction) -> tuple[int, int]:
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
    return input("State your name, duelist\nYour reply: \n")


def print_intro(name):
    print(f"\nHello, {name}.\n"
          f"It seems like you have signed up for this major dueling tournament\n"
          f"I'm the coordinator for this event\n"
          f"Oh, you don't know anything about that, you say? Well, that's too bad.\n"
          f"Your only way out of here is to beat the omega duelist 'Maximillion Pegasus'\n"
          f"I heard his deck is straight sick and you can't beat him conventionally\n"
          f"You probably have to find some cheat cards to bring him down\n"
          f"I've been hearing about these exodia cards that are busted\n"
          f"No duelist has ever been able to get all five, though.\n"
          f"Anyway, I won't bother you any longer. You probably have duels to attend to\n"
          f"Good luck. And may the heart of the cards be with you\n")


def print_instructions():
    print(f"You will be approached by duelists while moving through the convention center\n"
          f"Select cards from your deck to defeat them. Some cards have healing effects. These are important!\n"
          f"The doors to Maximillion Pegasus's room will open when you reach level 3\n"
          f"Be warned that you will need a special weapon to defeat him\n")


def print_end_of_game(name):
    print(f"you have finished, {name}!")


def print_obstacle_message(character, direction):
    print(f"can't move to {move_character(character, direction)}, there is an obstacle")


def print_death_message():
    print(f"You collapse to the floor in a daze\n"
          f"It seems you don't have what it takes to hang with these guys\n"
          f"RIP")
    sys.exit()


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


def item_obtained(character):
    character["exodia pieces"] += 1


def is_alive(character):
    return character["CURRENT HP"] > 0


def make_character(name):
    return {"name": name, "coordinates": (6, 4), "level": 1, "CURRENT HP": 100,
            "MAX HP": 100, "cards allowed": 2, "CURRENT EXP": 0, "EXP TO LEVEL": 150,
            "exodia pieces": 0, "boss dead": False,
            "SKILLS": (
                {"type": "DARK MAGICIAN", "damage range": [10, 30]},
                {"type": "BLUE-EYES WHITE DRAGON", "damage range": [100, 150]},
                {"type": "RED-EYES BLACK DRAGON", "damage range": [50, 100]},
                {"type": "GOBLIN'S SECRET REMEDY", "heal range": [50, 100]},
                {"type": "BLUE-EYES ULTIMATE DRAGON", "damage range": [9999, 9999]},
                {"type": "KURIBOH", "heal range": [20, 50]},
                {"type": "DARK MAGICIAN GIRL", "damage range": [50, 150]},
                {"type": "SCAPEGOAT", "heal range": [10, 50]},
                {"type": "JINZO", "damage range": [0, 150]},
                {"type": "DIAN KETO THE CURE MASTER", "heal range":[1000, 1500]},
                {"type": "CELTIC GUARDIAN", "damage range":[5, 20]},
                {"type": "MAN-EATER BUG", "damage range": [0, 20]},
                {"type": "BUSTER BLADER", "damage range": [50, 80]},
                {"type": "TOON WIZARD", "damage range": [0, 40]}
            )
            }


# Global constant for enumerating user choices in duels, a random subset will be chosen in a battle
USER_INPUT_FIGHTING = ("DARK MAGICIAN", "BLUE-EYES WHITE DRAGON", "GOBLIN'S SECRET REMEDY",
                       "RED-EYES BLACK DRAGON", "DARK MAGICIAN GIRL", "BLUE-EYES ULTIMATE DRAGON",
                       "KURIBOH", "SCAPEGOAT", "JINZO", "DIAN KETO THE CURE MASTER", "CELTIC GUARDIAN",
                       "MAN-EATER BUG", "BUSTER BLADER", "TOON WIZARD"
                       )

"""
CHARACTER RELATED FUNCTIONALITY END
"""


def quit_game():
    sys.exit()


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
    print(input_name)
    return input_name[0]


def game():
    rows = 10
    columns = 10
    enemies = enemies_init()
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
        if direction == "QUIT":
            quit_game()
        valid_move = validate_move(board, character, direction)
        if valid_move:
            set_coordinate_state(board, character["coordinates"], random_event)
            character["coordinates"] = move_character(character, direction)
            current_environment = describe_current_location(board, character)
            if current_environment[0] == "item":
                item_obtained(character)
                print(character)
                continue
            if current_environment in list(filter(is_none, list(ENVIRONMENTS))):
                execute_challenge_protocol(character, current_environment, enemies)
                print(character)
                if not is_alive(character):
                    print_death_message()
                print(f"Nice victory, {name}!")
                if character_has_leveled(character):
                    handle_level_up(board, character)
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
