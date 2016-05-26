from deck import Deck;

class Game:
    PHASE_STATUS_DEFENDED = 0
    PHASE_STATUS_SURRENDERED = 1
    def __init__(self):
        self.deck = Deck();
        self.players = list();
        self.activePlayer = 0;

    def addPlayer(self, player):
        self.players.append(player);

    def start(self):
        print "Dealing cards"
        self.deal();
        self.printCards()
        print "Starting game"
        while not self.finished():
            outcome = self.phase();
            print "~~~~~~~~~ PHASE COMPLETED ~~~~~~~~~";
            self.fullFillHands();
            self.nextPlayer(outcome);
        print "Player ", self.activePlayer, "won"

    def nextPlayer(self, outcome):
        if outcome == Game.PHASE_STATUS_DEFENDED:
            self.activePlayer = self.nextPlayerIndex()

    def deal(self):
        for player in self.players:
            player.giveCards(self.deck.drawCards(6));

    def printCards(self):
        print "================= HUMAN ============="
        self.players[0].printCards()
        print "================= BOT ============="
        self.players[1].printCards()

    def phase(self):
        self.table = list();
        while True:
            if not self.canAttack():
                return Game.PHASE_STATUS_DEFENDED;
            self.lastCard = self.attack();
            if not self.canDefend():
                print "Can't defend from", self.lastCard
                self.takeTable();
                return Game.PHASE_STATUS_SURRENDERED;
            self.lastCard = self.defend();

    def defend(self):
        defendingCard = self.defendingPlayer().defend(self.lastCard);
        self.table.append(defendingCard);
        return defendingCard;

    def fullFillHands(self):
        for player in self.players:
            player.giveCards(self.deck.drawCards(player.shouldTake()));

    def takeTable(self):
        self.defendingPlayer().giveCards(self.table);
        self.table = list();

    def nextPlayerIndex(self):
        if self.activePlayer == 0:
            return 1;
        else:
            return 0;

    def defendingPlayer(self):
        return self.players[self.nextPlayerIndex()];

    def canAttack(self):
        if len(self.table) == 0:
            return True
        else:
            return self.attackingPlayer().canAttack(self.table);

    def attackingPlayer(self):
        return self.players[self.activePlayer];

    def canDefend(self):
        defendingPlayer = self.defendingPlayer();
        return defendingPlayer.willDefendFrom(self.lastCard);

    def attack(self):
        attackingPlayer = self.players[self.activePlayer];
        attackingCard = attackingPlayer.selectAttackingCard(self.table);
        print "Attacking with", attackingCard
        attackingPlayer.removeCard(attackingCard);
        self.addCardToTable(attackingCard);
        print "Player", self.activePlayer, "put", attackingCard
        return attackingCard;

    def addCardToTable(self, card):
        self.table.append(card);

    def deckIsEmpty(self):
        return self.deck.isEmpty()

    def finished(self):
        if not self.deckIsEmpty():
            return False;
        for player in self.players:
            if player.hasNoCards():
                return True;
        return False;
