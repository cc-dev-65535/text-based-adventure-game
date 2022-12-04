import io
from unittest import TestCase
from unittest.mock import patch
from game import *


class TestMovement(TestCase):
    def test_move_character_west(self):
        test_character = make_character("John")
        test_character["coordinates"] = (1, 1)
        self.assertEqual(move_character(test_character, "WEST"), (1, 0))

    def test_move_character_east(self):
        test_character = make_character("John")
        test_character["coordinates"] = (1, 1)
        self.assertEqual(move_character(test_character, "EAST"), (1, 2))

    def test_move_character_south(self):
        test_character = make_character("John")
        test_character["coordinates"] = (1, 1)
        self.assertEqual(move_character(test_character, "SOUTH"), (2, 1))

    def test_move_character_north(self):
        test_character = make_character("John")
        test_character["coordinates"] = (1, 1)
        self.assertEqual(move_character(test_character, "NORTH"), (0, 1))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_move_obstacle(self, mock_output):
        test_board = make_board(10, 10)
        test_character = make_character("John")
        test_character["coordinates"] = (0, 0)
        set_coordinate_state(test_board, (0, 1), wall)
        self.assertEqual(validate_move(test_board, test_character, "EAST"), False)
        printed_this = mock_output.getvalue()
        expected_output = f"Can't move there. There is a wall that towers over you\n"
        self.assertEqual(expected_output, printed_this)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_validate_move_out_of_bounds(self, mock_output):
        test_board = make_board(10, 10)
        test_character = make_character("John")
        test_character["coordinates"] = (0, 0)
        self.assertEqual(validate_move(test_board, test_character, "WEST"), False)
        printed_this = mock_output.getvalue()
        expected_output = f"Can't move there. It is outside of the convention center\n"
        self.assertEqual(expected_output, printed_this)
