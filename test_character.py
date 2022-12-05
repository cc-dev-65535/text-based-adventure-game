from unittest import TestCase
from game import *


class TestCharacter(TestCase):
    def test_boss_dead_true(self):
        test_character = make_character("John")
        test_character["boss killed"] = True
        self.assertEqual(boss_dead(test_character), True)

    def test_boss_dead_false(self):
        test_character = make_character("John")
        self.assertEqual(boss_dead(test_character), False)

    def test_is_alive_true(self):
        test_character = make_character("John")
        self.assertEqual(is_alive(test_character), True)

    def test_is_alive_negative(self):
        test_character = make_character("John")
        test_character["CURRENT HP"] = -50
        self.assertEqual(boss_dead(test_character), False)

    def test_is_alive_zero(self):
        test_character = make_character("John")
        test_character["CURRENT HP"] = 0
        self.assertEqual(boss_dead(test_character), False)
