import random

pips = random.randint(1, 6)
print("You roll the die.. it lands with", pips, "showing.")

prizes = ["a car", "$10000", "a pony", "$500000"]
prizes_won = random.choice(prizes)
print("You turn the wheel of fortune... It lands on a prize of", prizes_won + "!!")

cards = list(range(1, 12, 1))
random.shuffle(cards)
print("The cards are now in this order:")
print(cards)