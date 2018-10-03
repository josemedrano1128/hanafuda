# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 23:38:43 2018

@author: Jose
"""

from random import shuffle
from time import sleep
import cards


#work on this class is pending
class CardCollection:
    #I think this is the real solution, since so many of these classes have similar methods.
    #still need to implement this in the other classs
    #__slots__ = ["contents"]
    
    def __init__(self, contents=None):
        if contents is None:
            self.contents = []
        else:
            self.contents = contents
    
    def __len__(self):
        return len(self.contents)
    
    def shuffle(self):
        """Shuffles the deck contents"""
        #repeating this function name might be a bad idea but scope saving me
        #it's not actually scope; it's the fact that I call the standalone function 
        #instead of Deck.shuffle()
        shuffle(self.contents)

    def __repr__(self):
        return "{}({})".format(type(self).__name__,self.contents)
    
    def __str__(self):
        return "{}({})".format(type(self).__name__,[card.name for card in self.contents])
    
    def sort(self):
        self.contents.sort()

    

class Deck(CardCollection):
    #contents will be ordered from [top->bottom] for simplicity
    
    #__slots__ = ["_collection"]
    
    def __init__(self, contents=None):
        CardCollection.__init__(self, contents)
        #self._collection = CardCollection(contents)

    def pop(self, number=1):
        """returns the top n cards in the deck and erases them as part of self.contents"""
        cardsToDeal,self.contents = self.contents[:number],self.contents[number:]
        return cardsToDeal


class Hand(CardCollection):
    
    def __init__(self, contents=None):
        CardCollection.__init__(self, contents)
    
    def play(self, cardIndex):
        cardToPlay = self.contents.pop(cardIndex)
        return cardToPlay
    
class CenterBoard(CardCollection):
    __slots__ = ["awaitingRelease"]
    
    def __init__(self, contents=None):
        CardCollection.__init__(self, contents)
    
    def accept(self, cardPlayed):
        #and return a value if hiki/match is achieved?
        matchList = list(filter(lambda card: card.monthId == cardPlayed.monthId, self.contents))
        if len(matchList) == 0:
            self.contents += [cardPlayed]
            return 0
        if len(matchList) == 1:
            self.contents.remove(matchList[0])
            self.awaitingRelease = [matchList[0],cardPlayed]
            return 1
        #stuff for displaying options here

    def release(self, cards):
        #release to scoring area
        awaitingRelease,self.awaitingRelease = self.awaitingRelease, []
        return awaitingRelease
    
    def __str__(self):
        return str([card.name.strip("'") for card in self.contents])
    
    #def __repr__(self):
     #   return str(self.contents)
    
    

class ScoringArea:
    
    __slots__ = ["contents"]
    
    def __init__(self):
        self.contents = {"20" : [], "10" : [], "5": [], "1": []}
    
    def accept(self, cards):
        """Accepts any number of cards given at a time and puts them in the appropriate score areas"""
        #Uses the values as the dictionary key, as that is how cards are stored in physical score areas
        #scoring work itself should be done by the Manager
        for card in cards:
            self.contents[str(card.value)].append(card)


class Manager:
    pass



if __name__ == "__main__":
    """
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
    """
    gameDeck = Deck(cards.getDeck())
    print("Deck initialized...shuffling\n")
    sleep(2)
    gameDeck.shuffle()
    #print("Printing Deck...\n")
    #print(gameDeck)
    print("Dealing...\n")
    hand1 = Hand(gameDeck.pop(8))
    hand1.sort()
    hand2 = Hand(gameDeck.pop(8))
    hand2.sort()
    sleep(2)
    print("Hands have been dealt.\n")
    sleep(1)
    print("Dealing to Center Board...\n")
    center = CenterBoard(gameDeck.pop(8))
    sleep(2)
    print("Center Board:")
    print(center)
    print("\nGame is ready to begin. Proceed.")
    