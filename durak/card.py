# -*- coding: utf-8 -*-
class Card:
    SUITS = ['S', 'H', 'D', 'C']
    RANKS = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    SUITS_PRINTABLE = ['♠', '♥', '♦', '♣']

    def __init__(self, suit, rank):
        self.suit = suit;
        self.rank = rank;

    def __repr__(self):
        return self.rank + self.printable_suit(self.suit)

    def printable_suit(self, suit):
        return Card.SUITS_PRINTABLE[Card.SUITS.index(suit)]

    def greaterThan(self, card):
        return self.suit == card.suit and Card.RANKS.index(self.rank) > Card.RANKS.index(card.rank)

    def sameRank(self, card):
        return self.rank == card.rank;
