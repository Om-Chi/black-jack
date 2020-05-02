import random

cards = {"Queen": 10, "Jack": 10, "King": 10, "Ace": 11} 

DECK = [random.randint(1, 10) for i in range(2)] + [random.choice(list(cards.keys())) for i in range(4)]
players_hand = random.choices(DECK, weights = [36, 35, 4, 4, 4, 4], k = 2)
dealer_hand = random.choices(DECK, weights = [36, 35, 4, 4, 4, 4], k = 2)
print(players_hand)

user = input("Type 'H' to hit or 'S' to stay: ")
print(user)

chance = 0
while user == 'H' and chance < 3:
  hit_me = random.choice(DECK)
  print(hit_me)
  user = input("Type 'H' to hit or 'S' to stay: ")
  print(user)
  chance += 1

if user == 'S':
  print(dealer_hand)
  if sum(dealer_hand) <= 10:   #Find a way to add the value of cards; convert the strings into int
    print(random.choice(DECK))
