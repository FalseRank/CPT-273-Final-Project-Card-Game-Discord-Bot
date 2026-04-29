#Imports required libraries
import random
from core.cards import BLACKJACK_VALUES

#Creates class for "BlackJackGame" which handles game logic
class BlackjackGame:
    def __init__(self, players, deck, economy):
        #Gets users playing
        self.players = players 

        #Uses IDs to store hands
        self.hands = {p.id: [] for p in players}

        #Tracks if player stands
        self.stood = {p.id: False for p in players}
        #Tracks if player busts
        self.busted = {p.id: False for p in players}

        #Gets deck and economy
        self.deck = deck
        self.economy = economy

        #Stores bets per player
        self.bets = {}

        #Sets dealers hand
        self.dealer = []

        #For games state
        self.game_over = False
        #Tracks whose turn it is
        self.turn_index = 0

        #Deals 2 cards to everyone
        for _ in range(2):
            for p in players:
                self.hands[p.id].append(self.draw())
            self.dealer.append(self.draw())



    #Draws a card from deck
    def draw(self):
        return self.deck.draw()



    #Places bet
    def place_bet(self, player, amount):
        pid = player.id
        balance = self.economy.get(player)

        #Validates whether bet is a positive number
        if amount <= 0:
            return "Bet must be greater than 0."

        #Validates whether you have enough in balance for bet
        if amount > balance:
            return "Not enough chips."

        #Removes the chips and stores the bet
        self.economy.remove(player, amount)
        self.bets[pid] = amount

        return f"Bet placed: {amount} chips"



    #Calculates hAND vALUE
    def hand_value(self, hand):
        value = 0
        aces = 0

        for rank, _ in hand:
            value += BLACKJACK_VALUES.get(rank, 0)

            #Tracks if user pulls ace
            if rank == "Ace":
                aces += 1

        #If user has ace determines whether it is 10 or 1
        while value > 21 and aces:
            value -= 10
            aces -= 1

        return value


#----------------------------------------------------------------------------------------
#Turn System

    #Gets current players turn
    def current_player(self):
        return self.players[self.turn_index]



    #Player draw card
    def hit(self, player):
        pid = player.id

        self.hands[pid].append(self.draw())

        #Check if user busts
        if self.hand_value(self.hands[pid]) > 21:
            self.busted[pid] = True
            return "Busted!"

        return "Hit!"



    #Player ends their turn
    def stand(self, player):
        self.stood[player.id] = True
        return "Stood."



    #Moves to next valid player
    def next_turn(self):
        for _ in range(len(self.players)):
            self.turn_index = (self.turn_index + 1) % len(self.players)
            p = self.players[self.turn_index]

            #Skips the users who have stood or busted
            if not self.busted[p.id] and not self.stood[p.id]:
                return True
        #If no players are left
        return False
#--------------------------------------------------------------------------------------------------


    #Checks if all players are done
    def all_done(self):
        return all(
            self.stood[p.id] or self.busted[p.id]
            for p in self.players
        )



    #Dealer logic
    def dealer_play(self):
        #If hand is less than 17 hit
        while self.hand_value(self.dealer) < 17:
            self.dealer.append(self.draw())



#----------------------------------------------------------------------------------------------------
#Results

    def results(self):
        dealer_val = self.hand_value(self.dealer)
        results = []

        for p in self.players:
            pid = p.id
            player_val = self.hand_value(self.hands[pid])

            #Get players bet
            bet = self.bets.get(pid, 0)

            #Requires bets to recieve payout
            if bet == 0:
                results.append(
                    f"{p.display_name}: No bet placed (no payout)"
                )
                continue
            payout = 0

            #Checks if user busted
            if self.busted[pid]:
                outcome = "Bust"

            #Checks if user got blackjack
            elif player_val == 21 and len(self.hands[pid]) == 2:
                outcome = "Blackjack"
                payout = int(bet * 2.5)

            #Cheks if user won
            elif dealer_val > 21 or player_val > dealer_val:
                outcome = "Win"
                payout = bet * 2

            #Checks if user and dealer got the same value
            elif player_val == dealer_val:
                outcome = "Push"
                payout = bet

            #Checks if user lost
            else:
                outcome = "Lose"

            #Pays winnings
            if payout > 0:
                self.economy.add(p, payout)

            #Stores result text
            results.append(
                f"{p.display_name}: {outcome} ({player_val}) | Bet: {bet}"
            )

        return dealer_val, results