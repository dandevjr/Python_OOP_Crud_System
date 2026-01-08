class Thermostat:
    def __init__(self, location, temperature):
        self.__location = location
        self.__temperature = temperature

    def get_location(self):  # GETTER
        return self.__location

    def set_location(self, value):  # SETTER
        self.__location = value

    def get_temperature(self):  # GETTER
        return self.__temperature

    def set_temperature(self, value):  # SETTER
        if 10 <= value <= 30:
            self.__temperature = value
        else:
            print("Invalid temperature. Must be between 10°C and 30°C.")

    def display_details(self):
        print(f"Location: {self.__location}, Temperature: {self.__temperature}°C")

thermostats = [
    Thermostat("Living Room", 22),
    Thermostat("Bedroom", 28)
]

while True:
    print("\nTHERMOSTAT SYSTEM")
    print("1. View All Thermostats")
    print("2. Add New Thermostat")
    print("3. Update Thermostat")
    print("4. Delete Thermostat")
    print("5. Encapsulation Test")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        if not thermostats:
            print("No thermostat records found.")
        else:
            for i, t in enumerate(thermostats, start=1):  # TRAVERSAL
                print(f"{i}. ", end="")
                t.display_details()

    elif choice == "2":
        location = input("Enter location: ")
        temp = int(input("Enter temperature (10–30°C): "))
        if 10 <= temp <= 30:
            thermostats.append(Thermostat(location, temp))  # OBJECT CREATION
            print(f"'{location}' thermostat added.")
        else:
            print("Error: Temperature must be between 10°C and 30°C.")

    elif choice == "3":
        update_location = input("Enter location to update: ")
        found = False
        for t in thermostats:
            if t.get_location().lower() == update_location.lower():
                new_temp = int(input("Enter new temperature (10–30°C): "))
                t.set_temperature(new_temp)
                print("Thermostat updated.")
                found = True
                break
        if not found:
            print("Thermostat not found.")

    elif choice == "4":
        delete_location = input("Enter location to delete: ")
        for t in thermostats:
            if t.get_location().lower() == delete_location.lower():
                thermostats.remove(t)
                print(f"Thermostat at '{delete_location}' deleted.")
                break
        else:
            print("Thermostat not found.")

    elif choice == "5":  # ENCAPSULATION TEST
        for t in thermostats:
            print(f"{t.get_location()} | Temperature: {t.get_temperature()}°C")

    elif choice == "6":
        print("Exiting system.")
        break

    else:
        print("Invalid choice.")