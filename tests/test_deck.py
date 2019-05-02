import unittest as ut
import deck
from deck import Card
from deck import Deck
from deck import Joker


class TestDeck(ut.TestCase):
    """Tests for 'Deck' functionality."""

    def test_init(self):
        cards = {
            0: Card(1, 'h'),
            1: Card(2, 'h'),
            2: Card(3, 'h'),
            3: Card(4, 'h'),
            4: Card(5, 'h'),
            5: Card(6, 'h'),
            6: Card(7, 'h'),
            7: Card(8, 'h'),
            8: Card(9, 'h'),
            9: Card(10, 'h'),
            10: Card(11, 'h'),
            11: Card(12, 'h'),
            12: Card(13,'h'),

            13: Card(1, 'c'),
            14: Card(2, 'c'),
            15: Card(3, 'c'),
            16: Card(4, 'c'),
            17: Card(5, 'c'),
            18: Card(6, 'c'),
            19: Card(7, 'c'),
            20: Card(8, 'c'),
            21: Card(9, 'c'),
            22: Card(10, 'c'),
            23: Card(11, 'c'),
            24: Card(12, 'c'),
            25: Card(13, 'c'),

            26: Card(1, 'd'),
            27: Card(2, 'd'),
            28: Card(3, 'd'),
            29: Card(4, 'd'),
            30: Card(5, 'd'),
            31: Card(6, 'd'),
            32: Card(7, 'd'),
            33: Card(8, 'd'),
            34: Card(9, 'd'),
            35: Card(10, 'd'),
            36: Card(11, 'd'),
            37: Card(12, 'd'),
            38: Card(13, 'd'),

            39: Card(1, 's'),
            40: Card(2, 's'),
            41: Card(3, 's'),
            42: Card(4, 's'),
            43: Card(5, 's'),
            44: Card(6, 's'),
            45: Card(7, 's'),
            46: Card(8, 's'),
            47: Card(9, 's'),
            48: Card(10, 's'),
            49: Card(11, 's'),
            50: Card(12, 's'),
            51: Card(13, 's'),
        }
        self.assertEqual(Deck(0).cards, cards)
        cards[52] = Joker()
        cards[53] = Joker()
        self.assertEqual(Deck(2).cards, cards)

    def test_shuffle(self):
        deck.random.random = lambda: 0.4  # A patch so that in tests the random number generated is always 0.4
        d = Deck(0)
        d.shuffle()
        d2 = Deck(0)
        d2.shuffle()
        self.assertDictEqual(d.cards, d2.cards)


class TestCard(ut.TestCase):
    """Tests for 'Card' functionality."""

    def test_print(self):
        ace_s = Card(1, 's')
        seven_h = Card(7, 'h')
        queen_d = Card(12, 'd')
        king_c = Card(13, 'c')
        two_s = Card(2, 's')

        self.assertEqual(ace_s.__str__(), "Ace of Spades")
        self.assertEqual(seven_h.__str__(), "7 of Hearts")
        self.assertEqual(queen_d.__str__(), "Queen of Diamonds")
        self.assertEqual(king_c.__str__(), "King of Clubs")
        self.assertEqual(two_s.__str__(), "2 of Spades")

    def test_init(self):
        with self.assertRaises(AttributeError):
            Card(1, 'r')
            Card(0, 'r')
            Card(0, 's')


class TestJoker(ut.TestCase):
    """Tests for 'Joker' functionality."""

    def test_print(self):
        joker = Joker()
        self.assertEqual(joker.__str__(), "Joker")


if __name__ == '__main__':
    ut.main()
