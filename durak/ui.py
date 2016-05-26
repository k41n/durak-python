from player import Player;

class UI(Player):
    def __init__(self):
        Player.__init__(self);

    def selectAttackingCard(self, table):
        print "---------- YOUR CARDS: ----------"
        self.printCards()
        selected = input("Select card to move --> ")
        return self.hand[selected]

    def willDefendFrom(self, card):
        print "---------- YOUR CARDS: ----------"
        self.printCards()
        print "Will you defend? (Y/N) ",
        result = raw_input().lower();
        if result == "N":
            return True;
        else:
            return False;
