from entities.HandValue import HandValue


class HandCalculator:
    sevenCards = []
    score = {}
    pairDictionary = {
        14: 0,
        13: 0,
        12: 0,
        11: 0,
        10: 0,
        9: 0,
        8: 0,
        7: 0,
        6: 0,
        5: 0,
        4: 0,
        3: 0,
        2: 0
    }

    def bestHand(self, handofcards, river):

        # reset score for each new calculation
        self.score = {
            "handvalue": HandValue.highcard,
            "higestCard": 0,
            'winningcombination': 0
        }

        for Card in handofcards:
            self.sevenCards.append(Card)
        for Card in river:
            self.sevenCards.append(Card)
        for Card in self.sevenCards:
            self.pairDictionary[Card.value] += 1

        # player has a pair
        hasPair = self.hasPair(self.sevenCards)
        if hasPair != None:
            return hasPair

        # player has a highcard
        return self.hasHighCard(self.sevenCards)

    def hasPair(self, sevenCards):
        higestCard = 0

        for pairvalues in self.pairDictionary.values():
            if pairvalues >= 2:
                self.score["handvalue"] = HandValue.pair
                self.score["winningcombination"] = pairvalues

                for Card in sevenCards:
                    if Card.value > higestCard:
                        higestCard = Card.value

                self.score["higestCard"] = higestCard
                return self.score
            else:
                return None

    def hasHighCard(self, sevenCards):
        higestCard = 0

        for Card in sevenCards:
            if Card.value > higestCard:
                higestCard = Card.value

        self.score["handvalue"] = HandValue.highcard
        self.score["winningcombination"] = higestCard
        return self.score

    # def hasroyalflush(self, handofcards, river):
