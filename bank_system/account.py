from random import randint

class Account:
    number = 0
    pin = 0
    balance = 0

    # constructor
    def __init__(self, number, balance):
        self.number = number
        self.balance = balance

    def __init__(self): # register
        self.number = randint(0000,9999)
        self.balance = 0
        
        print("Your account number is:", self.number)
        value = int(input("Enter a security pin: "))
        self.set_pin(value)

    def set_pin(self, value):
        self.pin = value

        print("Pin has been set.")
    

    def deposit(self, amount):
        print("Deposited:", amount)
        self.balance += amount

        print("Current balance:", self.balance)

    def withdraw(self, amount):
        print("Withdrew:", amount)
        self.balance -= amount

        print("Current balance:", self.balance)

    def balance_inquiry (self):
        print("Your balance is:", self.balance)