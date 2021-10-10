class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        self.name = new_name

    def change_pin(self, new_pin):
        self.pin = new_pin

    def change_password(self, new_password):
        self.password = new_password

class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0.0
    
    def show_balance(self):
        print("{} has an account balance of: {}".format(self.name, self.balance))
    
    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            print("Not enough money!")
            print("     Attempted to withdraw: {}".format(withdraw_amount))
            print("     Balance: {}".format(self.balance))
            return False
        else:
            self.balance -= withdraw_amount
            return True

    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    def transfer_money(self, receiving_user, transfer_amount):
        print("Authentication required")
        pin = input("Enter your PIN: ")
        if pin == receiving_user.pin:
            print("Transfer authorized")
            print("Transferring ${} to {}".format(transfer_amount, receiving_user.name))
            self.balance -= transfer_amount
            receiving_user.deposit(transfer_amount)
        else:
            print("Invalid PIN. Transaction canceled")

    def request_money(self, user_requested, user_requesting, transfer_amount):
        print("Authentication required")
        pin = input("Enter your PIN: ")
        if pin == user_requested.pin:
            print("Transfer authorized")
            print("Transferring ${} to {}".format(transfer_amount, user_requested.name))
        else:
            print("Invalid PIN. Transaction canceled")

        password = input("Enter your password: ")
        if password == user_requesting.password:
            funds_available = user_requested.withdraw(transfer_amount)
            if funds_available:
                self.balance += transfer_amount
            else:
                print("{} does not have enough money! Transaction canceled". format(user_requested.name))
        else:
            print("Invalid password. Transaction canceled")
        

""" Driver Code for Task 1 """
# test_user = User("Bob", 1234, "password")
# print(test_user.name, test_user.pin, test_user.password)

""" Driver Code for Task 2 """
# test_user = User("Bob", 1234, "password")
# print(test_user.name, test_user.pin, test_user.password)
# test_user.change_name("Bobby")
# test_user.change_pin("4321")
# test_user.change_password("newpassword")
# print(test_user.name, test_user.pin, test_user.password)

""" Driver Code for Task 3"""
# test_bankUser = BankUser("Bob", 1234, "password")
# print(test_bankUser.name, test_bankUser.pin, test_bankUser.password, test_bankUser.balance)
# test_bankUser.show_balance()
# test_bankUser.deposit(100)
# test_bankUser.show_balance()
# test_bankUser.withdraw(150)
# test_bankUser.show_balance()
# test_bankUser.withdraw(50)
# test_bankUser.show_balance()

""" Driver Code for Task 5"""
test_bankUser1 = BankUser("Bob", "1234", "password")
test_bankUser2 = BankUser("Alice", "1234", "password")
print(test_bankUser1.name, test_bankUser1.pin, test_bankUser1.password, test_bankUser1.balance)
print(test_bankUser2.name, test_bankUser2.pin, test_bankUser2.password, test_bankUser2.balance)
test_bankUser2.deposit(5000)
print(test_bankUser1.name, test_bankUser1.pin, test_bankUser1.password, test_bankUser1.balance)
print(test_bankUser2.name, test_bankUser2.pin, test_bankUser2.password, test_bankUser2.balance)
test_bankUser2.transfer_money(test_bankUser1, 500)
print(test_bankUser1.name, test_bankUser1.pin, test_bankUser1.password, test_bankUser1.balance)
print(test_bankUser2.name, test_bankUser2.pin, test_bankUser2.password, test_bankUser2.balance)

test_bankUser1.request_money(test_bankUser2, test_bankUser1, 5000)
print(test_bankUser1.name, test_bankUser1.pin, test_bankUser1.password, test_bankUser1.balance)
print(test_bankUser2.name, test_bankUser2.pin, test_bankUser2.password, test_bankUser2.balance)

# float = 2.154327
# format_float = "{:.2f}".format(float)
# print(format_float
