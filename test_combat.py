from unittest import TestCase
from unittest.mock import patch
from game import *


class TestCombat(TestCase):
    @patch('random.randint', return_value=45)
    def test_effect_the_enemy_combat_skill_alive(self, random_number_generator):
        test_character = make_character("John")
        enemy = {"type": "elite duelist", "HP": 300, "damage range": [40, 65], "exp gained": 25}
        skill = "DARK MAGICIAN GIRL"
        self.assertEqual(effect_the_enemy(enemy, test_character, skill), False)
        self.assertEqual(enemy["HP"], 300 - 45)

    @patch('random.randint', return_value=45)
    def test_effect_the_enemy_combat_skill_dead(self, random_number_generator):
        test_character = make_character("John")
        enemy = {"type": "elite duelist", "HP": 40, "damage range": [40, 65], "exp gained": 25}
        skill = "DARK MAGICIAN GIRL"
        self.assertEqual(effect_the_enemy(enemy, test_character, skill), True)
        self.assertEqual(enemy["HP"], 0)

    @patch('random.randint', return_value=45)
    def test_effect_the_enemy_heal_skill(self, random_number_generator):
        test_character = make_character("John")
        enemy = {"type": "elite duelist", "HP": 300, "damage range": [40, 65], "exp gained": 25}
        skill = "SCAPEGOAT"
        self.assertEqual(effect_the_enemy(enemy, test_character, skill), False)
        self.assertEqual(enemy["HP"], 300)

    @patch('random.randint', return_value=45)
    def test_effect_the_character_combat_skill_alive(self, random_number_generator):
        test_character = make_character("John")
        enemy = {"type": "elite duelist", "HP": 40, "damage range": [40, 65], "exp gained": 25}
        skill = "DARK MAGICIAN GIRL"
        effect_the_character(enemy, test_character, skill)
        self.assertEqual(test_character["CURRENT HP"], 55)

    @patch('random.randint', return_value=45)
    def test_effect_the_character_combat_skill_dead(self, random_number_generator):
        test_character = make_character("John")
        test_character["CURRENT HP"] = 20
        enemy = {"type": "elite duelist", "HP": 40, "damage range": [40, 65], "exp gained": 25}
        skill = "DARK MAGICIAN GIRL"
        effect_the_character(enemy, test_character, skill)
        self.assertEqual(test_character["CURRENT HP"], 0)

    @patch('random.randint', return_value=45)
    def test_effect_the_character_heal_skill(self, random_number_generator):
        test_character = make_character("John")
        test_character["CURRENT HP"] = 20
        enemy = {"type": "elite duelist", "HP": 40, "damage range": [40, 65], "exp gained": 25}
        skill = "SCAPEGOAT"
        effect_the_character(enemy, test_character, skill)
        self.assertEqual(test_character["CURRENT HP"], 20 + 45 - 45)

    def test_update_game_state_boss_is_a_boss(self):
        enemy = {"type": "boss", "HP": 100000, "damage range": [9000, 10000], "exp gained": 0}
        update_game_state_boss(enemy)
        self.assertEqual(enemy["damage range"], [70, 100])

    """
    # Don't know how to test when input is needed from a helper function

    @patch('builtins.input', side_effect=["1"])
    @patch('random.sample', return_value=("DARK MAGICIAN", "BLUE-EYES WHITE DRAGON", "GOBLIN'S SECRET REMEDY",
                                          "RED-EYES BLACK DRAGON", "DARK MAGICIAN GIRL", "BLUE-EYES ULTIMATE DRAGON",
                                          "KURIBOH", "SCAPEGOAT", "JINZO", "DIAN KETO THE CURE MASTER",
                                          "CELTIC GUARDIAN", "MAN-EATER BUG", "BUSTER BLADER", "TOON WIZARD"))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_execute_challenge_protocol_value_exception(self, mock_output, random_sample, mock_input):
        test_character = make_character("John")
        current_environment = ("elite duelist", "?", "Oh my! An elite duelist approaches you")
        enemies = enemies_init()
        test_character["cards allowed"] = 50
        execute_challenge_protocol(test_character, current_environment, enemies)
    """
