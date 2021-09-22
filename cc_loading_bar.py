quartiles = ['1/4', '1/2', '3/4', 'Loading Complete']

for amount_loaded in range(0, 101, 5):
    print(amount_loaded)
    if amount_loaded == 25:
        print("{} of the way there".format(quartiles[0]))
    elif amount_loaded == 50:
        print("{} of the way there".format(quartiles[1]))
    elif amount_loaded == 75:
        print("{} of the way there".format(quartiles[2]))
    elif amount_loaded == 100:
        print("{}".format(quartiles[3]))
