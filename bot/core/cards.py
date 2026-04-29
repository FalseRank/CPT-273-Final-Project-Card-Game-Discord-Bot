#Standard card values used in higher and lower and war
CARD_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10,
    "Jack": 11, "Queen": 12, "King": 13, "Ace": 14
}

#Blackjack card values
BLACKJACK_VALUES = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11
}

#Adds suits with emojis
SUIT_EMOJIS = {
    "Hearts": "♥️",
    "Diamonds": "♦️",
    "Clubs": "♣️",
    "Spades": "♠️"
}

#Format card function
def format_card(card):
    rank, suit = card
    emoji = SUIT_EMOJIS.get(suit, "")
    #Returns as string
    return f"{rank} {emoji}"