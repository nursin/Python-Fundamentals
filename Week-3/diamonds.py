import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    user_selection = input("Pick a card or Q + enter to quit")
    if user_selection == "Q":
        break
    random_card = diamonds.pop(random.randint(0, len(diamonds) - 1))
    hand.append(random_card)
    print(random_card)
    print("Your hand:", hand)
    print("Remaining cards:", diamonds)

if not diamonds:
    print("There are no more cards to pick.")