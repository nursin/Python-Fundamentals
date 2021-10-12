from GIGO_GAME_pkg import complaint_food_lists, game_objects

def game():
    gigo = game_objects.GIGO(0, 100, 80, 0, 0, 0, 120, complaint_food_lists.complaint_list)
    server = game_objects.Server(complaint_food_lists.food_list)

    while True:
        print("Health: {}".format(gigo.GIGO_health))
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
                gigo.GIGO_health += food_score
            print("")
        else:
            print("Invalid response\n")
