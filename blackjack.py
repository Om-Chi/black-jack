import random

spades = {"Queen": 10, "Jack": 10, "King": 10, "Ace": 11}
hearts = {"Queen": 10, "Jack": 10, "King": 10, "Ace": 11}
clubs = {"Queen": 10, "Jack": 10, "King": 10, "Ace": 11}
diamonds = {"Queen": 10, "Jack": 10, "King": 10, "Ace": 11}
DECK = [random.randint(1, 10), random.choice(list(spades.keys())), random.choice(list(hearts.keys())), random.choice(list(clubs.keys())), random.choice(list(diamonds.keys()))]
players_hand = random.choices(DECK, weights = [36, 4, 4, 4, 4], k = 2)
dealer_hand = random.choices(DECK, weights = [36, 4, 4, 4, 4], k = 2)
print(players_hand)
hit_me = random.choices(DECK, weights = [36, 4, 4, 4, 4], k = 1)
hit_dealer = random.choices(DECK, weights = [36, 4, 4, 4, 4], k = 1)

user = input("Type 'H' to hit or 'S' to stay: ")
print(user)

chance = 0
while user != "H" and chance == False:
    print(dealer_hand)
    chance += 1
    for card in dealer_hand:
        if card in ("Ace", 2):
            print(hit_dealer)
        else: None
    next = input(f"Type 'H' to hit again ")
    print(next)
    if next == "H":
        hit_dealer2 = random.choices(DECK, weights=[36, 4, 4, 4, 4], k=1)
        print(hit_dealer2)
    else:
        None

if user == "H":
    print(hit_me)
    print(dealer_hand)
