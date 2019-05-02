import unittest as ut
import dice
import random


class TestDice(ut.TestCase):
    """Tests for 'dice' functionality."""

    def test_roll_given_rand(self):
        dice.random.randint = lambda n, m: 1  # A patch so that in tests the random number generated is always 1

        # 6 sided dice test
        result = dice.roll(2, 6)
        result2 = dice.roll(1, 6)
        self.assertEqual(result, [1, 1])
        self.assertEqual(result2, [1])

        # 4 sided dice test
        result = dice.roll(1, 4)
        result2 = dice.roll(3, 4)
        self.assertEqual(result, [1])
        self.assertEqual(result2, [1, 1, 1])


if __name__ == '__main__':
    ut.main()
