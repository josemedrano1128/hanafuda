# hanafuda
Playable Hanafuda Koi Koi created in Pygame

Using this to develop a bunch of skills at once. Gonna start off as a 2 player game, hopefully I can incorporate basic AI in later. 

Recent Edits:
cards.py:
Added functionality that will be useful for sorting a deck/hand later to the Card class, as well as a few other changes to make it a more proper class (lack of dynamic attributes, better str representation vs repr). Made the cards themselves private objects and instead the module will have a "cardlist" dict containing the list of cards, indexed by "jan001" etc.

koikoi.py:
The basic skeleton for a few other game-necessary objects. Still needs a Manager object that will contain the bulk of the game's code.
