class CrushDigit:
    def __init__(self, text, shift, rounds):
        self.original_text = text
        self.shift = shift
        self.rounds = rounds
        self.encrypted_text = ""
        self.decrypted_text = ""

    def crush_digit(self, text, shift):
        result = ""
        for char in text:
            if char.isdigit():
                result += str((int(char) + shift) % 10)
            else:
                result += char
        return result

    def encrypt(self):
        print("\nEncryption rounds:")
        self.encrypted_text = self.original_text
        for i in range(1, self.rounds + 1):
            self.encrypted_text = self.crush_digit(self.encrypted_text, self.shift)
            print(f"Round {i}: {self.encrypted_text}")

    def decrypt(self):
        print("\nDecryption rounds:")
        self.decrypted_text = self.encrypted_text
        for i in range(1, self.rounds + 1):
            self.decrypted_text = self.crush_digit(self.decrypted_text, -self.shift)
            print(f"Round {i}: {self.decrypted_text}")

    def display_all(self):
        print(f"\nOriginal Text: {self.original_text}")
        print(f"Encrypted Text: {self.encrypted_text}")
        print(f"Decrypted Text: {self.decrypted_text}")

# Initial object
crush = CrushDigit("12072008", 3, 10)

# Menu loop
while True:
    print("\nCRUSHDIGIT ENCRYPTION SYSTEM")
    print("1. Encrypt Text")
    print("2. Decrypt Text")
    print("3. View All Texts")
    print("4. Update Text / Shift / Rounds")
    print("5. Exit")

    choice = input("Choose an option (1-5): ").strip()

    if choice == "1":
        crush.encrypt()

    elif choice == "2":
        crush.decrypt()

    elif choice == "3":
        crush.display_all()

    elif choice == "4":
        new_text = input("Enter new text: ")
        new_shift = int(input("Enter new shift value: "))
        new_rounds = int(input("Enter number of rounds: "))
        crush = CrushDigit(new_text, new_shift, new_rounds)
        print("Values updated.")

    elif choice == "5":
        print("Exiting system.")
        break

    else:
        print("Invalid choice. Please select from 1 to 5.")