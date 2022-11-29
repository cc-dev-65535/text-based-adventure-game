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
"""

import itertools
import random
import move

ENVIRONMENT_LIST = ("enem", "ridl", "none")


def make_character(name):
    return {"name" : name, "coordinates": (0,0), "HP": 150, "MP": 150}


def fill_board_coordinates_vertical(board, coords, times, generate_function):
    (start_x, start_y) = coords
    for pair in zip(range(start_x, start_x + times), itertools.repeat(start_y, times)):
        board[pair] = generate_function


def fill_board_coordinates_horizontal(board, coords, times, generate_function):
    (start_x, start_y) = coords
    for pair in zip(itertools.repeat(start_x, times), range(start_y, start_y + times)):
        board[pair] = generate_function


def random_event():
    random_num = random.randint(1, 100)
    if random_num < 49:
        return ENVIRONMENT_LIST[0]
    elif 49 < random_num < 70:
        return ENVIRONMENT_LIST[1]
    else:
        return ENVIRONMENT_LIST[2]


def empty():
    return "none"


def wall():
    return "wall"


def make_board(rows, columns):
    """
    """
    board = {}
    for row_coordinate in range(rows):
        for pair in zip(itertools.repeat(row_coordinate, rows), range(columns)):
            board[pair] = random_event
    fill_board_coordinates_horizontal(board, (2, 2), 5, wall)
    fill_board_coordinates_horizontal(board, (5, 2), 5, wall)
    fill_board_coordinates_horizontal(board, (0, 0), 1, empty)
    return board


def get_coordinate_state(coordinate):
    #print(coordinate())
    if 'wall' == coordinate():
        return 'wall'
    elif 'item' == coordinate():
        return 'item'
    else:
        return '????'


def map_board(board, character):
    for k, v in board.items():
        if k == character["coordinates"]:
            print(f"{k}=@@@@ ", end="")
        else:
            print(f"{k}={get_coordinate_state(v)} ", end="")
        if k[1] == 9:
            print("\n")


def describe_current_location(board, character):
    return board[character["coordinates"]]()


def game():
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    character = make_character("Collin")
    achieve_goal = False
    while not achieve_goal:
        # tell user where they are
        #unfreeze()
        print(f"you see: {describe_current_location(board, character)} at {character['coordinates']}")
        #direction = get_user_choice() # enumerate user choices (North, West, East, South)
        direction = input("make a move\n")
        if (direction == "map"):
            map_board(board, character)
            continue
        valid_move = move.validate_move(board, character, direction) # return false if move is out of bounds
        if valid_move:
            #freeze(board[character["coordinates"]])
            character["coordinates"] = move.move_character(character, direction) # update coords
            print(f"you see: {describe_current_location(board, character)} at {character['coordinates']}")
            input("do something!\n")
            #roll_for_initiaive = check_for_challenges() # return true after rolling RNG
            #if roll_for_initiaive:
                #execute_challenge_protocol(character)
                #if character_has_leveled():
                    #execute_glow_up_protocol() # ASCII art? congradulation message
            #achieved_goal = check_if_goal_attained(board, character) # reached level 3, killed boss
                # one of the key: value pair in character should be boss_killed : False
        else:
            print(f"can't move to {move.move_character(character, direction)}")
            # tell user they can't go in that direction

    #out of while loop
    # print end game message


def main():
    """
    Drives the program.
    """
    game()


if __name__ == "__main__":
    main()