from GIGO_GAME_pkg import complaint_food_lists, game_objects

def game():
    gigo = game_objects.GIGO(0, 100, 80, 0, 0, 0, 120, complaint_food_lists.complaint_list)
    server = game_objects.Server(complaint_food_lists.food_list)

    while True:
        print(gigo.GIGO_health)
        food_item, food_score = server.serve()
        print("Feed or Pass: {} ".format(food_item.capitalize()))
        print(food_score)
        print(gigo.complain())
        input()