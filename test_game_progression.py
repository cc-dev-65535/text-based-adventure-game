import io
from unittest import TestCase
from unittest.mock import patch
from game import *


class TestGameProgression(TestCase):
    def test_item_obtained(self):
        test_character = make_character("John")
        self.assertEqual(test_character["exodia pieces"], 0)
        item_obtained(test_character)
        item_obtained(test_character)
        item_obtained(test_character)
        self.assertEqual(test_character["exodia pieces"], 3)

    def test_character_get_exp(self):
        test_character = make_character("John")
        test_enemy = {"type": "strong duelist", "HP": 200, "damage range": [25, 45], "exp gained": 25}
        self.assertEqual(test_character["CURRENT EXP"], 0)
        character_get_exp(test_character, test_enemy)
        character_get_exp(test_character, test_enemy)
        self.assertEqual(test_character["CURRENT EXP"], 50)

    @patch('random.choice', return_value=("nothing", "?", "There is nothing here, phew"))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_handle_level_up(self, mock_output, random_choice):
        test_board = make_board(10, 10)
        test_character = make_character("John")
        self.assertEqual(test_character["level"], 1)
        self.assertEqual(test_character["MAX HP"], 100)
        self.assertEqual(test_character["CURRENT HP"], test_character["MAX HP"])
        self.assertEqual(test_character["cards allowed"], 3)
        handle_level_up(test_board, test_character)  # Character is level 2
        printed_this = mock_output.getvalue()
        expected_output = r"""
        ╭╮╱╱╭━━━┳╮╱╱╭┳━━━┳╮╱╱╱╭╮╱╭┳━━━╮
        ┃┃╱╱┃╭━━┫╰╮╭╯┃╭━━┫┃╱╱╱┃┃╱┃┃╭━╮┃
        ┃┃╱╱┃╰━━╋╮┃┃╭┫╰━━┫┃╱╱╱┃┃╱┃┃╰━╯┃
        ┃┃╱╭┫╭━━╯┃╰╯┃┃╭━━┫┃╱╭╮┃┃╱┃┃╭━━╯
        ┃╰━╯┃╰━━╮╰╮╭╯┃╰━━┫╰━╯┃┃╰━╯┃┃
        ╰━━━┻━━━╯╱╰╯╱╰━━━┻━━━╯╰━━━┻╯
                                        """
        expected_output += f'\nCongratulations on leveling to level 2!\n...But you feel like you are attracting ' \
                          f'more attention from stronger duelists\n'
        self.assertEqual(expected_output, printed_this)
        self.assertEqual(test_character["CURRENT EXP"], 0)
        self.assertEqual(test_character["level"], 2)
        self.assertEqual(test_character["MAX HP"], 200)
        self.assertEqual(test_character["CURRENT HP"], test_character["MAX HP"])
        self.assertEqual(test_character["cards allowed"], 4)
        handle_level_up(test_board, test_character)  # Character is level 3, update game board
        self.assertEqual(test_board[(3, 4)](test_character), ("nothing", "?", "There is nothing here, phew"))
        self.assertEqual(test_board[(3, 5)](test_character), ("nothing", "?", "There is nothing here, phew"))

    def test_character_has_leveled(self):
        test_character = make_character("John Doe")
        test_enemy = {"type": "strong duelist", "HP": 200, "damage range": [25, 45], "exp gained": 25}
        self.assertEqual(test_character["CURRENT EXP"], 0)
        character_get_exp(test_character, test_enemy)
        character_get_exp(test_character, test_enemy)
        character_get_exp(test_character, test_enemy)
        character_get_exp(test_character, test_enemy)
        character_get_exp(test_character, test_enemy)
        character_get_exp(test_character, test_enemy)
        self.assertEqual(test_character["CURRENT EXP"], 150)
        self.assertEqual(character_has_leveled(test_character), True)
