class Car:
    def __init__(self, brand, color):
        self.brand = brand              # Public attribute
        self.color = color              # Public attribute
        self.__fuel = 100.0             # Private attribute (liters)
        self.__odometer = 0.0           # Private attribute (kilometers)

    def drive(self, distance):
        fuel_needed = distance * 0.2    # Assume 0.2 liters/km
        if fuel_needed <= self.__fuel:
            self.__fuel -= fuel_needed
            self.__odometer += distance
            print(f"The car drove {distance} km.")
        else:
            print("Not enough fuel to drive that distance.")

    def refuel(self, amount):
        if amount > 0:
            self.__fuel += amount
            print(f"Refueled {amount} liters.")
        else:
            print("Invalid refuel amount.")

    def get_status(self):
        print(f"Brand: {self.brand}, Color: {self.color}")
        print(f"Fuel: {self.__fuel:.1f} L, Odometer: {self.__odometer:.1f} km")

    def update_color(self, new_color):
        self.color = new_color
        print(f"Color updated to {new_color}.")

# Sample car object
cars = {
    "Car1": Car("Toyota", "Red")
}

# Main menu loop
while True:
    print("\nCAR MANAGEMENT SYSTEM")
    print("1. Add Multiple Cars")
    print("2. View All Cars")
    print("3. Drive a Car")
    print("4. Refuel a Car")
    print("5. Update Car Color")
    print("6. Update Car Name (ID)")
    print("7. Delete a Car")
    print("8. Encapsulation Test")
    print("9. Exit")

    choice = input("Choose an option (1-9): ").strip()

    if choice == "1":
        count = int(input("How many cars do you want to add? "))
        for i in range(count):
            print(f"\nCreating car {i+1} of {count}")
            key = input("Enter car ID: ")
            if key in cars:
                print("Car ID already exists.")
            else:
                brand = input("Enter car brand: ")
                color = input("Enter car color: ")
                cars[key] = Car(brand, color)
                print(f"Car '{key}' added.")

    elif choice == "2":
        print("\nAll Cars:")
        if not cars:
            print("No cars available.")
        else:
            for key, car in cars.items():
                print(f"\nCar ID: {key}")
                car.get_status()

    elif choice == "3":
        key = input("Enter car ID to drive: ")
        if key in cars:
            distance = float(input("Enter distance to drive (km): "))
            cars[key].drive(distance)
        else:
            print("Car not found.")

    elif choice == "4":
        key = input("Enter car ID to refuel: ")
        if key in cars:
            amount = float(input("Enter fuel amount (liters): "))
            cars[key].refuel(amount)
        else:
            print("Car not found.")

    elif choice == "5":
        key = input("Enter car ID to update color: ")
        if key in cars:
            new_color = input("Enter new color: ")
            cars[key].update_color(new_color)
        else:
            print("Car not found.")

    elif choice == "6":
        old_key = input("Enter current car ID: ")
        if old_key in cars:
            new_key = input("Enter new car ID: ")
            if new_key in cars:
                print("New car ID already exists.")
            else:
                cars[new_key] = cars.pop(old_key)
                print(f"Car ID updated from '{old_key}' to '{new_key}'.")
        else:
            print("Car not found.")

    elif choice == "7":
        key = input("Enter car ID to delete: ")
        if key in cars:
            del cars[key]
            print(f"Car '{key}' deleted.")
        else:
            print("Car not found.")

    elif choice == "8":
        print("\nEncapsulation Test:")
        for key, car in cars.items():
            print(f"\nCar ID: {key}")
            try:
                car.__fuel = 1000
                car.__odometer = -500
                print("Direct modification attempted.")
            except:
                print("Direct modification blocked.")
            car.get_status()

        

    elif choice == "9":
        print("Exiting car system.")
        break

    else:
        print("Invalid choice. Please select from 1 to 9.")