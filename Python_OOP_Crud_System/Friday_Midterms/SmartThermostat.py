class SmartThermostat:
    def __init__(self, roomName, initialTemp, securityPin):
        self.roomName = roomName                    # Public attribute
        self.__currentTemperature = initialTemp     # Private attribute
        self.__securityPin = securityPin            # Private attribute

    def setTemperature(self, degrees, pin):
        if pin == self.__securityPin:
            self.__currentTemperature = degrees
            print(f"Temperature set to {degrees}°C in {self.roomName}.")
        else:
            print("Invalid security PIN. Temperature not changed.") 

    def get_status(self):
        print(f"Room: {self.roomName}")
        print(f"Current Temperature: {self.__currentTemperature}°C")

    def update_room_name(self, new_name):
        self.roomName = new_name
        print(f"Room name updated to '{new_name}'.")

# Sample thermostat object
thermostats = {
    "Thermo1": SmartThermostat("Living Room", 24, "1234")
}

# Main menu loop
while True:
    print("\nSMART THERMOSTAT SYSTEM")
    print("1. Add Multiple Thermostats")
    print("2. View All Thermostats")
    print("3. Set Temperature")
    print("4. Update Room Name")
    print("5. Delete Thermostat")
    print("6. Encapsulation Test")
    print("7. Exit")

    choice = input("Choose an option (1-7): ").strip()

    if choice == "1":
        count = int(input("How many thermostats do you want to add? "))
        for i in range(count):
            print(f"\nCreating thermostat {i+1} of {count}")
            key = input("Enter thermostat ID: ")
            if key in thermostats:
                print("Thermostat ID already exists.")
            else:
                room = input("Enter room name: ")
                temp = float(input("Enter initial temperature (°C): "))
                pin = input("Set security PIN: ")
                thermostats[key] = SmartThermostat(room, temp, pin)
                print(f"Thermostat '{key}' added.")

    elif choice == "2":
        print("\nAll Thermostats:")
        if not thermostats:
            print("No thermostats available.")
        else:
            for key, thermo in thermostats.items():
                print(f"\nThermostat ID: {key}")
                thermo.get_status()

    elif choice == "3":
        key = input("Enter thermostat ID to set temperature: ")
        if key in thermostats:
            degrees = float(input("Enter new temperature (°C): "))
            pin = input("Enter security PIN: ")
            thermostats[key].setTemperature(degrees, pin)
        else:
            print("Thermostat not found.")

    elif choice == "4":
        key = input("Enter thermostat ID to update room name: ")
        if key in thermostats:
            new_name = input("Enter new room name: ")
            thermostats[key].update_room_name(new_name)
        else:
            print("Thermostat not found.")

    elif choice == "5":
        key = input("Enter thermostat ID to delete: ")
        if key in thermostats:
            del thermostats[key]
            print(f"Thermostat '{key}' deleted.")
        else:
            print("Thermostat not found.")

    elif choice == "6":
        print("\nEncapsulation Test:")
        for key, thermo in thermostats.items():
            print(f"\nThermostat ID: {key}")
            try:
                thermo.__currentTemperature = 1000
                thermo.__securityPin = "0000"
                print("Direct modification attempted.")
            except:
                print("Direct modification blocked.")
            thermo.get_status()

        print("\nExplanation:")
        print("Direct access to __currentTemperature and __securityPin is blocked because they are private attributes.")
        print("Encapsulation ensures that temperature changes require PIN validation, protecting room settings from unauthorized access.")

    elif choice == "7":
        print("Exiting thermostat system.")
        break

    else:
        print("Invalid choice. Please select from 1 to 7.")