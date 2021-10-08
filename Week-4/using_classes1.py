# class Player:
#     max_hp = 4000

# player1 = Player()
# player2 = Player()

# print(player1.max_hp)
# print(player2.max_hp)

# Player.max_hp = 5000

# print(player1.max_hp)
# print(player2.max_hp)


class Player:
    # constructor
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.score = 0

player1 = Player("Aaron", 1200)
player2 = Player("Irene", 1300)

print("P1: {} -- HP: {} -- SCORE: {}".format(player1.name, player1.hp, player1.score))
print("P2: {} -- HP: {} -- SCORE: {}".format(player2.name, player2.hp, player2.score))

player1.hp += 500
player1.score =+ 10

print("P1: {} -- HP: {} -- SCORE: {}".format(player1.name, player1.hp, player1.score))
print("P2: {} -- HP: {} -- SCORE: {}".format(player2.name, player2.hp, player2.score))