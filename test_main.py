# test_main.py
import unittest
from main import greeting

class TestMain(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(greeting("User"), "Hello, User! Welcome to Jenkins CI/CD/DVD.")

if __name__ == "__main__":
    unittest.main()