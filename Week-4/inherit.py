class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, password):
        self.password = password
        print("Your password has been changed to {}".format(self.password))

class BankUser(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.balance = 0

    def check_balance(self):
        print("{} has an account balance of: {}".format(self.name, self.balance))
    
bankuser1 = BankUser("Jane", "jane@nucamp.co", "bestpassword")

