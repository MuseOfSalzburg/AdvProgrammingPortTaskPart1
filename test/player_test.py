import unittest
from app.player import Player


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.test_instance = Player("42", "C00L_G4M3R")

    def test_uid_function(self):
        self.assertEqual(self.test_instance.uid, "42")

    def test_name_function(self):
        self.assertEqual(self.test_instance.name, "C00L_G4M3R")


if __name__ == '__main__':
    unittest.main()
