import unittest
import decklists



deck = {
    'foo': {'maindeck': 4},
    'bar': {'maindeck': 2, 'sideboard': 2},
    'baz': {'sideboard': 2}
}

class test_join_boards(unittest.TestCase):
    def test_happy_path(self):
        maindeck = {
            'foo': {'maindeck': 4},
            'bar': {'maindeck': 2}
        }

        sideboard = {
            'bar': {'sideboard': 2},
            'baz': {'sideboard': 3}
        }
        deck = {
            'foo': {'maindeck': 4},
            'bar': {'maindeck': 2, 'sideboard': 2},
            'baz': {'sideboard': 2}
        }
        combined = decklists.join_boards(maindeck, sideboard)
        self.assertDictEqual(combined,deck)