from GIGO_GAME_pkg import complaint_food_lists, game_objects
import random

def game():
    gigo = game_objects.GIGO(0, 100, 80, 0, 0, 0, 120, complaint_food_lists.complaint_list)
    server = game_objects.Server(complaint_food_lists.food_list)
    revive = game_objects.CPR()
    while True:
        print("Health: {}".format(gigo.GIGO_health))
        print("Score: {}".format(gigo.score))
        food_item, food_score = server.serve()
        print("Food item: {}".format(food_item.capitalize()))
        feed = input("Feed or Pass: ")

        if feed == "pass":
            gigo.complain()
            print("")
            continue
        elif feed == "feed":
            gigo.score += food_score
            if food_score == -1:
                gigo.GIGO_health += -5
            elif food_score == 1:
                gigo.score += random.randint(1, 10)
            print("")
        else:
            print("Invalid response\n")

        if gigo.GIGO_health <= 75 and gigo.GIGO_health > 50:
            print("GIGO overweight")
        elif gigo.GIGO_health <= 50 and gigo.GIGO_health > 25:
            print("GIGO obese")
        elif gigo.GIGO_health <= 25 and gigo.GIGO_health > 0:
            print("GIGO morbid obesity")
        elif gigo.GIGO_health <= 0:
            gigo.die()
            revived = revive.revive()
            if revived == True:
                print("CPR success!")
                gigo.GIGO_health += 25
                gigo.score -= 25
            else:
                print("CPR failed!")
                print("Your score: {}".format(gigo.score))
                input("Press enter to continue")
                break
        else:
            continue