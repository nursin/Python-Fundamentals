from GIGO_GAME_pkg import homepage, single_player, game_objects
import random

settings = []
high_score = 0

while True:
    homepage.show_homepage()
    print("High score: {}".format(high_score))
    option = input("Select an option: ")
    if option == "1":
        print("Single player")
        score = single_player.game(settings)
        if score > high_score:
            high_score = score
    elif option == "2":
        print("Mulitple player")
    elif option == "3":
        homepage.show_settings()
        health = input("Enter beginning health: ")
        weight = input("Enter beginning weight: ")
        settings = [int(health), int(weight)]
        print(settings)
    elif option == "4":
        print("High score")
    elif option == "5":
        print("Exiting")
        break
    else:
        print("Invalid option")
