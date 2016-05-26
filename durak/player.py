class Player:
    def __init__(self):
        self.hand = list();

    def giveCards(self, cards):
        for card in cards:
            self.hand.append(card);

    def printCards(self):
        for card in self.hand:
            print card

    def removeCard(self, card):
        indx = self.hand.index(card);
        self.hand.pop(indx)
        self.printCards();

    def shouldTake(self):
        if len(self.hand) > 6:
            return 0;
        return 6 - len(self.hand);

    def canAttack(self, table):
        for card in self.hand:
            for tableCard in table:
                if card.sameRank(tableCard):
                    return True;
        return False;

    def hasNoCards(self):
        return len(self.hand) == 0;
