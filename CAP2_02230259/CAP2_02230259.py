#####################################################################
#Name: Ahasis Ghimiray
#Department: Mechanical Engineering
#Students_ID: 02230259
#####################################################################
# Reference:
'''
https://youtu.be/bSrm9RXwBaI
https://youtu.be/SiBw7os-_zI
https://youtu.be/xTh-ln2XhgU
'''

import random

class Account:
    def __init__(self, account_number, password, balance=0, username='', phone_number=''):
        # Initialize account with account number, password, username, phone number, and optional balance
        self.account_number = account_number
        self.password = password
        self.username = username
        self.phone_number = phone_number
        self.balance = balance

    def deposit(self, amount):
        # Deposit amount to account
        self.balance += amount
        return f"Deposit successful. Current balance: {self.balance}"

    def withdraw(self, amount):
        # Withdraw amount from account if sufficient funds are available
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrawal successful. Current balance: {self.balance}"
        else:
            return "Insufficient funds"

    def transfer(self, amount, recipient_account):
        # Transfer amount to another account if sufficient funds are available
        if self.balance >= amount:
            self.balance -= amount
            recipient_account.balance += amount
            return f"Transfer of {amount} to account {recipient_account.account_number} successful. Current balance: {self.balance}"
        else:
            return "Insufficient funds"

    def __str__(self):
        # Return account details as a string
        return f"Account Number: {self.account_number}, Balance: {self.balance}, Username: {self.username}, Phone Number: {self.phone_number}"

class PersonalAccount(Account):
    def __init__(self, account_number, password, balance=0, username='', phone_number=''):
        # Initialize a personal account
        super().__init__(account_number, password, balance, username, phone_number)
        self.account_type = "Personal"

class BusinessAccount(Account):
    def __init__(self, account_number, password, balance=0, username='', phone_number=''):
        # Initialize a business account
        super().__init__(account_number, password, balance, username, phone_number)
        self.account_type = "Business"

class Bank:
    def __init__(self):
        # Initialize the bank with an empty dictionary of accounts
        self.accounts = {}
        self.load_accounts()

    def create_account(self, account_type, username, phone_number):
        # Generate a random account number and password
        account_number = random.randint(100000000, 999999999)
        password = str(random.randint(1000, 9999))
        # Create either a PersonalAccount or BusinessAccount based on account_type
        if account_type == 'personal':
            account = PersonalAccount(account_number, password, username=username, phone_number=phone_number)
        elif account_type == 'business':
            account = BusinessAccount(account_number, password, username=username, phone_number=phone_number)
        # Add the new account to the bank's accounts dictionary
        self.accounts[account_number] = account
        self.save_accounts()
        return account

    def save_accounts(self):
        # Save account information to a text file
        with open("/Users/ahasis/Desktop/Semister Notes/CSF/CAP2_02230259/accounts.txt", "w") as file:
            for account in self.accounts.values():
                file.write(f"{account.account_number},{account.password},{account.account_type},{account.balance},{account.username},{account.phone_number}\n")

    def load_accounts(self):
        # Load account information from a text file
        try:
            with open("/Users/ahasis/Desktop/Semister Notes/CSF/CAP2_02230259/accounts.txt", "r") as file:
                for line in file:
                    account_number, password, account_type, balance, username, phone_number = line.strip().split(",")
                    account_number = int(account_number)
                    balance = float(balance)
                    if account_type == "Personal":
                        account = PersonalAccount(account_number, password, balance, username, phone_number)
                    elif account_type == "Business":
                        account = BusinessAccount(account_number, password, balance, username, phone_number)
                    self.accounts[account_number] = account
        except FileNotFoundError:
            pass

def main():
    bank = Bank()

    while True:
        # Display the main menu
        print("\nBank of Bhutan Limited")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Create a new account
            account_type = input("Enter account type (personal/business): ").lower()
            username = input("Enter your name: ")
            phone_number = input("Enter your phone number: ")
            account = bank.create_account(account_type, username, phone_number)
            print(f"Account created successfully. Account Number: {account.account_number}, Password: {account.password}")

        elif choice == "2":
            # Login to an existing account
            account_number = int(input("Enter account number: "))
            password = input("Enter password: ")
            if account_number in bank.accounts and bank.accounts[account_number].password == password:
                user = bank.accounts[account_number]
                print(f"Welcome, {user.username}!")
                while True:
                    # Display account options
                    print("\n1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Transfer Money")
                    print("5. Delete Account")
                    print("6. Logout")
                    option = input("Enter your choice: ")

                    if option == "1":
                        # Check balance
                        print("Balance:", user.balance)

                    elif option == "2":
                        # Deposit money
                        amount = float(input("Enter amount to deposit: "))
                        print(user.deposit(amount))
                        bank.save_accounts()

                    elif option == "3":
                        # Withdraw money
                        amount = float(input("Enter amount to withdraw: "))
                        print(user.withdraw(amount))
                        bank.save_accounts()

                    elif option == "4":
                        # Transfer money to another account
                        recipient_account_number = int(input("Enter recipient's account number: "))
                        if recipient_account_number in bank.accounts:
                            amount = float(input("Enter amount to transfer: "))
                            print(user.transfer(amount, bank.accounts[recipient_account_number]))
                            bank.save_accounts()
                        else:
                            print("Recipient account does not exist.")

                    elif option == "5":
                        # Delete account
                        confirm = input("Are you sure you want to delete your account? (yes/no): ").lower()
                        if confirm == "yes":
                            del bank.accounts[account_number]
                            bank.save_accounts()
                            print("Account deleted successfully.")
                            break
                        else:
                            print("Account deletion canceled.")

                    elif option == "6":
                        # Logout
                        print("Logged out successfully.")
                        break

                    else:
                        print("Invalid option.")

            else:
                print("Invalid account number or password.")

        elif choice == "3":
            # Exit the application
            print("Thank you for using Bank of Bhutan Limited.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
