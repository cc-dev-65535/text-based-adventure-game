from move import *
from environments import *
from print import *

"""
Robert Oh
A01321210
"""
#MORE NOTES
#describe current location returns
#get user choice uses a enumerated list and returns a
#check for challenges returns true or false
#character carreis around a dictionary that is basically it's global status
#once boss is beaten, leave the main game loop;
# to move, the game prints out a list for us and we select an element out of it
# combat: combat_was_a_success function causes player level ups
# probability of encounters is 20% at beignning

#make_board example
# def make_board(rows, columns):
#     board = {}
#     for row in rows:
#         for column in columns:
#             board[(row,columns)] = "something is in this coordinate"

# git conflict (pushing w/o pulling first)
# PULL first: merge incoming changes to branch
# merge -> merge

# ----
# check assignment 4 pdf: main game loop

# give users choices: no need for combat system.
#
# goal: level up to three, then boss encounter

# don't use .get

#use enumerate() for user choices

#----combat----
#combat()
#intiative()
#combat_victory()
#hit_detection() # rng calculation according to stats
"""
    for rows in rows:
        for column in columns:
            # board[(row,column)] = ["Welcome to this room", None]
            # roll rng, assign challenge according to roll dice

    # return dictionary:
        # key: coordinate tuple
        # value: list [string that describes location, event/character to interact, [choices1, choices2]]

def make_character(character_name):
    # dictionary
    # return address of dictionary so its assigned to character
    # keep track of stats, items?

def describe_current_location(board, character):
    # read board location and character, print out


def game():
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    character = make_character("Player name")
    achieve_goal = False
    while not achieve_goal:
        # tell user where they are
        describe_current_location(board, character)
        direction = get_user_choice() # enumerate user choices (North, West, East, South)
        valid_move = validate_move(board, character, direction) # return false if move is out of bounds
        if valid_move:
            move_character(character) # update coords
            describe_current_location(board, character)
            roll_for_initiaive = check_for_challenges() # return true after rolling RNG
            if roll_for_initiaive:
                execute_challenge_protocol(character)
                if character_has_leveled():
                    execute_glow_up_protocol() # ASCII art? congradulation message
            achieved_goal = check_if_goal_attained(board, character) # reached level 3, killed boss
                # one of the key: value pair in character should be boss_killed : False
        else:
            # tell user they can't go in that direction

    #out of while loop
    # print end game message
    
REMEMBER ANNOTATIONS
"""
# Global constant for enumerating user choices in movement
VALID_USER_INPUT_MOVING = (("1", "NORTH"), ("2", "EAST"), ("3", "SOUTH"), ("4", "WEST"), ("5", "MAP"))
# Global constant for enumerating user choices in fighting
VALID_USER_INPUT_FIGHTING_LEVEL_ONE = (("1", "PUNCH"), ("2", "KICK"), ("3", "BITE"), ("4", "HEADBUTT"))


def make_character(name):
    return {"name": name, "coordinates": (6, 4), "level": 1, "HP": 150, "MP": 150, "EXP": 0}


def leveled_up():
    pass


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


def make_board(rows, columns, character):
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
    for coordinate, generate_function in board.items():
        print(f"[{generate_function(character)[1]}] ", end="")
        if coordinate[1] == 9:
            print("")
    print("! = you, # = water, % = wall, ? = an event, @ = an item")


def describe_current_location(board, character):
    environment = board[character["coordinates"]](character)
    print(f"{environment[2]}, you are at {character['coordinates']}\n")
    return environment


def is_none(environment):
    return environment[0] != "nothing"


def get_user_choice(choice_list):
    user_input = ""
    choices_to_print = "make a selection:\n"
    valid_input = [choice[0] for choice in choice_list]
    while user_input not in valid_input:
        for choice in choice_list:
            choices_to_print += f"{choice[0]}.{choice[1]}\n"
        user_input = input(choices_to_print)
    input_name = [choice[1] for choice in choice_list if choice[0] == user_input]
    return input_name[0]


def enemy_not_dead(enemy):
    return enemy["HP"] >= 0


def character_not_dead(character):
    return character["HP"] >= 0


def damage_the_enemy(enemy, skill):
    enemy["HP"] -= 30
    pass


def damage_the_character(character, enemy):
    character["HP"] -= 1
    pass


def character_get_exp(character, enemy):
    character["EXP"] += 1


def execute_challenge_protocol(character, current_environment):
    print(f"you are fighting the {current_environment[0]}!")
    enemy = {"HP": 100, "damage_range": range(50,100)}
    while enemy_not_dead(enemy) and character_not_dead(character):
        skill = get_user_choice(VALID_USER_INPUT_FIGHTING_LEVEL_ONE)
        print(skill)
        damage_the_enemy(enemy, skill)
        damage_the_character(character, enemy)
    character_get_exp(character, enemy)
    print(enemy)


def print_obstacle_message(character, direction):
    print(f"can't move to {move_character(character, direction)}, there is an obstacle")

def game():
    rows = 10
    columns = 10
    name = get_character_name()
    character = make_character(name)
    board = make_board(rows, columns, character)
    achieve_goal = False
    print_intro(name)
    print_instructions()
    while not achieve_goal:
        set_coordinate_state(board, character["coordinates"], cool_description)
        describe_current_location(board, character)
        direction = get_user_choice(VALID_USER_INPUT_MOVING)
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
                # if character_has_leveled():
                    # execute_glow_up_protocol() # ASCII art? congradulation message
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
