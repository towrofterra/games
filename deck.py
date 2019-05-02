import abc
import random


class Deck:
    # Initializes the deck with a dictionary of cards
    def __init__(self, num_jokers):
        self.cards = {}
        self.num_cards = 0

        def add_cards(suit, num):
            for i in range(1, num+1):
                self.cards[self.num_cards] = Card(i, suit)
                self.num_cards += 1

        add_cards('h', 13)
        add_cards('c', 13)
        add_cards('d', 13)
        add_cards('s', 13)

        for i in range(0, num_jokers):
            self.cards[self.num_cards] = Joker()
            self.num_cards += 1

    def shuffle(self):
        random.shuffle(self.cards, random.random)
        # for c in self.cards.values():
        #     print(c)


class ACard(abc.ABC):
    # Abstract class for all types of cards
    @abc.abstractmethod
    def __str__(self):
        pass

    @abc.abstractmethod
    def __eq__(self, other):
        pass


class Card(ACard):
    # Value represents the face value of the card, A being 1, J-K being 11-13
    # Suit represents the suit of the card (char, initial of the suit)
    suits = {'s': "Spades", 'c': "Clubs", 'h': "Hearts", 'd': "Diamonds"}
    values = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}

    # Initializes this card. Raises an AttributeError if values aren't valid
    def __init__(self, value, suit):
        if suit not in self.suits or 1 > value or 13 < value:
            raise AttributeError
        self.value = value
        self.suit = suit

    # Returns the string representation of this card
    def __str__(self):
        return "{} of {}".format(self.values.get(self.value, self.value), self.suits.get(self.suit, self.suit))

    # Equality function
    def __eq__(self, other):
        if isinstance(other, Card):
            return other.value == self.value and other.suit == self.suit
        return False


class Joker(ACard):
    # Special class to represent a Joker card

    # Returns the string representation of this card
    def __str__(self):
        return "Joker"

    # Equality function
    def __eq__(self, other):
        return isinstance(other, Joker)
