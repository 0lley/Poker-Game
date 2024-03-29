import random
from Ascii import dealerImg, cardFaces
from os import system, name 
from time import sleep 
 
def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

def messageDisplay(times, speed, msg):
    for i in range(times):
        clear()
        print('    ' + msg + '.')
        sleep(speed)
        clear()
        print('    ' + msg + '..')
        sleep(speed)
        clear()
        print('    ' + msg + '...')
        sleep(speed)
    clear()

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
    # '14': 2
}

currentDeck = []
playerCards = []
botCards = []

def handCheck():
    playerCards.sort()
    a = 1
    for i in playerCards:
        a = a*i
    print(a)
    if math.factorial(playerCards[4])/math.factorial((playerCards[0]-1)) == a:
        print("You have a flush!")

funds = 0

while funds < 100:
    funds = int(input(dealerImg))
    clear()

for i in range(1, len(Deck) + 1):
    for j in range(Deck.get(str(i))):
        currentDeck.append(str(i))
#Copies availbable cards from the dictionary to a list

for i in range(5):
    r = random.randint(0, len(currentDeck) - 1)
    playerCards.append(int(currentDeck[r]))
    currentDeck.remove(str(currentDeck[r]))
    Deck[str(playerCards[-1])] = Deck[str(playerCards[-1])] - 1

    r = random.randint(0, len(currentDeck) - 1)
    botCards.append(int(currentDeck[r]))
    currentDeck.remove(str(currentDeck[r]))
    Deck[str(botCards[-1])] = Deck[str(botCards[-1])] - 1
#Appends selected cards from the currentDeck list to the player's and bot's hands, then removes them from currentDeck and the dictionary

#TODO: Put ascii art of the opponent

messageDisplay(2, 0.25, 'Drawing cards')

print("Your hand is: ")
for i in range(5):
    print(cardFaces.get(str(playerCards[i])))

for i in range(4):
    if (input("    Would you like to replace any cards? (yes/no) ")) == 'yes':
        r = random.randint(0, len(currentDeck) - 1)
        playerCards[int(input("    Which card slot would you like to replace? (1 - 5) ")) - 1] = (currentDeck[r])
        currentDeck.remove(str(currentDeck[r]))
        Deck[str(playerCards[-1])] = Deck[str(playerCards[-1])] - 1

        messageDisplay(2, 0.25, 'Drawing a new card')
        print("Your new hand is: ")
        for i in range(5):
            print(cardFaces.get(str(playerCards[i])))

    else:
        print("Your final hand is: ")
        for i in range(5):
            print(cardFaces.get(str(playerCards[i])))
        sleep(2.5)
        messageDisplay(2, 0.25, "Revealing opponent's hand")
        break

playerCards.sort()
botCards.sort()
#TODO: Add cardchecking here

# clear()
input('    Press Enter to exit... ')