from unittest import TestCase
from even import is_even


class Test(TestCase):
    def test_is_even(self):
        sample_input = [4, 5, 8, 8, 8, 2, 9]
        output = is_even(sample_input)

        self.assertEqual([0, 1, 0, 0, 0, 0, 1], output)  # add assertion here
