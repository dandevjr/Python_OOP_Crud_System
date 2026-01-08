class Thermostat:
    def __init__(self, roomName, initialTemp):
        self.roomName = roomName                  # Public attribute
        self.__targetTemperature = initialTemp    # Private attribute

    def setTemperature(self, degrees):
        if 16 <= degrees <= 30:
            self.__targetTemperature = degrees
            print(f"{self.roomName} temperature set to {degrees}°C.")
        else:
            print("Temperature out of safe range (16–30°C). Action blocked.")

    def _technicianOverride(self, degrees, code):
        if code == "TECH999":
            self.__targetTemperature = degrees
            print(f"Technician override: {self.roomName} temperature set to {degrees}°C.")
        else:
            print("Invalid technician code. Access denied.")

    def get_status(self):
        print(f"Room: {self.roomName}")
        print(f"Target Temperature: {self.__targetTemperature}°C")

    def updateRoomName(self, new_name):
        self.roomName = new_name
        print(f"Room name updated to '{new_name}'.")

# Sample devices
devices = {
    "Device1": Thermostat("Living Room", 22),
    "Device2": Thermostat("Bedroom", 24)
}

# Main menu loop
while True:
    print("\nTHERMOSTAT MANAGEMENT SYSTEM")
    print("1. Add Multiple Devices")
    print("2. View All Devices")
    print("3. Set Temperature (Safe Range)")
    print("4. Technician Override")
    print("5. Update Room Name")
    print("6. Delete Device")
    print("7. Encapsulation Test")
    print("8. Exit")

    choice = input("Choose an option (1-8): ").strip()

    if choice == "1":
        count = int(input("How many devices do you want to add? "))
        for i in range(count):
            print(f"\nCreating device {i+1} of {count}")
            key = input("Enter device ID: ")
            if key in devices:
                print("Device ID already exists.")
            else:
                room = input("Enter room name: ")
                temp = float(input("Enter initial temperature (°C): "))
                devices[key] = Thermostat(room, temp)
                print(f"Device '{key}' added.")

    elif choice == "2":
        print("\nAll Devices:")
        if not devices:
            print("No devices available.")
        else:
            for key, device in devices.items():
                print(f"\nDevice ID: {key}")
                device.get_status()

    elif choice == "3":
        key = input("Enter device ID to set temperature: ")
        if key in devices:
            degrees = float(input("Enter new temperature (°C): "))
            devices[key].setTemperature(degrees)
        else:
            print("Device not found.")

    elif choice == "4":
        key = input("Enter device ID for technician override: ")
        if key in devices:
            degrees = float(input("Enter override temperature (°C): "))
            code = input("Enter technician code: ")
            devices[key]._technicianOverride(degrees, code)
        else:
            print("Device not found.")

    elif choice == "5":
        key = input("Enter device ID to update room name: ")
        if key in devices:
            new_name = input("Enter new room name: ")
            devices[key].updateRoomName(new_name)
        else:
            print("Device not found.")

    elif choice == "6":
        key = input("Enter device ID to delete: ")
        if key in devices:
            del devices[key]
            print(f"Device '{key}' deleted.")
        else:
            print("Device not found.")

    elif choice == "7":
        print("\nEncapsulation Test:")
        for key, device in devices.items():
            print(f"\nDevice ID: {key}")
            try:
                device.__targetTemperature = 100
                print("Direct modification attempted.")
            except:
                print("Direct modification blocked.")
            device.get_status()

        

    elif choice == "8":
        print("Exiting thermostat system.")
        break

    else:
        print("Invalid choice. Please select from 1 to 8.")