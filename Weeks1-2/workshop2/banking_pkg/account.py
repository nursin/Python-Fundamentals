def show_balance(balance):
    print("Your balance is: {}".format(balance))

def deposit(balance):
    amount = int(input("Enter amount to deposit:"))
    return amount + balance

def withdraw(balance):
    amount = int(input("Enter amount to withdraw:"))
    if balance < amount:
        print("Not enough money!")
        return balance
    else:
        return balance - amount

def logout(name):
    print("Goodbye {}!".format(name))