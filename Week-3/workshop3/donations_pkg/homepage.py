def show_homepage():
    print("\n       === DonateMe Homepage ===          ")
    print("------------------------------------------")
    print("| 1.   Login       | 2.   Register        |")
    print("------------------------------------------")
    print("| 3.   Donate      | 4.   Show Donations  |")
    print("------------------------------------------")
    print("|              5.   Exit                  |")
    print("------------------------------------------")

def donate(username):
    donate_amt = float(input("Enter amount to donate: "))
    donation = "{} donated ${}".format(username, donate_amt)
    print("Thank you for donating!")
    return donation

def show_donations(donations):
    print("\n--- All Donations ---")
    if not donations:
        print("Currently, there are no donations.")
    else:
        for donation in donations:
            print(donation)