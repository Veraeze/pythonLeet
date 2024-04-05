import unittest
from unittest import TestCase
from src.scanner.scanner_class import Scanner

scan = Scanner()


class TestScanner(TestCase):
    def test_nextInt(self):
        print("Enter a number: ")  # 5
        first_input = scan.nextInt()
        print("Enter a number: ")  # 2
        second_input = scan.nextInt()
        result = first_input * second_input

        self.assertEqual(10, result)  # add assertion here

    def test_nextDouble(self):
        print("Enter a number: ")  # 2.5
        first_input = scan.nextDouble()
        print("Enter a number: ")  # 1.6
        second_input = scan.nextDouble()
        result = first_input + second_input

        self.assertEqual(4.1, result)  # add assertion here

    def test_nextLine(self):
        print("Enter a word: ")  # come
        first_input = scan.nextLine()
        print("Enter a word: ")  # go
        second_input = scan.nextLine()
        result = first_input + second_input

        self.assertEqual("comego", result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
