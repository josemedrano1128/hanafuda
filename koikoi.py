# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 23:38:43 2018

@author: Jose
"""

import collections

#work on this class is pending
class Deck(collections.MutableSequence):
    #does this even need to be its own class, now that I think about it? 

    #__slots__ = []
    
    def __init__(self, contents=None):
        if contents is None:
            self.contents = []
        else:
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
    
    
