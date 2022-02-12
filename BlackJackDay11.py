import random

from art import logo
print(logo)

# Added some personal challenges not requested. 
# Made the deck of cards reduce so you can practice counting cards :)
# Added a stronger function to check hand value for the edge cases of multiple aces

deck = {
  "hearts":[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
  "diamonds":[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
  "spades":[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10],
  "clubs":[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
}
suits = ['hearts','diamonds','spades','clubs']

def drawAcard(deck):
  card_value = 0
  while card_value == 0:
    suit = random.choice(suits)
    card = random.randint(0,12)
    card_value = deck[suit][card]
  deck[suit][card] = 0
  return card_value

def CalculateWinner(GameData):
  ph = GameData['PlayerHand'] 
  ch = GameData['compHand']
  if getMinValue(ph) > 21:
    print('You Lose: Busted')
  elif getMinValue(ch) >21:
    print('You WIN: comp Busted')
  elif getMaxValue(ch) == getMaxValue(ph):
    print("Draw")
  elif getMaxValue(ch) > getMaxValue(ph):
    print(f"You loose: Computer {getMaxValue(ch)} vs Your {getMaxValue(ph)}")
  else:
    print(f"You Win: Your {getMaxValue(ph)} vs Computer {getMaxValue(ch)}")

def deal():
  computerCardValues = []
  playerCardValues = []
  for _ in range(2):
    computerCardValues.append(drawAcard(deck))
    playerCardValues.append(drawAcard(deck))
  print(f'Your cards: {playerCardValues}')
  print(f'Computer\'s cards [{computerCardValues[0]}, *]')
  return {
    'compHand' : computerCardValues,
    'PlayerHand' : playerCardValues
  }

def getMinValue(hand):
  total_value = 0
  for val in hand:
    if val != 11:
      total_value += val
    else:
      total_value += 1
  return total_value

def getMaxValue(hand):
  total_value = 0
  Ace_count = 0
  for val in hand:
    if val != 11:
      total_value += val
    else:
      Ace_count += 1
      total_value += 11
    while total_value > 21 and Ace_count> 0:
      total_value -= 10
  return total_value

game = 'on'
while game == 'on':

  start = input("Would you like to play some BlackJack? ")
  if start != 'y' and start != 'yes':
    print('see ya')
    game = 'off'
    break
  GameData = deal()
  HorS = ''
  while HorS != 's':
    HorS = input('would you like to (h)it or (s)tand: ')
    if HorS == 'h':
      GameData['PlayerHand'].append(drawAcard(deck))
      print(f"Your cards: {GameData['PlayerHand']}")
      if  getMinValue(GameData['PlayerHand']) > 21:
        print('Busted')
        HorS = 's'
  
  #computer Turn
  while getMinValue(GameData['compHand']) < 17 and getMaxValue(GameData['compHand']) < 17:
    GameData['compHand'].append(drawAcard(deck))
  
  CalculateWinner(GameData)
  print(GameData)
  print(deck)

