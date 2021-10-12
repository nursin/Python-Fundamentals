import random

from GIGO_GAME_pkg import complaint_food_lists

class GIGO:
    def __init__(self, score, GIGO_health, blood_sugar, sob, chf, swelling, weight, complaint_list):
        self.score = score
        self.GIGO_health = GIGO_health
        self.blood_sugar = blood_sugar
        self.sob = sob
        self.chf = chf
        self.swelling = swelling
        self.weight = weight
        # vitals = {bp: "120/80", hr: "80", oxygen: "100%"}
        self.complaint_list = complaint_list

    def complain(self):
        print(random.choice(self.complaint_list))

    def die(self):
        print("GIGO has died!")

class Server:
    def __init__(self, food_list):
        self.food_list = food_list

    def serve(self):
        food_item = random.choice(list(self.food_list))
        food_score = self.food_list[food_item]
        return [food_item, food_score]

class CPR:
    def __init__(self):
        pass

    def revive(self):
        count = 0
        num = random.randint(1, 100)
        while count < 6:
            guess = int(input("Enter a number between 1 - 100: "))

            if guess == num:
                return True
            elif count == 5:
                return False
            elif guess > num:
                print("Too high")
            elif guess < num:
                print("Too low")
            else:
                print("Guess again")
            count += 1
        
        
