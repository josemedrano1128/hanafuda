# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 22:54:45 2018

@author: Jose
"""

class Card:
    def __init__(self, name, nameId, monthId, flower, value):
        self.name = name
        self.nameId = nameId
        self.monthId = monthId
        self.flower = flower
        self.value = value
    
    def __str__(self):
        return "%s, %s, %s" % (self.name, self.flower, self.value)
    
    def __repr__(self):
        return "Card(%s, %s, %s, %s, %s)" % (self.name, self.nameId, self.monthId, self.flower, self.value) 


jan001 = Card("Crane", "jan001", 1, "pine", 20)
jan002 = Card("Pine Poetry Ribbon", "jan002", 1, "pine", 5)
jan003 = Card("Pine 1", "jan003", 1, "pine", 1)
jan004 = Card("Pine 2", "jan004", 1, "pine", 1)
feb001 = Card("Warbler", "feb001", 2, "plum", 10)
feb002 = Card("Plum Poetry Ribbon", "feb002", 2, "plum", 5)
feb003 = Card("Plum 1", "feb003", 2, "plum", 1)
feb004 = Card("Plum 2", "feb004", 2, "plum", 1)
mar001 = Card("Blossom Banner", "mar001", 3, "blossom", 20)
mar002 = Card("Blossom Poetry Ribbon", "mar002", 3, "blossom", 5)
mar003 = Card("Blossom 1", "mar003", 3, "blossom", 1)
mar004 = Card("Blossom 2", "mar004", 3, "blossom", 1)
apr001 = Card("Cuckoo", "apr001", 4, "wisteria", 10)
apr002 = Card("Wisteria Red Ribbon", "apr002", 4, "wisteria", 5)
apr003 = Card("Wisteria 1", "apr003", 4, "wisteria", 1)
apr004 = Card("Wisteria 2", "apr004", 4, "wisteria", 1)
may001 = Card("Water Iris", "may001", 5, "iris", 10)
may002 = Card("Iris Red Ribbon", "may002", 5, "iris", 5)
may003 = Card("Iris 1", "may003", 5, "iris", 1)
may004 = Card("Iris 2", "may004", 5, "iris", 1)
jun001 = Card("Butterflies", "jun001", 6, "peony", 10)
jun002 = Card("Peony Blue Ribbon", "jun002", 6, "peony", 5)
jun003 = Card("Peony 1", "jun003", 6, "peony", 1)
jun004 = Card("Peony 2", "jun004", 6, "peony", 1)
jul001 = Card("Boar", "jul001", 7, "clover", 10)
jul002 = Card("Clover Red Ribbon", "jul002", 7, "clover", 5)
jul003 = Card("Clover 1", "jul003", 7, "clover", 1)
jul004 = Card("Clover 2", "jul004", 7, "clover", 1)
aug001 = Card("Moon", "aug001", 8, "suzuki", 20)
aug002 = Card("Geese", "aug002", 8, "suzuki", 10)
aug003 = Card("Suzuki 1", "aug003", 8, "suzuki", 1)
aug004 = Card("Suzuki 2", "aug004", 8, "suzuki", 1)
sep001 = Card("Sake Cup", "sep001", 9, "chrysanthemum", 10)
sep002 = Card("Chrys Blue Ribbon", "sep002", 9, "chrysanthemum", 5)
sep003 = Card("Chrys 1", "sep003", 9, "chrysanthemum", 1)
sep004 = Card("Chrys 2", "sep004", 9, "chrysanthemum", 1)
oct001 = Card("Deer", "oct001", 10, "maple", 10)
oct002 = Card("Maple Blue Ribbon", "oct002", 10, "maple", 5)
oct003 = Card("Maple 1", "oct003", 10, "maple", 1)
oct004 = Card("Maple 2", "oct004", 10, "maple", 1)
nov001 = Card("Rain Man", "nov001", 11, "willow", 20)
nov002 = Card("Willow Red Ribbon", "nov002", 11, "willow", 5)
nov003 = Card("Willow 1", "nov003", 11, "willow", 1)
nov004 = Card("Lightning", "nov004", 11, "willow", 1)
dec001 = Card("Phoenix", "dec001", 12, "paulownia", 20)
dec002 = Card("Paul 1", "dec002", 12, "paulownia", 1)
dec003 = Card("Paul 2", "dec003", 12, "paulownia", 1)
dec004 = Card("Paul 3", "dec004", 12, "paulownia", 1)


if __name__ == "__main__":
    print(jan001)
    print(repr(jan001))

    
 