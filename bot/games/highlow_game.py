#Imports required libraries 
from core.cards import CARD_VALUES

#Makes class for HighLowGame which handles game logic
class HighLowGame:
    def __init__(self, deck):
        #Deck used for drawing cards
        self.deck = deck

        #Pulls starting card
        self.current_card = self.deck.draw()

        #Sets player score
        self.score = 0

        #Game state flag
        self.game_over = False

    #Pulls next card from deck
    def draw_next(self):
        return self.deck.draw()

    #Handles high or low choice
    def guess(self, choice):

        #Prevents playing if game ends
        if self.game_over:
            return "Game over!", None, False

        #Draws next card
        next_card = self.draw_next()

        #If deck fails
        if not next_card:
            self.game_over = True
            return "No cards left!", None, False

        #Get value of cards
        c_val = CARD_VALUES[self.current_card[0]]
        n_val = CARD_VALUES[next_card[0]]

        #If card are equal
        if n_val == c_val:
            return "It's a tie!", next_card, False

        #Checks if the users guess was correct
        correct = (
            (choice == "higher" and n_val > c_val) or
            (choice == "lower" and n_val < c_val)
        )

        #If the guess is correct
        if correct:
            #Increases score
            self.score += 1
            self.current_card = next_card
            return "Correct!", next_card, True

        #If guess is wrong end game
        else:
            self.game_over = True
            return "Wrong!", next_card, False