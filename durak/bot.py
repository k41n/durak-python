from player import Player;

class Bot(Player):
    def __init__(self):
        Player.__init__(self);

    def willDefendFrom(self, card):
        for candidate in self.hand:
            if candidate.greaterThan(card):
                return True;
        return False;

    def defend(self, card):
        candidates = list();
        for candidate in self.hand:
            if candidate.greaterThan(card):
                candidates.append(candidate);
        minCandidate = candidates[0];
        for candidate in candidates:
            if minCandidate.greaterThan(candidate):
                minCandidate = candidate;
        print "Defending with", minCandidate;
        return minCandidate;

    def selectAttackingCard(self, table):
        if len(table) == 0:
            return self.hand[0];
        for card in self.hand:
            for tableCard in table:
                if card.sameRank(tableCard):
                    return card;
