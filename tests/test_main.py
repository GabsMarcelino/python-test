import unittest

from src.main import add, subtract


class MainTest(unittest.TestCase):
    def test_add(self):
        assert add(2, 3) == 5
        assert add(2, 4) == 6

    def test_subtract(self):
        assert subtract(2, 3) == -1
        assert subtract(2, 4) == -2

if __name__ == '__main__':
    unittest.main()
