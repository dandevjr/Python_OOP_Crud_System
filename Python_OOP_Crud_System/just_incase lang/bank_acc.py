class BankAccount:
    def __init__(self, user, balance=0):
        self.user = user                     
        self.__balance = balance               

    
    def get_balance(self):
        return self.__balance

    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f" Deposited ₱{amount:.2f} into {self.user}'s account. | New Balance: ₱{self.__balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    
    def withdraw(self, amount):
        if amount <= 0:
            print(" Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f" Withdrew ₱{amount:.2f} from {self.user}'s account. | New Balance: ₱{self.__balance:.2f}")

    
    def _set_initial_balance(self, new_balance, manager_passcode):
        """Secure method for manager to set or adjust balance directly."""
        ADMIN_PASS = "bankadmin123"  # 

        if manager_passcode != ADMIN_PASS:
            print(" Unauthorized access! Incorrect manager passcode.")
            return

        if new_balance < 0:
            print("Initial balance cannot be negative.")
            return

        self.__balance = new_balance
        print(f" Manager set {self.user}'s balance to ₱{self.__balance:.2f}.")


accounts = {}
manager_logged_in = False

while True:
    print("\n===  BANK SYSTEM MENU ===")
    print("1. Add User")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Manager Login")
    print("6. Manager: Set or Adjust Balance")
    print("7. Logout Manager")
    print("8. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter new user's name: ").lower().strip()
        if name in accounts:
            print("️ User already exists!")
        else:
            accounts[name] = BankAccount(name)
            print(f" Account created for {name} with starting balance ₱0.00.")

    elif choice == '2':
        name = input("Enter account name: ").lower().strip()
        if name in accounts:
            amount = float(input("Enter amount to deposit: "))
            accounts[name].deposit(amount)
        else:
            print(" Account not found.")

    elif choice == '3':
        name = input("Enter account name: ").lower().strip()
        if name in accounts:
            amount = float(input("Enter amount to withdraw: "))
            accounts[name].withdraw(amount)
        else:
            print(" Account not found.")

    elif choice == '4':
        name = input("Enter account name: ").lower().strip()
        if name in accounts:
            print(f"{name}'s Balance: ₱{accounts[name].get_balance():.2f}")
        else:
            print(" Account not found.")

    elif choice == '5':
        if manager_logged_in:
            print(" Manager already logged in.")
        else:
            passcode = input("Enter manager passcode: ")
            if passcode == "bankadmin123":
                manager_logged_in = True
                print(" Manager access granted.")
            else:
                print(" Incorrect manager passcode.")

    elif choice == '6':
        if not manager_logged_in:
            print(" Manager access required. Please log in first.")
        else:
            name = input("Enter account name to set balance: ").lower().strip()
            if name in accounts:
                new_balance = float(input(f"Enter new balance for {name}: "))
                accounts[name]._set_initial_balance(new_balance, "bankadmin123")
            else:
                print(" Account not found.")

    elif choice == '7':
        if manager_logged_in:
            manager_logged_in = False
            print(" Manager logged out successfully.")
        else:
            print("️ No manager currently logged in.")

    elif choice == '8':
        print(" Thank you for using the Bank System. Goodbye!")
        break

    else:
        print(" Invalid option. Try again.")
