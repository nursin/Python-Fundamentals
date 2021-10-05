def login(username, password, database):
    for username_db, password_db in database.items():
        if username == username_db and password == password_db:
            print("Successful login")
            return username
        elif username == username_db:
            print("Invalid password")
            return ""
        else:
            print("Username not found")
            return ""


def register(username, database):
    for username_db, password_db in database.items():
        if username == username_db:
            print("Already registered")
            return ""
        else:
            print("Registered succefully")
            return username
