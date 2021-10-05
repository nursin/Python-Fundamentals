from donations_pkg import homepage, user
database = {"admin": "password123"}
donations = []
authorized_user = ""

while True:
    homepage.show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as: {}".format(authorized_user))
    selected_option = input("Choose an option: ")

    if selected_option == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = user.login(username, password, database)
        continue
    elif selected_option == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = user.register(username, database)
        if authorized_user == "":
            continue
        else:
            database[username] = password
            print(database)
            continue
    elif selected_option == "3":
        if authorized_user == "":
            print("You are not logged in!")
            continue
        else:
            donate = homepage.donate(authorized_user)
            donations.append(donate)
            continue
    elif selected_option == "4":
        homepage.show_donations(donations)
        continue
    elif selected_option == "5":
        print("Goodbye!!")
        break
