# -*- coding: utf-8 -*-
from card import Card;
from random import shuffle;

class Deck:
    SUITS = ['S', 'H', 'D', 'C']
    RANKS = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    def __init__(self):
        self.cards = list()
        for s in Deck.SUITS:
            for r in Deck.RANKS:
                self.cards.append(Card(s,r))
        shuffle(self.cards)
        print self.cards

    def isEmpty(self):
        return len(self.cards) == 0;

    def drawCards(self, number):
        ret = list()
        for i in range(0,number):
            if len(self.cards) > 0:
                drawnCard = self.cards.pop(0)
                print "\t\tDrawn from deck", drawnCard
                ret.append(drawnCard)
        return ret
