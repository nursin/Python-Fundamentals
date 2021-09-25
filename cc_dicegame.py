import random

def sum(x, y):
    return x + y


def dice_game():
    high_score = 0
    while(True):
        print("Current High Score: " + str(high_score))
        print("1) Roll Dice")
        print("2) Leave Game")
        print("3) Reset High Score")
        choice = input("Enter your choice: ")
        if choice == "1":
            dice_throw_1 = random.randint(1, 6)
            dice_throw_2 = random.randint(1, 6)
            total = sum(dice_throw_1, dice_throw_2)
            if total > high_score:
                high_score = total
                print("New High Score: " + str(high_score))
            print("Dice thrown are {} & {}".format(dice_throw_1, dice_throw_2) + "\n")
        elif choice == "2":
            print("Goodbye!")
            break
        elif choice == "3":
            high_score = 0
            print("\n")
            continue
        else:
            print("{} is not an option!\n".format(choice))

dice_game()
