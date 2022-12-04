from unittest import TestCase
from unittest.mock import patch
from game import *


class TestEnvironments(TestCase):
    @patch('random.choice', return_value=("strong duelist", "?", "Oh no! A strong duelist approaches you"))
    def test_random_event(self, random_choice):
        test_character = make_character("John")
        random_event(test_character)
        self.assertEqual(random_event(test_character),
                         ("strong duelist", "?", "Oh no! A strong duelist approaches you"))

    @patch('random.choice', return_value=("", "!", "The sound of duelists is deafening"))
    def test_cool_description(self, random_choice):
        test_character = make_character("John")
        cool_description(test_character)
        self.assertEqual(random_event(test_character),
                         ("", "!", "The sound of duelists is deafening"))

    def test_is_battle_environment_is(self):
        self.assertEqual(is_battle_environment(("weak duelist", "?", "Yikes! A weak duelist approaches you")),
                         True)

    def test_is_battle_environment_is_not(self):
        self.assertEqual(is_battle_environment(("wall", "%", "a wall that towers over you")),
                         False)