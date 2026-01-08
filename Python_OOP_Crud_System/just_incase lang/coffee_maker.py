class CoffeeMaker:
    def __init__(self, brand, waterLevel=100, beanLevel=100):
        self.brand = brand                     
        self.__waterLevel = waterLevel         
        self.__beanLevel = beanLevel

  
    def brewCoffee(self):
        print(f"\n[{self.brand}] Starting to brew coffee...")

        # Check resources first
        if self.__waterLevel < 20:
            print(" Not enough water to brew coffee!")
            return
        if self.__beanLevel < 10:
            print("Not enough beans to brew coffee!")
            return

        # Brew and reduce resources
        self.__waterLevel -= 20
        self.__beanLevel -= 10
        print("Coffee brewed successfully!")
        print(f"Remaining: Water = {self.__waterLevel}%, Beans = {self.__beanLevel}%")

    def refillWater(self, amount):
        if amount <= 0:
            print("Amount must be positive!")
            return
        self.__waterLevel = min(100, self.__waterLevel + amount)
        print(f"Water refilled. Current level: {self.__waterLevel}%")

    def refillBeans(self, amount):
        if amount <= 0:
            print("Amount must be positive!")
            return
        self.__beanLevel = min(100, self.__beanLevel + amount)
        print(f" Beans refilled. Current level: {self.__beanLevel}%")

  
    def getWaterLevel(self):
        return self.__waterLevel

    def getBeanLevel(self):
        return self.__beanLevel



machines = {}

while True:
    print("\n=== COFFEE MAKER CONTROL PANEL ===")
    print("1. Add Coffee Machine")
    print("2. Show Machine Status")
    print("3. Brew Coffee")
    print("4. Refill Water")
    print("5. Refill Beans")
    print("6. Try to Cheat (Directly Modify Private Values)")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        brand = input("Enter coffee machine brand: ")
        if brand in machines:
            print("Machine already exists!")
        else:
            machines[brand] = CoffeeMaker(brand)
            print(f"Coffee machine '{brand}' added successfully.")

    elif choice == '2':
        if not machines:
            print("No coffee machines available.")
        else:
            print("\n--- Current Coffee Machines ---")
            for m in machines.values():
                print(f"{m.brand}: Water = {m.getWaterLevel()}%, Beans = {m.getBeanLevel()}%")

    elif choice == '3':
        brand = input("Enter machine brand to brew coffee: ")
        if brand in machines:
            machines[brand].brewCoffee()
        else:
            print("Machine not found!")

    elif choice == '4':
        brand = input("Enter machine brand to refill water: ")
        if brand in machines:
            amount = int(input("Enter amount to refill: "))
            machines[brand].refillWater(amount)
        else:
            print("Machine not found!")

    elif choice == '5':
        brand = input("Enter machine brand to refill beans: ")
        if brand in machines:
            amount = int(input("Enter amount to refill: "))
            machines[brand].refillBeans(amount)
        else:
            print("Machine not found!")

    elif choice == '6':
        print("\n--- Encapsulation Demonstration ---")
        demo = CoffeeMaker("DemoBrew 5000")
        demo.brewCoffee()
        print(f"Before cheat: Water = {demo.getWaterLevel()}%, Beans = {demo.getBeanLevel()}%")

        print("\nAttempting to cheat by directly setting private attributes...")
        demo.__waterLevel = 0
        demo.__beanLevel = 0

        # Attempt to brew again
        demo.brewCoffee()

        print(f"\nActual Internal Status:")
        print(f"Water Level: {demo.getWaterLevel()}%")
        print(f"Bean Level: {demo.getBeanLevel()}%")

        print("\nWhy cheat fails:")
        print("Because __waterLevel and __beanLevel are private attributes.")
        print("Python automatically renames them internally to _CoffeeMaker__waterLevel.")
        print("When you assign demo.__waterLevel = 0, it just creates a *new public variable*")
        print("— it does NOT change the real private ones inside the object.")

    elif choice == '7':
        print("Exiting Coffee Control Panel. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
