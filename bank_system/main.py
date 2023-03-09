from random import randint
from account import Account
from atm import ATM

accounts = [] # initialize array
atm = None
logout = 0
exit = 0

def login():
    print("Welcome to Bank!")
    print("[1] Login\n[2] Register\n[3] Exit")
    choice = int(input("Enter: "))

    if choice == 1: # Login
        number = int(input("Enter account number: "))

        if not accounts: # check if empty
            print("No accounts registered")
        else:
            array_length = len(accounts)
            for i in range(array_length):
                if number == accounts[i].number:
                    pin = int(input("Enter pin: "))
                    if accounts[i].pin == pin:
                        atm = ATM(accounts[i])
                        print("Successfuly logged in to Account number:", number)
                        return atm
                    else:
                        print("Invalid pin")
                        return None
                else:
                    print("Invalid account number/pin")
                    return None
            
    elif choice == 2: # Register
        acc = Account() # initialize
        accounts.append(acc) # append to account array
        atm = ATM(acc)
        return atm
    
    elif choice == 3: # Exit program
        quit()

    else:
        print("Invalid input")
        return None

while exit == 0:
    atm = None
    logout = 0
    while atm is None:
        atm = login()

    while logout == 0:
        logout = atm.main_menu()