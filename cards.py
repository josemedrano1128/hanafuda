# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 22:54:45 2018

@author: Jose
"""

class Card:
    """A hanafuda card object, described by its traditional name
    and unique ID, numeric month ID, flower, and point value"""
    #I should probably add subclasses for each month? Might just be a case of over-specifying
    __slots__ = ["name", "nameId", "monthId", "flower", "value"]
    
    def __init__(self, name, nameId, monthId, flower, value):
        self.name = name
        self.nameId = nameId
        self.monthId = monthId
        self.flower = flower
        self.value = value
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        #change this to new style formatting 
        return "Card({}, {}, {}, {}, {})".format(self.name, self.nameId, self.monthId, self.flower, self.value) 
    
    def __lt__(self, other):
        if self.monthId > other.monthId:
            return False
        if self.monthId < other.monthId:
            return True
        if self.value > other.value:
            return True
        if self.nameId < other.nameId:
            return True
        return False

    def __eq__(self, other):
        if self.monthId == other.monthId and self.value == other.value and self.nameId == other.nameId:
            return True
        return False

    def __gt__(self, other):
        if not self.__eq__(other):
            return not self.__lt__(other)
    
    def __le__(self, other):
        return (self.__lt__(other) or self.__eq__(other))
    
    def __ge__(self, other):
        return (self.__gt__(other) or self.__eq__(other))
    


#The following is a standard hanafuda deck.
_jan001 = Card("Crane", "jan001", 1, "pine", 20)
_jan002 = Card("Pine Poetry Ribbon", "jan002", 1, "pine", 5)
_jan003 = Card("Pine 1", "jan003", 1, "pine", 1)
_jan004 = Card("Pine 2", "jan004", 1, "pine", 1)
_feb001 = Card("Warbler", "feb001", 2, "plum", 10)
_feb002 = Card("Plum Poetry Ribbon", "feb002", 2, "plum", 5)
_feb003 = Card("Plum 1", "feb003", 2, "plum", 1)
_feb004 = Card("Plum 2", "feb004", 2, "plum", 1)
_mar001 = Card("Blossom Banner", "mar001", 3, "blossom", 20)
_mar002 = Card("Blossom Poetry Ribbon", "mar002", 3, "blossom", 5)
_mar003 = Card("Blossom 1", "mar003", 3, "blossom", 1)
_mar004 = Card("Blossom 2", "mar004", 3, "blossom", 1)
_apr001 = Card("Cuckoo", "apr001", 4, "wisteria", 10)
_apr002 = Card("Wisteria Red Ribbon", "apr002", 4, "wisteria", 5)
_apr003 = Card("Wisteria 1", "apr003", 4, "wisteria", 1)
_apr004 = Card("Wisteria 2", "apr004", 4, "wisteria", 1)
_may001 = Card("Water Iris", "may001", 5, "iris", 10)
_may002 = Card("Iris Red Ribbon", "may002", 5, "iris", 5)
_may003 = Card("Iris 1", "may003", 5, "iris", 1)
_may004 = Card("Iris 2", "may004", 5, "iris", 1)
_jun001 = Card("Butterflies", "jun001", 6, "peony", 10)
_jun002 = Card("Peony Blue Ribbon", "jun002", 6, "peony", 5)
_jun003 = Card("Peony 1", "jun003", 6, "peony", 1)
_jun004 = Card("Peony 2", "jun004", 6, "peony", 1)
_jul001 = Card("Boar", "jul001", 7, "clover", 10)
_jul002 = Card("Clover Red Ribbon", "jul002", 7, "clover", 5)
_jul003 = Card("Clover 1", "jul003", 7, "clover", 1)
_jul004 = Card("Clover 2", "jul004", 7, "clover", 1)
_aug001 = Card("Moon", "aug001", 8, "suzuki", 20)
_aug002 = Card("Geese", "aug002", 8, "suzuki", 10)
_aug003 = Card("Suzuki 1", "aug003", 8, "suzuki", 1)
_aug004 = Card("Suzuki 2", "aug004", 8, "suzuki", 1)
_sep001 = Card("Sake Cup", "sep001", 9, "chrysanthemum", 10)
_sep002 = Card("Chrys Blue Ribbon", "sep002", 9, "chrysanthemum", 5)
_sep003 = Card("Chrys 1", "sep003", 9, "chrysanthemum", 1)
_sep004 = Card("Chrys 2", "sep004", 9, "chrysanthemum", 1)
_oct001 = Card("Deer", "oct001", 10, "maple", 10)
_oct002 = Card("Maple Blue Ribbon", "oct002", 10, "maple", 5)
_oct003 = Card("Maple 1", "oct003", 10, "maple", 1)
_oct004 = Card("Maple 2", "oct004", 10, "maple", 1)
_nov001 = Card("Rain Man", "nov001", 11, "willow", 20)
_nov002 = Card("Willow Red Ribbon", "nov002", 11, "willow", 5)
_nov003 = Card("Willow 1", "nov003", 11, "willow", 1)
_nov004 = Card("Lightning", "nov004", 11, "willow", 1)
_dec001 = Card("Phoenix", "dec001", 12, "paulownia", 20)
_dec002 = Card("Paul 1", "dec002", 12, "paulownia", 1)
_dec003 = Card("Paul 2", "dec003", 12, "paulownia", 1)
_dec004 = Card("Paul 3", "dec004", 12, "paulownia", 1)


#is the next chunk bad practice? I feel like it's bad practice...
#
_hanafudaDict = {}
for i in ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]:
    for j in range(1,5): 
        currentIndex = "{}00{}".format(i, j)
        _hanafudaDict[currentIndex] = eval("_{}".format(currentIndex))

def getCard(nameId):
    """Returns the Hanafuda card with the given index from getCardList"""
    return _hanafudaDict[nameId]
#


def getCardList():
    """List of cards and indices to use with getCard"""
    return [[card.nameId, card.name] for card in sorted(_hanafudaDict.values())]

def getDeck():
    """returns a list of cards ready to be made into a Deck"""
    return [card for card in sorted(_hanafudaDict.values())]



#entirely for testing purposes...
if __name__ == "__main__":
    print(_jan001)
    print(repr(_jan001))
    print(_hanafudaDict["jan001"])
    print(_hanafudaDict["feb003"])
    bleh = [_jan003, _jan004, _jan001, _sep003]
    bleh.sort()
    print(bleh)
    print([str(item) for item in bleh])
    print(getCard("jan001"))
    print(repr(getCard("jan001")))
 