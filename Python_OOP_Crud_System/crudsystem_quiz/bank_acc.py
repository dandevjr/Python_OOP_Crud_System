class BankAccount:
    def __init__(self, name, account_type, balance):
        self.name = name
        self.account_type = account_type
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):  # GETTER
        return self.__balance

    def set_balance(self, new_balance):  # SETTER
        print("Direct balance modification not allowed.")

    def display_details(self):
        print(f"Name: {self.name}, Type: {self.account_type}, Balance: {self.__balance:.2f}")

accounts = [
    BankAccount("Jack", "Savings", 5000),
    BankAccount("Romar", "Checking", 3000)
]

while True:
    print("\nBANK ACCOUNT MANAGER")
    print("1. Add Account")
    print("2. View All Accounts")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Encapsulation Test")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        name = input("Enter name: ")
        acc_type = input("Enter account type: ")
        balance = float(input("Enter initial balance: "))
        if balance < 0:
            print("Error: Balance must be non-negative.")
        else:
            accounts.append(BankAccount(name, acc_type, balance))
            print(f"'{name}' added.")

    elif choice == "2":
        if not accounts:
            print("No accounts found.")
        else:
            for i, acc in enumerate(accounts, start=1):
                print(f"{i}. ", end="")
                acc.display_details()

    elif choice == "3":
        name = input("Enter account name: ")
        amount = float(input("Enter deposit amount: "))
        for acc in accounts:
            if acc.name.lower() == name.lower():
                acc.deposit(amount)
                print("Deposit successful.")
                break
        else:
            print("Account not found.")

    elif choice == "4":
        name = input("Enter account name: ")
        amount = float(input("Enter withdrawal amount: "))
        for acc in accounts:
            if acc.name.lower() == name.lower():
                acc.withdraw(amount)
                break
        else:
            print("Account not found.")

    elif choice == "5":  # ENCAPSULATION TEST
        for acc in accounts:
            print(f"{acc.name} balance access: {acc.get_balance():.2f}")

    elif choice == "6":
        break

    else:
        print("Invalid choice.")