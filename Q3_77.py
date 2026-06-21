# -*- coding: utf-8 -*-
"""
@author: Kandidatnr: 77
Question 3.
"""

class Menu: 
    def __init__(self):
        self.options = []
    
    def add_option(self, option):
        self.options.append(option)
        
    def get_input(self):
        done = False
        while not done:
            print("\n" + "="*41)
            for i in range(len(self.options)):
                print("%d %s" % (i+1, self.options[i]))
             
            print("="*41 + "\n")    
            try:
                user_choice = int(input("Enter your option: "))
                if (user_choice >= 1 and user_choice <= len(self.options)):
                    done = True
                else:
                    print("\nInvalid option.")
            except ValueError:
                print("\nPlease enter a valid number.\n")
        return user_choice
                    

class BankAccount:
    def __init__(self):
        self.balance = 0.0
        
    def deposit(self, amount):
        if amount <= 0:
            print("\nDeposit amount cannot be negative!\n")
        else:
            self.balance += amount
        
    def withdraw(self, amount):
        if amount <= 0:
            print("\nWithdrawal amount cannot be negative!\n")
        elif amount > self.balance:
            print("\nYou have insufficient funds.")
        else:
            self.balance -= amount
        
    def add_interest(self):
        if self.balance <= 0:
            print("\nYou have insufficient funds.")
        else:
            interest = self.balance * 0.12
            self.balance += interest
            print(f"\nYour interest is: ${interest:.2f} (12%).")
        
    def get_balance(self):
        return self.balance


def main():
    account_error_msg = "\n--Please open an account first.--"
    
    menu = Menu()
    menu.add_option("Open a new account")
    menu.add_option("Deposit money into your account")
    menu.add_option("Withdraw money from your account")
    menu.add_option("Add interests to your account")
    menu.add_option("Get the current balance of your account")
    menu.add_option("Quit")
    
    account = None

    while True:
        choice = menu.get_input()
        
        if choice == 1:
            account = BankAccount()
            print("\nAccount opened successfully.")
        elif choice == 2:
            if account is None:
                print(account_error_msg)
            else:
                amount = float(input("\nEnter amount to deposit: "))
                account.deposit(amount)
                print("Amount deposited successfully.")
        elif choice == 3:
            if account is None:
                print(account_error_msg)
            else:
                amount = float(input("\nEnter amount to withdraw: "))
                account.withdraw(amount)
                print("Amount withdrawn successfully.")
        elif choice == 4:
            if account is None:
                print(account_error_msg)
            else:
                account.add_interest()
                print("\nInterest is added.")
        elif choice == 5:
            if account is None:
                print(account_error_msg)
            else:
                balance = account.get_balance()
                print(f"\nCurrent balance: ${balance:.2f}")
        elif choice == 6:
            print("\n\nThank you for using the Bank Account Management System 77!")
            break
main()
            





