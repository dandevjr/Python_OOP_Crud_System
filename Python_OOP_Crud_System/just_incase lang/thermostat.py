import time

class SmartThermostat:
    def __init__(self, roomName, targetTemperature=22):
        self.roomName = roomName                     
        self.__targetTemperature = targetTemperature  
        self.__minTemp = 16                           
        self.__maxTemp = 30                           

    
    def getTemperature(self):
        return self.__targetTemperature


    def increaseTemp(self, increase_amount):
        if increase_amount <= 0:
            print("Temperature increase must be positive.")
            return

        new_temp = self.__targetTemperature + increase_amount
        if new_temp > self.__maxTemp:
            print(f"Cannot exceed safe limit ({self.__maxTemp}°C).")
        else:
            self.__targetTemperature = new_temp
            print(f"{self.roomName}: Increased to {self.__targetTemperature}°C")

  
    def decreaseTemp(self, decrease_amount):
        if decrease_amount <= 0:
            print("Temperature decrease must be positive.")
            return

        new_temp = self.__targetTemperature - decrease_amount
        if new_temp < self.__minTemp:
            print(f"Cannot go below safe limit ({self.__minTemp}°C).")
        else:
            self.__targetTemperature = new_temp
            print(f"{self.roomName}: Decreased to {self.__targetTemperature}°C")

    def _overrideTemperature(self, newTemp, authCode):
        """Privileged diagnostic method — technician only."""
        TECHNICIAN_CODE = "ADMIN123"
        if authCode != TECHNICIAN_CODE:
            print("Access denied. Invalid technician code.")
            return
        self.__targetTemperature = newTemp
        print(f"Technician override: {self.roomName} set to {self.__targetTemperature}°C")

   
    def diagnosticOverride(self, newTemp, authCode, duration=5):
        """Allows technician to temporarily override temperature limits for diagnostics."""
        TECHNICIAN_CODE = "ADMIN123"
        if authCode != TECHNICIAN_CODE:
            print("Access denied. Invalid technician code.")
            return

        print(f"Diagnostic override activated for {self.roomName}.")
        print(f"Temporarily setting temperature to {newTemp}°C for {duration} seconds.")

        original_temp = self.__targetTemperature
        self.__targetTemperature = newTemp
        time.sleep(duration)

        
        self.__targetTemperature = original_temp
        print(f"Diagnostic override ended. Temperature restored to {self.__targetTemperature}°C")

 
    def displayStatus(self):
        print(f"Room: {self.roomName} | Target Temp: {self.__targetTemperature}°C")



def menu():
    thermostats = {}

    while True:
        print("\n=== SMART THERMOSTAT SYSTEM ===")
        print("1. Add New Thermostat")
        print("2. View All Thermostats")
        print("3. Increase Temperature")
        print("4. Decrease Temperature")
        print("5. Technician Override")
        print("6. Diagnostic Override")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter room name: ").capitalize()
            if name in thermostats:
                print("Thermostat already exists for that room.")
            else:
                thermostats[name] = SmartThermostat(name)
                print(f"Thermostat created for {name}.")

        elif choice == '2':
            if not thermostats:
                print("No thermostats found.")
            else:
                print("\nCurrent Thermostat Status:")
                for t in thermostats.values():
                    t.displayStatus()

        elif choice == '3':
            name = input("Enter room name: ").capitalize()
            if name in thermostats:
                amt = int(input("Enter temperature increase amount: "))
                thermostats[name].increaseTemp(amt)
            else:
                print("Thermostat not found.")

        elif choice == '4':
            name = input("Enter room name: ").capitalize()
            if name in thermostats:
                amt = int(input("Enter temperature decrease amount: "))
                thermostats[name].decreaseTemp(amt)
            else:
                print("Thermostat not found.")

        elif choice == '5':
            name = input("Enter room name: ").capitalize()
            if name in thermostats:
                newTemp = int(input("Enter new temperature: "))
                code = input("Enter Technician Code: ")
                thermostats[name]._overrideTemperature(newTemp, code)
            else:
                print("Thermostat not found.")

        elif choice == '6':
            name = input("Enter room name: ").capitalize()
            if name in thermostats:
                newTemp = int(input("Enter diagnostic temperature: "))
                duration = int(input("Enter duration in seconds: "))
                code = input("Enter Technician Code: ")
                thermostats[name].diagnosticOverride(newTemp, code, duration)
            else:
                print("Thermostat not found.")

        elif choice == '7':
            print("Exiting system. Goodbye.")
            break

        else:
            print("Invalid option. Please try again.")

# ---------------- MAIN EXECUTION ---------------- #

menu()
