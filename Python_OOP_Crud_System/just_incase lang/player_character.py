class PlayerCharacter:
    def __init__(self, playerName, healthPoints=100, manaPoints=100, maxhealth=100, maxmana=100):
        self.playerName = playerName            
        self.__healthPoints = healthPoints         
        self.__manaPoints = manaPoints
        self.__maxhealth = maxhealth
        self.__maxmana = maxmana

  
    def getHealth(self):
        return self.__healthPoints

    def getMana(self):
        return self.__manaPoints

    
    def takeDamage(self, damage_amount):
        if damage_amount < 0:
            print("Damage must be positive!")
            return
        old_hp = self.__healthPoints
        self.__healthPoints = max(0, self.__healthPoints - damage_amount)
        print(f"{self.playerName} took {damage_amount} damage! HP: {old_hp} → {self.__healthPoints}/{self.__maxhealth}")

    def heal(self, heal_amount):
        if heal_amount < 0:
            print("Heal amount must be positive!")
            return

        if self.__healthPoints == self.__maxhealth:
            print(f"{self.playerName} is already at full health! (Overheal: {heal_amount})")
            return

        old_hp = self.__healthPoints
        new_hp = self.__healthPoints + heal_amount

        if new_hp > self.__maxhealth:
            overheal = new_hp - self.__maxhealth
            self.__healthPoints = self.__maxhealth
            print(f"{self.playerName} healed {heal_amount - overheal} HP (+{overheal} overheal). HP: {old_hp} → {self.__healthPoints}/{self.__maxhealth}")
        else:
            self.__healthPoints = new_hp
            print(f"{self.playerName} healed {heal_amount} HP! HP: {old_hp} → {self.__healthPoints}/{self.__maxhealth}")

    def castSpell(self, manaCost):
        if manaCost <= 0:
            print("Mana cost must be positive!")
            return
        if manaCost > self.__manaPoints:
            print(f"{self.playerName} tried to cast a spell but lacks mana! ({self.__manaPoints}/{self.__maxmana})")
        else:
            old_mana = self.__manaPoints
            self.__manaPoints -= manaCost
            print(f"{self.playerName} cast a spell! Mana: {old_mana} → {self.__manaPoints}/{self.__maxmana}")

    def restoreMana(self, restore_amount):
        if restore_amount <= 0:
            print("Restore amount must be positive!")
            return
        if self.__manaPoints == self.__maxmana:
            print(f"{self.playerName}'s mana is already full! (Overrestore: {restore_amount})")
            return

        old_mana = self.__manaPoints
        new_mana = self.__manaPoints + restore_amount

        if new_mana > self.__maxmana:
            over = new_mana - self.__maxmana
            self.__manaPoints = self.__maxmana
            print(f"{self.playerName} restored {restore_amount - over} mana (+{over} overrestore). MP: {old_mana} → {self.__manaPoints}/{self.__maxmana}")
        else:
            self.__manaPoints = new_mana
            print(f"{self.playerName} restored {restore_amount} mana! MP: {old_mana} → {self.__manaPoints}/{self.__maxmana}")

    # --- Game Master privileged methods ---
    def _setHealthByGM(self, newHealth):
        if not (0 <= newHealth <= self.__maxhealth):
            print("Invalid HP value — must be between 0 and 100.")
            return
        self.__healthPoints = newHealth
        print(f"Game Master set {self.playerName}'s HP to {self.__healthPoints}/{self.__maxhealth}")

    def _setManaByGM(self, newMana):
        if not (0 <= newMana <= self.__maxmana):
            print("Invalid Mana value — must be between 0 and 100.")
            return
        self.__manaPoints = newMana
        print(f"Game Master set {self.playerName}'s Mana to {self.__manaPoints}/{self.__maxmana}")


# --- MAIN MENU ---
players = {}

while True:
    print("\n=== PLAYER MANAGEMENT MENU ===")
    print("1. Add Player")
    print("2. Show All Players")
    print("3. Damage a Player")
    print("4. Heal a Player")
    print("5. Cast Spell (Use Mana)")
    print("6. Restore Mana")
    print("7. GM Set Health")
    print("8. GM Set Mana")
    print("9. Demonstrate Encapsulation Cheat Fail")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter new player name: ")
        if name in players:
            print("Player already exists!")
        else:
            players[name] = PlayerCharacter(name)
            print(f"Player '{name}' has joined the game!")

    elif choice == '2':
        if not players:
            print("No players yet.")
        else:
            print("\n--- Current Players ---")
            for p in players.values():
                print(f"{p.playerName}: {p.getHealth()}/100 HP, {p.getMana()}/100 MP")

    elif choice == '3':
        name = input("Enter player name to damage: ")
        if name in players:
            dmg = int(input("Enter damage amount: "))
            players[name].takeDamage(dmg)
        else:
            print("Player not found!")

    elif choice == '4':
        name = input("Enter player name to heal: ")
        if name in players:
            heal = int(input("Enter heal amount: "))
            players[name].heal(heal)
        else:
            print("Player not found!")

    elif choice == '5':
        name = input("Enter player name to cast spell: ")
        if name in players:
            cost = int(input("Enter mana cost: "))
            players[name].castSpell(cost)
        else:
            print("Player not found!")

    elif choice == '6':
        name = input("Enter player name to restore mana: ")
        if name in players:
            amount = int(input("Enter amount to restore: "))
            players[name].restoreMana(amount)
        else:
            print("Player not found!")

    elif choice == '7':
        name = input("Enter player name to set HP (GM use): ")
        if name in players:
            hp = int(input("Enter new HP value: "))
            players[name]._setHealthByGM(hp)
        else:
            print("Player not found!")

    elif choice == '8':
        name = input("Enter player name to set Mana (GM use): ")
        if name in players:
            mana = int(input("Enter new Mana value: "))
            players[name]._setManaByGM(mana)
        else:
            print("Player not found!")

    elif choice == '9':
        print("\n--- Encapsulation Demonstration ---")
        hero = PlayerCharacter("Hero")
        hero.castSpell(20)
        print(f"After casting spell: Mana = {hero.getMana()}")

        print("\nNow trying to 'cheat' by directly setting mana and health...")
      
        hero.__manaPoints = 100
        hero.__healthPoints = 100

        print("After attempted cheat:")
        print(f"Actual Health: {hero.getHealth()}")  
        print(f"Actual Mana: {hero.getMana()}")      
        print("\nWhy cheat fails:")
        print("Because __healthPoints and __manaPoints are private. "
              "Python name-mangles them (stored as _PlayerCharacter__healthPoints internally), "
              "so assigning hero.__manaPoints just creates a *new* public variable "
              "instead of modifying the real private ones inside the class.")

    elif choice == '10':
        print("Exiting the game. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
