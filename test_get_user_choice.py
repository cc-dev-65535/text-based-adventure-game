from unittest import TestCase
from unittest.mock import patch
from game import *


class TestUserChoice(TestCase):
    @patch('builtins.input', side_effect=["3"])
    def test_get_user_choice_directions(self, mock_input):
        self.assertEqual(get_user_choice(("NORTH", "EAST", "SOUTH", "WEST", "MAP", "QUIT")),
                         "SOUTH")

    @patch('builtins.input', side_effect=["2"])
    def test_get_user_choice_skills(self, mock_input):
        self.assertEqual(get_user_choice(("DARK MAGICIAN", "BLUE-EYES WHITE DRAGON", "GOBLIN'S SECRET REMEDY")),
                         "BLUE-EYES WHITE DRAGON")

    """
    # Don't know how to test invalid input in cases where the function doesn't return.

    @patch('builtins.input', side_effect=["7"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_invalid(self, mock_output, mock_input):
        get_user_choice(("NORTH", "EAST", "SOUTH", "WEST", "MAP", "QUIT"))
        printed_this = mock_output.getvalue()
        expected_output = "Invalid input, make another selection:\n" \
                          "1. NORTH\n2. EAST\n3. SOUTH\n4. WEST\n5. MAP\n6. QUIT\n"
        self.assertEqual(expected_output, printed_this)
    """