import random
from os import system, name 
from time import sleep 
 
def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

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

funds = int(input("""              __                                               
        _..-''--'----_.                                        
      ,''.-''| .---/ _`-._                                     
    ,' \ \  ;| | ,/ / `-._`-.                                  
  ,' ,',\ \( | |// /,-._  / /                                  
  ;.`. `,\ \`| |/ / |   )/ /                                   
 / /`_`.\_\ \| /_.-.'-''/ /                                    
/ /_|_:.`. \ |;'`..')  / /                                     
`-._`-._`.`.;`.\  ,'  / /                                      
    `-._`.`/    ,'-._/ /                                       
      : `-/     \`-.._/                                        
      |  :      ;._ (                                          
      :  |      \  ` \                                         
       \         \   |                                         
        :        :   ;                                         
        |           /                                          
        ;         ,'                                           
       /         /                                             
      /         /                                              
               / ~ SSt                                         
    
    How many chips would you like? """))

for i in range(1, len(Deck) + 1):
    for j in range(Deck.get(str(i))):
        currentDeck.append(str(i))
#Copies availbable cards from the dictionary to a list

for i in range(5):
    r = random.randint(0, len(currentDeck) - 1)
    playerCards.append(currentDeck[r])
    currentDeck.remove(str(currentDeck[r]))
    Deck[str(playerCards[-1])] = Deck[str(playerCards[-1])] - 1

    r = random.randint(0, len(currentDeck) - 1)
    botCards.append(currentDeck[r])
    currentDeck.remove(str(currentDeck[r]))
    Deck[str(botCards[-1])] = Deck[str(botCards[-1])] - 1
#Appends selected cards from the currentDeck list to the player's and bot's hands, then removes them from currentDeck and the dictionary

# prompt(print())
# print(playerCards)

clear()
input('    Press Enter to exit...')