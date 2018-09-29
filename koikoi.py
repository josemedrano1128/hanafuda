# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 23:38:43 2018

@author: Jose
"""

class Deck:
    __slots__ = []
    
    def __init__(self, contents):
        self.contents = contents
    
    def pop(self, number=1):
        #release top card in deck
        pass
    
    def shuffle(self):
        #randomize deck order
        pass
    
    def __str__(self):
        pass
    
    def __repr__(self):
        pass


class Hand:
    __slots__ = []
    
    def __init__(self):
        pass
    
    def play(self, card):
        pass
    
    def sort(self):
        pass
    
    
