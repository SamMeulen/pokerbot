import random
from entities.Card import Card


class Deck:
    suitList = ['hearts', 'spades', 'diamonds', 'clubs']
    valueList = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    cardList = []

    def createDeck(self):
        for suit in self.suitList:
            for value in self.valueList:
                self.cardList.append(Card(suit, value))

    def dealCard(self):
        card = random.choice(self.cardList)
        self.cardList.remove(card)
        return card
