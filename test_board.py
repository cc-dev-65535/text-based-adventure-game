from unittest import TestCase
from game import *


class TestBoard(TestCase):
    def test_fill_board_coordinates_column(self):
        test_board = make_board(10, 10)
        fill_board_coordinates_column(test_board, (3, 5), 4, wall)
        self.assertNotEqual(test_board[(2, 5)], wall)
        self.assertEqual(test_board[(3, 5)], wall)
        self.assertEqual(test_board[(4, 5)], wall)
        self.assertEqual(test_board[(5, 5)], wall)
        self.assertEqual(test_board[(6, 5)], wall)
        self.assertNotEqual(test_board[(7, 5)], wall)

    def test_fill_board_coordinates_row(self):
        test_board = make_board(10, 10)
        fill_board_coordinates_row(test_board, (3, 5), 4, wall)
        self.assertNotEqual(test_board[(3, 4)], wall)
        self.assertEqual(test_board[(3, 5)], wall)
        self.assertEqual(test_board[(3, 6)], wall)
        self.assertEqual(test_board[(3, 7)], wall)
        self.assertEqual(test_board[(3, 8)], wall)
        self.assertNotEqual(test_board[(3, 9)], wall)

    def test_set_coordinate_state(self):
        test_board = make_board(10, 10)
        set_coordinate_state(test_board, (5, 6), wall)
        self.assertEqual(test_board[(5, 6)], wall)