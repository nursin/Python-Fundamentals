from GIGO_GAME_pkg import homepage, single_player
import random

homepage.show_homepage()

while True:
    option = input("Select an option: ")
    print(option)
    if option == "1":
        print("Single player")
        single_player.game()
    elif option == "2":
        print("Mulitple player")
    elif option == "3":
        print("Settings")
    elif option == "4":
        print("High score")
    elif option == "5":
        print("Exiting")
        break
    else:
        print("Invalid option")
