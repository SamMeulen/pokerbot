from enum import Enum

class HandValue(Enum):
    highcard = 1
    pair = 2
    twopairs = 3
    threeofakind = 4
    straight = 5
    flush = 6
    fullhouse = 7
    fourofakind = 8
    straightflush = 9
    royalflush = 10
