# content of test_class.py
import unittest

class TestClass(unittest.TestCase):
    def test_one(self):
        x = "this"
        assert "h" in x
