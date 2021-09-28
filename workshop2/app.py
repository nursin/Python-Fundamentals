from banking_pkg import account

while True:
    name = input("Enter name to register: ")
    if len(name) > 10 or len(name) < 1:
        print("Name must be > 1 and < 10 character!")
    else:
        break
while True:
    pin = input("Enter PIN: ")
    if len(pin) != 4 or pin.isnumeric() == False:
        print("Pin must be 4 numbers!")
    else: 
        break

balance = 0
registered = False


def atm_menu(balance, name):
    print("")
    print("          === Automated Teller Machine ===          ")
    if registered == False:
        print("{} has been registered with a starting balance of ${}".format(
            name, balance))
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

while True:
    print("Enter login name and PIN: ")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if (name_to_validate == name and pin_to_validate == pin):
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")

while True:
    atm_menu(balance, name)
    registered = True
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option == "4":
        account.logout(name)
        break
    else:
        print("Choose a valid option")
