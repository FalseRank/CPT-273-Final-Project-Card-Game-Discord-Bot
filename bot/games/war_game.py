#Required imports
from core.cards import CARD_VALUES

#Creates class "WarGame" for the game logic
class WarGame:
    def __init__(self, deck, p1_user, p2_user):
        #Gets deck 
        self.deck = deck
        #Sets variable for a deck for 1st user
        self.p1_user = p1_user
        #Sets variable for a deck for 2nd user
        self.p2_user = p2_user

        #Converts deck into list
        cards = list(self.deck.cards)
        #Splits deck in 2 and splits them to both users
        self.p1 = cards[:26]
        self.p2 = cards[26:]

        #Game state
        self.game_over = False
        self.winner = None

    #Removes the top card from both users hand and shows them
    def draw(self, player):
        return player.pop(0) if player else None

    #Gets the value of the card showed
    def value(self, card):
        return CARD_VALUES[card[0]]

    #Plays a round
    def play_round(self):
        #Stops if game is ended
        if self.game_over:
            return None

        #Checks if player ran out of cards
        if not self.p1:
            self.end(self.p2_user)
            return None
        #Checks if other player ran out of cards
        if not self.p2:
            self.end(self.p1_user)
            return None

        #Each player draws cards
        c1 = self.draw(self.p1)
        c2 = self.draw(self.p2)

        #Get card values
        v1 = self.value(c1)
        v2 = self.value(c2)

        result = ""

        #----------------------------------------------------------------------------
        #Determines the round winner

        #If player 1 values are greaterthan player 2 values
        if v1 > v2:
            #PLayer 1 wins both cards
            self.p1.extend([c1, c2])
            #Prints result
            result = f"{self.p1_user.mention} wins the round!"

        #If player 2 values are greater than player 1 values
        elif v2 > v1:
            #Player 2 wins both cards
            self.p2.extend([c1, c2])
            #Prints results
            result = f"{self.p2_user.mention} wins the round!"

        #If both card value equals
        else:
            result = "WAR!" 

        return c1, c2, result

    #Sets the winner and end games
    def end(self, winner):
        self.game_over = True
        self.winner = winner