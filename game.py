"""
Robert Oh
A01321210
"""
#MORE NOTES
#name chris
#level 1
#make_character returns dictionary?
# {"status": {"hp" : , "mp": , "level" : }}
#describe current location returns
#get user choice uses a enumerated list and returns a
#check for challenges returns true or false
#character carreis around a dictionary that is basically it's global status
#once boss is beaten, leave the main game loop;
# to move, the game prints out a list for us and we select an element out of it
# make_board returns a dictionary?? Yes, it returns a dictionary with tuples/coordinates as keys?
# combat: combat_was_a_success function causes player level ups
# probability of encounters is 20% at beignning

#make_board example
# def make_board(rows, columns):
#     board = {}
#     for row in rows:
#         for column in columns:
#             board[(row,columns)] = "something is in this coordinate"

# add .idea/ to git ignore

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


def fill_board_coordinates_vertical_walls(board, start, rows, times):
    list_of_column_number = [start] * times
    for pair in zip(range(rows, times), list_of_column_number):
        board[pair] = ["|"]


def fill_board_coordinates_horizontal_walls(board, start, columns, times):
    list_of_row_number = [start] * times
    for pair in zip(list_of_row_number, range(columns, times)):
        print(pair)
        board[pair] = ["-"]


def init_board(board):
    """"
    list_of_row_number = [0] * 10
    for pair in zip(list_of_row_number, range(10)):
        board[pair].append("-")
    """
    fill_board_coordinates_horizontal_walls(board, 0, 0, 10)
    fill_board_coordinates_horizontal_walls(board, 9, 0, 10)
    fill_board_coordinates_vertical_walls(board, 0, 0, 10)
    fill_board_coordinates_vertical_walls(board, 9, 0, 10)


def make_board(row, column):
    board = {}
    for row_coordinate in range(row):
        list_of_row_number = [row_coordinate] * row
        for pair in zip(list_of_row_number, range(column)):
            board[pair] = [" "]
    return board


def print_board(board):
    for k, v in board.items():
        print(f"{k}={v} ", end="")
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
    init_board(my_board)
    print_board(my_board)


if __name__ == "__main__":
    main()