#Import Required Library
import random
from collections import deque

#Creates class "Deck" which handles creating, shuffling, and drawing cards
class Deck:
    def __init__(self):
        #Immediately builds and shuffles deck
        self.reset()

    #Resets the deck
    def reset(self):
        #The suits in a deck
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        #All cards
        ranks = [
            "2","3","4","5","6","7","8","9","10",
            "Jack","Queen","King","Ace"
        ]

        #Creates all combinations of cards and suits
        self.cards = [(rank, suit) for suit in suits for rank in ranks]

        #Shuffles the deck randomly
        random.shuffle(self.cards)

        #Converts list into a deque for fast removal of cards
        self.cards = deque(self.cards)

    #Removes and returns the top card from the deck
    def draw(self):
        #If deck is empty refills the deck
        if not self.cards:
            self.reset()

        #Removes and returns the top card
        return self.cards.popleft()