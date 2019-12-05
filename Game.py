import random

Deck = {
    '1': 4,
    '2': 4,
    '3': 4,
    '4': 4,
    '5': 4,
    '6': 4,
    '7': 4,
    '8': 4,
    '9': 4,
    '10': 4,
    '11': 4,
    '12': 4,
    '13': 4
}

currentDeck = []
playerCards = []
botCards = []

for i in range(1, 14):
    for j in range(Deck.get(str(i))):
        currentDeck.append(str(i))
#Copies availbable cards from the dictionary to a list

for i in range(5):
    r = random.randint(0, len(currentDeck) - 1)
    playerCards.append(currentDeck[r])
    currentDeck.remove(str(currentDeck[r]))
#Appends selected cards from the currentDeck list to the player's and bot's hands, then removes them from currentDeck

for i in playerCards:
    Deck[str(i)] = Deck[str(i)] - 1
#Updates the dictionary to reflect the taken/removed cards
#TODO move this into the above for loop