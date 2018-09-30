# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 23:38:43 2018

@author: Jose
"""

from random import shuffle
import cards


#work on this class is pending
class Deck:
    #contents will be ordered from [top->bottom] for simplicity
    
    __slots__ = ["contents"]
    
    def __init__(self, contents=None):
        if contents is None:
            self.contents = []
        else:
            self.contents = contents
    
    def pop(self, number=1):
        """returns the top n cards in the deck and erases them as part of self.contents"""
        cardsToDeal,self.contents = self.contents[:number],self.contents[number:]
        return cardsToDeal
        
        
    
    def shuffle(self):
        """Shuffles the deck contents"""
        #repeating this function name might be a bad idea but scope saving me
        shuffle(self.contents)

    def __repr__(self):
        return "Deck({})".format(self.contents)


class Hand:
    #this is almost a subclass of Deck...I should consider making it one
    __slots__ = ["contents"]
    
    def __init__(self, contents):
        self.contents = contents
    
    def play(self, cardIndex):
        cardToPlay = self.contents.pop(cardIndex)
        return cardToPlay
    
    def __repr__(self):
        return "Hand({})".format(self.contents)
    
    def sort(self):
        self.contents.sort()
    
class CenterBoard:
    pass


class ScoringArea:
    pass


class Manager:
    pass



if __name__ == "__main__":
    print(cards.getCard("jan001"))
    myDeck = Deck([0,1,2,3,4,5])
    print(myDeck)
    myDeck.shuffle()
    print(myDeck)
    hand = Hand(myDeck.pop(3))
    print(hand)
    a = hand.play(1)
    print(hand)
    print(a)
    
    print("\nThe real tests start now...\n")
    
    realDeck = Deck(cards.getDeck())
    print(realDeck)
    print("\n")
    realDeck.shuffle()
    print(realDeck)
    print("\n")
    hand1 = Hand(realDeck.pop(8))
    hand2 = Hand(realDeck.pop(8))
    print(hand1)
    print("\n")
    hand1.sort()
    print(hand1)
    print("\n")
    print(hand2)
    print("\n")
    hand2.sort()
    print(hand2)