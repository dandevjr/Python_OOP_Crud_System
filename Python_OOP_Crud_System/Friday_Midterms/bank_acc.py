class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.__balance = 0  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{self.owner} deposited ${amount}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"{self.owner} withdrew ${amount}.")
            else:
                print(f"Error: {self.owner} tried to withdraw ${amount}, but only ${self.__balance} is available. Transaction denied.")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

    def display_account(self):
        print(f"Account Owner: {self.owner}, Balance: ${self.__balance}")

    def _admin_set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
            print(f"Admin set initial balance for {self.owner} to ${amount}.")
        else:
            print("Invalid initial balance. Must be non-negative.")

# Account storage
accounts = {}

# Admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"

def admin_login():
    print("\nADMIN LOGIN")
    username = input("Username: ")
    password = input("Password: ")
    return username == ADMIN_USERNAME and password == ADMIN_PASSWORD

# Main menu loop
while True:
    print("\nBANK ACCOUNT ATM SYSTEM")
    print("1. Add Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View Balance")
    print("5. Admin: Set Initial Balance")
    print("6. View All Accounts")
    print("7. Exit")

    choice = input("Choose an option (1-7): ").strip()

    if choice == "1":
        name = input("Enter new account holder name: ")
        if name in accounts:
            print("Account already exists.")
        else:
            accounts[name] = BankAccount(name)
            print(f"Account created for {name}.")

    elif choice == "2":
        name = input("Enter account holder name: ")
        if name in accounts:
            amount = float(input("Enter deposit amount: "))
            accounts[name].deposit(amount)
        else:
            print("Account not found.")

    elif choice == "3":
        name = input("Enter account holder name: ")
        if name in accounts:
            amount = float(input("Enter withdrawal amount: "))
            accounts[name].withdraw(amount)
        else:
            print("Account not found.")

    elif choice == "4":
        name = input("Enter account holder name: ")
        if name in accounts:
            balance = accounts[name].get_balance()
            print(f"{name}'s current balance: ${balance}")
        else:
            print("Account not found.")

    elif choice == "5":
        if admin_login():
            name = input("Enter account holder name to set balance: ")
            if name in accounts:
                amount = float(input("Enter initial balance: "))
                accounts[name]._admin_set_balance(amount)
            else:
                print("Account not found.")
        else:
            print("Access denied. Invalid admin credentials.")

    elif choice == "6":
        print("\nAll Accounts:")
        for account in accounts.values():
            account.display_account()

        print("\nEncapsulation Test:")
        for account in accounts.values():
            try:
                print(account.__balance)
            except AttributeError:
                print(f"{account.owner}: Cannot access __balance directly (encapsulation works).")
            print(f"{account.owner} balance via method: ${account.get_balance()}")

    elif choice == "7":
        print("Exiting ATM system.")
        break

    else:
        print("Invalid choice. Please select from 1 to 7.")