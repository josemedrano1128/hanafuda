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
        print("Now playing {}".format(self.contents[cardIndex].name))
        print("\n")
        sleep(2)
        cardToPlay = self.contents.pop(cardIndex)
        return cardToPlay

    def clear(self):
        self.contents = []
    
    def __str__(self):
        return ", ".join([card.name for card in self.contents])
    
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
        if len(matchList) < 3:
            choice = int(input("{} and {} both match: which do you want? 0 or 1: ".format(matchList[0],matchList[1])))
            self.contents.remove(matchList[choice])
            self.awaitingRelease = [matchList[choice],cardPlayed]
            return 1
        if len(matchList) == 3:
            #print("Hiki!!")
            for match in matchList:
                self.contents.remove(match)
            self.awaitingRelease = matchList + [cardPlayed]

    def release(self):
        #release to scoring area
        awaitingRelease,self.awaitingRelease = self.awaitingRelease, []
        return awaitingRelease
    
    def __str__(self):
        nameList = [card.name for card in self.contents]
        return ", ".join(nameList[:4]) + "\n" + ", ".join(nameList[4:])
    
    #def __repr__(self):
     #   return str(self.contents)
    
    

class ScoringArea:
    
    #__slots__ = ["contents"]
    
    def __init__(self):
        self.contents = {"20" : [], "10" : [], "5": [], "1": []}
        self.yakuList = ["goko", "shiko", "ame-shiko", "sanko", "hanami", "tsukimi", "inoshikacho", "tane", "akatan", "aotan", "akaaotan", "tan", "kasu"]
        
        _falseList = [False for i in range(len(self.yakuList))]
        self.yakuDict = dict(zip(self.yakuList, _falseList))
        
        _scoreList = [10, 8, 7, 5, 5, 5, 5, 1, 5, 5, 10, 1, 1]
        self.scoreDict = dict(zip(self.yakuList,_scoreList))
        
        self.sake = 0
    
    def accept(self, cards):
        """Accepts any number of cards given at a time and puts them in the appropriate score areas"""
        #Uses the values as the dictionary key, as that is how cards are stored in physical score areas
        #scoring work itself should be done by the Manager
        for card in cards:
            self.contents[str(card.value)].append(card)
            print("{} added to your scoring area".format(card.name))
            if card.nameId == "sep001":
                self.sake = 1
        print("\n")
        sleep(2)
    
    def checkYaku(self):
        
        #lists of names, for convenience. Sake cup count is used later for dregs purposes
        brightList = [card.nameId for card in self.contents["20"]]
        animalList = [card.nameId for card in self.contents["10"]]
        ribbonList = [card.nameId for card in self.contents["5"]]
        dregsList = [card.nameId for card in self.contents["1"]]
        #sake = 0
        
        brightCount = len(brightList)
        #check for Bright-5 (goko)
        if brightCount == 5:
            self.yakuDict["goko"] = True
        #Bright-4s
        elif brightCount == 4:
            if "nov001" in brightList:
                self.yakuDict["ame-shiko"] = True
            else:
                #otherwise, (full) 4-bright must be the case
                self.yakuDict["shiko"] = True
        elif brightCount == 3 and "nov001" not in brightList:
            self.yakuDict["sanko"] = True
        #check both Sake Cups...
        if "sep001" in animalList:
            self.sake = 1
            self.yakuDict["hanami"] = "mar001" in brightList
            self.yakuDict["tsukimi"] = "aug001" in brightList
        
        #check InoShikaCho...
        self.yakuDict["inoshikacho"] = ("jul001" in animalList and "oct001" in animalList and "jun001" in animalList)
        
        #check 5 animals...
        self.yakuDict["tane"] = (len(animalList) >= 5)
        
        #check akatan and aotan, remembering together they are one yaku
        akatan = "jan002" in ribbonList and "feb002" in ribbonList and "mar002" in ribbonList
        aotan = "jun002" in ribbonList and "sep002" in ribbonList and "oct002" in ribbonList
        self.yakuDict["akatan"] = akatan
        self.yakuDict["aotan"] = aotan
        if akatan and aotan:
            self.yakuDict["akatan"] = False
            self.yakuDict["aotan"] = False
            self.yakuDict["akaaotan"] = True
        
        #ribbon 5
        self.yakuDict["tan"] = (len(ribbonList) >= 5)
        
        #10 dregs/plains
        if len(dregsList) + self.sake >= 10:
            self.yakuDict["kasu"] = True
            
        return self.yakuDict
    
    def rawRoundScore(self):
        #yakuList = ["goko", "shiko", "ame-shiko", "sanko", "hanami", "tsukimi", "inoshikacho", "tane", "akatan", "aotan", "akaaotan", "tan", "kasu"]
        roundScore = 0
        achievedYaku = list(filter(lambda key: self.yakuDict[key], self.yakuDict.keys()))
        for yaku in achievedYaku:
            roundScore += self.scoreDict[yaku]
            if yaku == "inoshikacho":
                roundScore += (len(self.contents["10"]) - 3)
            if yaku == "tane":
                roundScore += (len(self.contents["10"]) - 5)
            if yaku == "akatan":
                roundScore += (len(self.contents["5"]) - 3)
            if yaku == "aotan":
                roundScore += (len(self.contents["5"]) - 3)
            if yaku == "akaaotan":
                roundScore += (len(self.contents["5"]) - 6)
            if yaku == "tan":
                roundScore += (len(self.contents["5"]) - 5)
            if yaku == "kasu":
                roundScore += (len(self.contents["1"]) + self.sake - 10)
        
        return roundScore
            
                
        

class Player:
    
    def __init__(self, playerNumber):
        self.score = 0
        self.playerNumber = playerNumber
        self.hand = Hand()
        self.scoringArea = ScoringArea()
    
    def addToHand(self, cards):
        self.hand.contents += (cards)
        return self.hand.contents
    
    def sortHand(self):
        self.hand.sort()
    
    def clearHand(self):
        self.hand.clear()
        
    def __getattr__(self, attr):
        return getattr(self.hand, attr)
    


class Manager:
    
    def __init__(self):
        self.players = [Player(1),Player(2)]
        self.state = "DEAL" 
        self.currentplayer = 0
        #self.fmap = {"AUTOWIN?": checkAutowin, "ROUNDWIN": roundWin}
        
    def checkAutowin(self):
        """Searches for 4 cards of any month in either hand"""
        #TODO: add in functionality for double 4-victory. 
        for player in self.players:
            monthVals = {}
            for card in player.hand.contents:
                month = card.monthId
                if month in monthVals:
                    monthVals[month] += 1
                    #breaks the moment it finds 4 of a month
                    if monthVals[month] == 4:
                        break
                else:
                    monthVals[month] = 1
            #iteration finished without finding 4
            else:
                return (False, player, None)
        
        return (True, player, month)
    
    #def roundWin(self, player, score):
     #   player.score += score
        #more?
                
        
    def roundSetup(self):
        self.koikoiBonus = 1
        self.gameDeck = Deck(cards.getDeck())
        print("Deck Initialized, shuffling...\n")
        self.gameDeck.shuffle()
        sleep(2)
        print("Dealing...\n")
        self.players[0].clearHand()
        self.players[1].clearHand()
        self.players[0].addToHand(self.gameDeck.pop(8))
        self.players[0].hand.sort()
        self.players[1].addToHand(self.gameDeck.pop(8))
        self.players[1].hand.sort()
        sleep(2)
        print("Hands have been dealt.\n")
        sleep(1)
        print("Dealing to Center Board...\n")
        self.center = CenterBoard(self.gameDeck.pop(8))
        sleep(2)
        #print("Center Board:")
        #print(self.center)
        print("\nGame is ready to begin. Proceed.")
        sleep(2)
        
    def playerPlay(self):
        print("Player {}'s Turn".format(self.players[self.currentplayer].playerNumber))
        sleep(1)
        print("\n")
        print("Center Board is: ")
        sleep(2)
        print(self.center)
        print("\n"*3)
        print("Cards in Hand are: ")
        sleep(1)
        print(self.players[self.currentplayer].hand)
        #TODO: add error handling here...
        #TODO: split the next compound line into separate lines for readability
        #TODO: give option to see scoring areas
        needRelease = self.center.accept(self.players[self.currentplayer].hand.play(int(input("0-based Card Index to Play? "))))
        if needRelease:
            if needRelease == 3:
                print("Hiki!")
            self.players[self.currentplayer].scoringArea.accept(self.center.release())
        
    def deckPlay(self):
        print("Now playing from Deck for Player {}".format(self.players[self.currentplayer].playerNumber))
        sleep(2)
        #note: Deck.pop() returns a list, index there to give the card itself
        #TODO: add error handling here...
        #TODO: split the next compound line into separate lines for readability
        #TODO: give option to see scoring areas
        cardToPlay = self.gameDeck.pop(1)[0]
        print("Now playing {}...".format(cardToPlay.name))
        print("\n")
        needRelease = self.center.accept(cardToPlay)
        if needRelease:
            if needRelease == 3:
                print("Hiki!")
            self.players[self.currentplayer].scoringArea.accept(self.center.release())


    def gameLoop(self):
        while True:
            #TODO: add more prints to actually make it player-friendly
            if self.state == "DEAL":
                self.roundSetup()
                self.state = "AUTOWIN?"
                continue
            
            elif self.state == "AUTOWIN?":
                win, wonplayer, wonmonth = self.checkAutowin()
                if win == True:
                    self.state = "WONROUND"
                    continue
                self.state = "PLAYERPLAY"
                continue
            
            elif self.state == "PLAYERPLAY":
                if len(self.players[self.currentplayer].hand) == 0:
                    print("Player {}'s Hand is Empty. Proceeding with next round...".format(self.players[self.currentplayer].playerNumber))
                    sleep(2)
                    self.state = "DEAL"
                    continue
                self.playerPlay()
                self.state = "DECKPLAY"
                continue
    
            elif self.state == "DECKPLAY":
                self.deckPlay()
                self.state = "YAKU?"
                continue
            
            elif self.state == "YAKU?":
                yaku = self.players[self.currentplayer].scoringArea.checkYaku()
                #achievedYaku = list(filter(lambda key: self.yakuDict[key], self.yakuDict.keys()))
                if True in yaku.values():
                    #print("You got a yaku! koikoi coming soon")
                    invalidInput = True
                    while invalidInput == True:
                        try:
                            options = input("You got a yaku! koikoi or stop? ")
                            if options.lower() != "koikoi" and options.lower() != "stop":
                                raise IOError
                        except IOError:
                            print("INVALID INPUT. ENTER ONLY EITHER koikoi OR stop.")
                        else:
                            invalidInput = False
                    if options == "koikoi":
                        self.state = "PLAYERPLAY"
                        self.currentplayer = not self.currentplayer
                        self.koikoiBonus += 1
                        continue
                    else:
                        self.state = "ROUNDWIN"
                        continue
                else:
                    self.currentplayer = not self.currentplayer
                    self.state = "PLAYERPLAY"
                    continue
                
            elif self.state == "ROUNDWIN":
                self.players[self.currentplayer].score += self.players[self.currentplayer].scoringArea.rawRoundScore()*self.koikoiBonus
                self.state = "DEAL" 
                
                
                


                    
        

if __name__ == "__main__":
    game = Manager()
    game.gameLoop()
    pass