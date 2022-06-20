import unittest
from unittest import result
import main 

class TestCases(unittest.TestCase):

    def test_item_count(self):
        result = main.item_count_in_departments(4,2,3)
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()