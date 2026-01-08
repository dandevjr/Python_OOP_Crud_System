class UserProfile:
    def __init__(self, username):
        self.username = username          
        self.__isVerified = False         

    
    def _adminVerify(self, adminCode):
        """Secure method: Only accessible to authorized administrators."""
        ADMIN_CODE = "VERIFY2025"
        if adminCode == ADMIN_CODE:
            self.__isVerified = True
            print(f"User '{self.username}' has been successfully verified by admin.")
        else:
            print("Access denied. Invalid admin code.")

    
    def displayProfile(self):
        status = "Verified" if self.__isVerified else "Not Verified"
        print(f"Username: {self.username} | Status: {status}")



def menu():
    users = {
        "TechGuru": UserProfile("TechGuru"),
        "ArtExplorer": UserProfile("ArtExplorer")
    }

    while True:
        print("\n=== USER VERIFICATION SYSTEM ===")
        print("1. Add New User")
        print("2. View All Users")
        print("3. Verify a User (Admin Only)")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            new_username = input("Enter new username: ").strip()
            if new_username in users:
                print("This username already exists.")
            else:
                users[new_username] = UserProfile(new_username)
                print(f"User '{new_username}' has been added successfully.")

        elif choice == '2':
            if not users:
                print("No users found.")
            else:
                print("\n--- CURRENT USER PROFILES ---")
                for user in users.values():
                    user.displayProfile()

        elif choice == '3':
            adminCode = input("Enter Admin Code: ").strip()
            username = input("Enter username to verify: ").strip()
            if username in users:
                users[username]._adminVerify(adminCode)
            else:
                print("User not found.")

        elif choice == '4':
            print("Exiting system. Goodbye.")
            break

        else:
            print("Invalid option. Please try again.")


menu()
