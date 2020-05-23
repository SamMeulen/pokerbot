from entities.Deck import Deck
from entities.HandValue import HandValue
from entities.HandCalculator import HandCalculator
from entities.ValueType import ValueType

deck = Deck()
deck.createDeck()
handOfCards1 = []
handOfCards2 = []
river = []
handValue1 = HandValue.highcard
handValue2 = HandValue.highcard
calculator = HandCalculator()
score1 = {}
score2 = {}

# deal 2 cards to each player
for i in range(0, 2):
    handOfCards1.append(deck.dealCard())
    handOfCards2.append(deck.dealCard())

# deal 5 cards to the river
for i in range(0, 5):
    river.append(deck.dealCard())

print('player 1')
for card in handOfCards1:
    print(card.suit + " " + str(card.value))
print('=========')
print('player 2')
for card in handOfCards2:
    print(card.suit + " " + str(card.value))
print('=========')
print('river')
for card in river:
    print(card.suit + " " + str(card.value))
print('=========')

score1 = calculator.bestHand(handOfCards1, river)
score2 = calculator.bestHand(handOfCards2, river)

if score1.get("handvalue").value > score2.get("handvalue").value:
    print('player1 wins with ' + score1.get("handvalue").name + ' ' + ValueType(score1.get("winningcombination")).name)
elif score1.get("handvalue").value < score2.get("handvalue").value:
    print('player2 wins with ' + score2.get("handvalue").name + ' ' + ValueType(score2.get("winningcombination")).name)
else:
    if score1.get("winningcombination") > score2.get("winningcombination"):
        print('player1 wins with ' + score1.get("handvalue").name + ' ' + ValueType(score1.get("winningcombination")).name)
    elif score1.get("winningcombination") < score2.get("winningcombination"):
        print('player2 wins with ' + score2.get("handvalue").name + ' ' + ValueType(score2.get("winningcombination")).name)
    else:
        print(
            'draw: both players have ' + score2.get("handvalue").name + ' ' + ValueType(score1.get("winningcombination")).name)
