class GameCharacter:
    def __init__(self, playerName):
        self.playerName = playerName        # Public attribute
        self.health = 100                   # Public attribute
        self.__mana = 100                   # Private attribute

    def takeDamage(self, amount):
        if amount > 0:
            self.health -= amount
            if self.health < 0:
                self.health = 0
            print(f"{self.playerName} took {amount} damage.")
        else:
            print("Invalid damage amount.")

    def addHealth(self, amount):
        if amount > 0 and amount != 100:
            self.health += amount
            print(f"{self.playerName} healed by {amount}.")
        else:
            print("Invalid or suspicious healing amount. Action blocked.")

    def castSpell(self, cost):
        if cost > 0 and cost <= self.__mana:
            self.__mana -= cost
            print(f"{self.playerName} cast a spell costing {cost} mana.")
            self.regenMana()
        elif cost == 100:
            print("Suspicious mana input detected. Action blocked.")
        else:
            print("Not enough mana to cast the spell.")

    def regenMana(self):
        self.__mana = 100
        print(f"{self.playerName}'s mana has been regenerated.")

    def displayStats(self):
        print(f"Player: {self.playerName}")
        print(f"Health: {self.health}")
        print(f"Mana: {self.__mana}")

    def updateName(self, new_name):
        self.playerName = new_name
        print(f"Player name updated to '{new_name}'.")

# Sample character
characters = {
    "Hero1": GameCharacter("Nullroot")
}

# Main menu loop
while True:
    print("\nGAME CHARACTER SYSTEM")
    print("1. Create Multiple Characters")
    print("2. View All Characters")
    print("3. Take Damage")
    print("4. Add Health")
    print("5. Cast Spell")
    print("6. Update Character Name")
    print("7. Delete Character")
    print("8. Encapsulation Test")
    print("9. Exit")

    choice = input("Choose an option (1-9): ").strip()

    if choice == "1":
        count = int(input("How many characters do you want to create? "))
        for i in range(count):
            print(f"\nCreating character {i+1} of {count}")
            key = input("Enter character ID: ")
            if key in characters:
                print("Character ID already exists.")
            else:
                name = input("Enter player name: ")
                characters[key] = GameCharacter(name)
                print(f"Character '{key}' created.")

    elif choice == "2":
        print("\nAll Characters:")
        if not characters:
            print("No characters available.")
        else:
            for key, char in characters.items():
                print(f"\nCharacter ID: {key}")
                char.displayStats()

    elif choice == "3":
        key = input("Enter character ID to damage: ")
        if key in characters:
            amount = int(input("Enter damage amount: "))
            characters[key].takeDamage(amount)
        else:
            print("Character not found.")

    elif choice == "4":
        key = input("Enter character ID to heal: ")
        if key in characters:
            amount = int(input("Enter healing amount: "))
            characters[key].addHealth(amount)
        else:
            print("Character not found.")

    elif choice == "5":
        key = input("Enter character ID to cast spell: ")
        if key in characters:
            cost = int(input("Enter spell mana cost: "))
            characters[key].castSpell(cost)
        else:
            print("Character not found.")

    elif choice == "6":
        key = input("Enter character ID to rename: ")
        if key in characters:
            new_name = input("Enter new player name: ")
            characters[key].updateName(new_name)
        else:
            print("Character not found.")

    elif choice == "7":
        key = input("Enter character ID to delete: ")
        if key in characters:
            del characters[key]
            print(f"Character '{key}' deleted.")
        else:
            print("Character not found.")

    elif choice == "8":
        print("\nEncapsulation Test:")
        for key, char in characters.items():
            print(f"\nCharacter ID: {key}")
            try:
                char.__mana = 1000
                print("Direct mana modification attempted.")
            except:
                print("Direct modification blocked.")
            char.displayStats()

        
    elif choice == "9":
        print("Exiting character system.")
        break

    else:
        print("Invalid choice. Please select from 1 to 9.")