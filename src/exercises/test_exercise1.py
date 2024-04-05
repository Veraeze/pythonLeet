import unittest
from unittest import TestCase
from exercise1 import convert


class MyTestCase(TestCase):
    def test_something(self):
        output = convert("2,3,5")
        self.assertEqual(output, [4, 9, 25])  # add assertion here


if __name__ == '__main__':
    unittest.main()
