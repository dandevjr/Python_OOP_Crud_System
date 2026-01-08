class BankAccount:
    def __init__(self, name, account_type, balance):
        self.name = name                    # public
        self._account_type = account_type   # protected
        self.__balance = balance            # private

    def get_account_type(self):  # GETTER
        return self._account_type

    def set_account_type(self, value):  # SETTER
        self._account_type = value

    def get_balance(self):  # GETTER
        return self.__balance

    def set_balance(self, value):  # SETTER
        if value >= 0:
            self.__balance = value
        else:
            print("Invalid balance. Must be non-negative.")

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

    def display_details(self):
        print(f"Name: {self.name}, Type: {self._account_type}, Balance: {self.__balance:.2f}")

accounts = [
    BankAccount("Jack", "Savings", 5000),
    BankAccount("Romar", "Checking", 3000)
]

while True:
    print("\nBANK ACCOUNT SYSTEM")
    print("1. View All Accounts")
    print("2. Add New Account")
    print("3. Update Account")
    print("4. Delete Account")
    print("5. Deposit / Withdraw")
    print("6. Encapsulation Test")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")

    if choice == "1":
        if not accounts:
            print("No accounts found.")
        else:
            for i, acc in enumerate(accounts, start=1):  # TRAVERSAL
                print(f"{i}. ", end="")
                acc.display_details()

    elif choice == "2":
        name = input("Enter account holder name: ")
        acc_type = input("Enter account type: ")
        balance = float(input("Enter initial balance: "))
        if balance < 0:
            print("Error: Balance must be non-negative.")
        else:
            accounts.append(BankAccount(name, acc_type, balance))  # OBJECT CREATION
            print(f"'{name}' added successfully.")

    elif choice == "3":
        update_name = input("Enter account holder name to update: ")
        found = False
        for acc in accounts:
            if acc.name.lower() == update_name.lower():
                new_type = input("Enter new account type: ")
                new_balance = float(input("Enter new balance: "))
                acc.set_account_type(new_type)
                acc.set_balance(new_balance)
                print("Account updated.")
                found = True
                break
        if not found:
            print("Account not found.")

    elif choice == "4":
        delete_name = input("Enter account holder name to delete: ")
        for acc in accounts:
            if acc.name.lower() == delete_name.lower():
                accounts.remove(acc)
                print(f"Account for '{delete_name}' deleted.")
                break
        else:
            print("Account not found.")

    elif choice == "5":
        trans_name = input("Enter account holder name: ")
        for acc in accounts:
            if acc.name.lower() == trans_name.lower():
                action = input("Deposit or Withdraw (D/W): ").strip().upper()
                amount = float(input("Enter amount: "))
                if action == "D":
                    acc.deposit(amount)
                elif action == "W":
                    acc.withdraw(amount)
                else:
                    print("Invalid action.")
                break
        else:
            print("Account not found.")

    elif choice == "6":  # ENCAPSULATION TEST
        for acc in accounts:
            print(f"{acc.name} | Type: {acc.get_account_type()} | Balance: {acc.get_balance():.2f}")

    elif choice == "7":
        print("Exiting system.")
        break

    else:
        print("Invalid choice.")