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

import itertools
import random

environment_list = ["enem", "ridl", "none"]

def make_character(name):
    return {"name" : name, "coordinates": (0,0), "HP": 150, "MP": 150}

def fill_board_coordinates_vertical(board, coords, times, generate_function):
    (start_x, start_y) = coords
    for pair in zip(range(start_x, start_x + times), [start_y] * times):
        board[pair] = generate_function


def fill_board_coordinates_horizontal(board, coords, times, generate_function):
    (start_x, start_y) = coords
    for pair in zip([start_x] * times, range(start_y, start_y + times)):
        board[pair] = generate_function

def random_event():
    random_num = random.randint(1, 100)
    if random_num < 49:
        return environment_list[0]
    elif 49 < random_num < 70:
        return environment_list[1]
    else:
        return environment_list[2]


def empty():
    return "none"

def wall():
    return "wall"


def make_board(rows, columns):
    """"
    list_of_row_number = [0] * 10
    for pair in zip(list_of_row_number, range(10)):
        board[pair].append("-")
    """
    board = {}
    for row_coordinate in range(rows):
        list_of_row_number = [row_coordinate] * rows
        for pair in zip(list_of_row_number, range(columns)):
            board[pair] = random_event
    #fill_board_coordinates_horizontal(board, (0, 0), 10, walls)
    #fill_board_coordinates_horizontal(board, (rows - 1, 0), 10, walls)
    #fill_board_coordinates_vertical(board, (0, 0), 10, walls)
    #fill_board_coordinates_vertical(board, (0, columns - 1), 10, walls)
    fill_board_coordinates_horizontal(board, (2, 2), 5, wall)
    fill_board_coordinates_horizontal(board, (5, 2), 5, wall)
    fill_board_coordinates_horizontal(board, (0, 0), 1, empty)
    return board


def print_board(board):
    for k, v in board.items():
        print(f"{k}={v()} ", end="")
        if k[1] == 9:
            print("\n")

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

def main():
    """
    Drives the program.
    """
    my_board = make_board(10, 10)
    print_board(my_board)
    print(make_character("Collin"))


if __name__ == "__main__":
    main()