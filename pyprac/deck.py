import sys
from random import randint

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def rankNumToStr(self, rank):
        if rank == 1:
            return "A"
        if rank == 11:
            return "J"
        if rank == 12:
            return "Q"
        if rank == 13:
            return "K"
        
        return rank
    
    def suitStrToSym(self, suit):
        if suit == "Spades":
            return u"\u2660"
        if suit == "Hearts":
            return u"\u2661"
        if suit == "Clubs":
            return u"\u2663"
        if suit == "Diamonds":
            return u"\u2662"
        
        return suit
       
    def printCard(self):
        print(self.suit, self.rank)
    def __str__(self):
        return self.suitStrToSym(self.suit) + " " + str(self.rankNumToStr(self.rank))


class Shuffle:
    def fisherShuffle(l):
    for i in range(len(l)):
        r = randint(0, 3)
        swap = l[i]
        l[i] = l[r]
        l[r] = swap
    return l
        
class Deck(Shuffle):
    def __init__(self):
        self.l = []
        self.suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        for i in range(1, 14):
            self.suits = fisherShuffle(self.suits)
            for suit in self.suits:
                self.l.append(Card(suit, i))
                
#         self.shuffle()
        return
    
    def shuffle(self):
        for i in range(len(self.l)):
            randNum = randint(0, 51)
            card_i = self.l[randNum]
            self.l[randNum] = self.l[i]
            self.l[i] = card_i
        
      
    def printDeck(self):
        for i in self.l:
            print(i)
deck1 = Deck()
deck1.shuffle()
print(deck1.printDeck())


    